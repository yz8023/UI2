#!/usr/bin/env bash
# 手工构建 APK（不依赖 Gradle）：aapt2 → javac → d8 → zipalign → apksigner
set -euo pipefail

SDK=${ANDROID_SDK_ROOT:-/tmp/asdk}
BT=$SDK/android-14
PLATFORM=$SDK/platforms/android-34/android.jar
JAVA_HOME=${JAVA_HOME:-/var/tmp/jdk17/jdk-17.0.21+9}
PATH=$JAVA_HOME/bin:$BT:$PATH

SRC=$(cd "$(dirname "$0")" && pwd)
ROOT=$(dirname "$SRC")
BUILD=$SRC/build
OUT=${1:-$ROOT/apk}

rm -rf "$BUILD"
mkdir -p "$BUILD/res" "$BUILD/gen" "$BUILD/classes" "$BUILD/dex" "$BUILD/assets/www" "$OUT"

echo "== 1/6 拷贝离线页面到 assets/www"
cd "$ROOT"
cp index.html "$BUILD/assets/www/"
for d in app motion-demos glass-demos video-demos; do
  mkdir -p "$BUILD/assets/www/$d"
  find "$d" -maxdepth 1 -name '*.html' -exec cp {} "$BUILD/assets/www/$d/" \;
done
# 完整素材库：47 个 HTML（总览 + 46 条）+ App（68 条 / XPopup 全量 / motion-web 全量）
cd "$ROOT/library"
find . -maxdepth 2 -name '*.html' | while read -r f; do
  mkdir -p "$BUILD/assets/www/library/$(dirname "$f")"
  cp "$f" "$BUILD/assets/www/library/$f"
done
cd "$ROOT"
cp "$SRC/AndroidManifest.xml" "$BUILD/AndroidManifest.xml"

echo "== 2/6 aapt2 compile / link"
aapt2 compile --dir "$SRC/res" -o "$BUILD/res.zip"
aapt2 link -o "$BUILD/base.apk" \
  -I "$PLATFORM" \
  --manifest "$BUILD/AndroidManifest.xml" \
  -R "$BUILD/res.zip" \
  --java "$BUILD/gen" \
  --auto-add-overlay \
  --no-version-vectors

echo "== 3/6 javac"
find "$SRC/java" "$BUILD/gen" -name '*.java' > "$BUILD/sources.txt"
javac -source 8 -target 8 -nowarn -encoding UTF-8 \
  -bootclasspath "$PLATFORM" \
  -d "$BUILD/classes" \
  @"$BUILD/sources.txt" 2>&1 | sed '/bootstrap class path/d'

echo "== 4/6 d8 → classes.dex"
find "$BUILD/classes" -name '*.class' > "$BUILD/classes.txt"
d8 --lib "$PLATFORM" --min-api 24 --release \
   --output "$BUILD/dex" @"$BUILD/classes.txt"

echo "== 5/6 打包（Python 写 zip，保证中文文件名 UTF-8 标志位）+ zipalign"
python3 "$SRC/add_assets.py" "$BUILD/base.apk" "$BUILD/unsigned.apk" "$BUILD/dex/classes.dex" "$BUILD/assets"
cd "$BUILD"
zipalign -f -p 4 unsigned.apk aligned.apk

echo "== 6/6 签名"
KS=$SRC/debug.keystore
if [ ! -f "$KS" ]; then
  keytool -genkeypair -v -keystore "$KS" -storepass android -keypass android \
    -alias androiddebugkey -keyalg RSA -keysize 2048 -validity 10000 \
    -dname "CN=UI Material Library, O=Arena, C=SG" >/dev/null 2>&1
fi
APK="$OUT/uikit-library-3.1.apk"
apksigner sign --ks "$KS" --ks-pass pass:android --key-pass pass:android \
  --ks-key-alias androiddebugkey --v1-signing-enabled true --v2-signing-enabled true \
  --out "$APK" aligned.apk
apksigner verify --print-certs "$APK" | head -5
ls -lh "$APK"
echo "APK: $APK"
