[app]

title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 0

# Recommended minimum and target API levels for 2025
android.minapi = 21
android.api = 33

# Ensure build-tools are installed (33.0.2 is stable for API 33)
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21

# Accept SDK licenses to prevent automated build failures
android.accept_sdk_license = True

# Skip SDK auto-update only if running offline builds
# android.skip_update = False

# Set architectures for wider device support
android.archs = armeabi-v7a, arm64-v8a

# Use SDL2 bootstrap by default for Kivy apps
# p4a.bootstrap = sdl2

# Enable AndroidX if you integrate modern gradle dependencies later
# android.enable_androidx = True

# Optional: If you use .aab for Play Store deploy
# android.release_artifact = aab

# Enable copy_libs to resolve .so library linking issues
android.copy_libs = 1

# Keep the screen on (optional for apps like games, camera, utilities)
# android.wakelock = True

# Logcat filter for cleaner debugging
android.logcat_filters = *:S python:D

# Allow backup by default
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1

# (Optional) Clean build directories for fresh builds
# build_dir = ./.buildozer
# bin_dir = ./bin

# For iOS builds (leave unchanged if not targeting iOS)
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
