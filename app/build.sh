#!/usr/bin/env bash


#
# build.sh — One-command Android build for Kivy/KivyMD with Buildozer
# Usage:
#   ./build.sh deps          # install system deps (apt/dnf/pacman)
#   ./build.sh venv          # create .venv and install Python deps (buildozer)
#   ./build.sh init          # buildozer init (creates buildozer.spec if missing)
#   ./build.sh debug         # build debug APK
#   ./build.sh run           # deploy & run on connected device
#   ./build.sh logcat        # stream device logs
#   ./build.sh clean         # clean build artifacts
#   ./build.sh release-apk   # signed release APK (needs keystore in spec)
#   ./build.sh release-aab   # signed Play Store bundle (AAB)
#
# Optional env:
#   ANDROID_KEYSTORE=path/to.jks ANDROID_KEYALIAS=alias \
#   ANDROID_KEYSTORE_PASSWORD=... ANDROID_KEY_PASSWORD=... ./build.sh release-apk
#
# Notes:
# - Tested on Ubuntu 22.04/24.04, Fedora 39+, Arch/Manjaro.
# - On WSL2, USB/ADB passthrough is tricky. Use a real Linux host or network ADB.
#



# --- Ensure we're running under bash ---
if [ -z "$BASH_VERSION" ]; then
  if command -v bash >/dev/null 2>&1; then
    echo "⚠️  Not running under bash — restarting..."
    exec bash "$0" "$@"
  else
    echo "❌ This script requires bash, but it’s not installed."
    echo "   Please install bash and try again."
    exit 1
  fi
fi

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${VENV_DIR:-$ROOT_DIR/.venv}"
PYTHON="${PYTHON:-python3}"

has_cmd() { command -v "$1" >/dev/null 2>&1; }

detect_pm() {
  if has_cmd apt-get; then echo "apt"; return; fi
  if has_cmd dnf; then echo "dnf"; return; fi
  if has_cmd pacman; then echo "pacman"; return; fi
  echo "unknown"
}

install_deps_apt() {
  sudo apt-get update
  sudo apt-get install -y \
    git python3 python3-venv python3-pip \
    openjdk-17-jdk unzip zip adb \
    autoconf automake libtool pkg-config m4 gettext \
    libffi-dev libssl-dev zlib1g-dev libbz2-dev liblzma-dev \
    libsqlite3-dev libreadline-dev libncurses5-dev libgdbm-dev \
    libnss3-dev libexpat1-dev uuid-dev \
    build-essential
}

install_deps_dnf() {
  sudo dnf install -y \
    @development-tools git python3-virtualenv python3-pip \
    java-17-openjdk unzip zip android-tools \
    autoconf automake libtool pkgconf-pkg-config gettext m4 \
    libffi-devel openssl-devel zlib-devel bzip2-devel xz-devel \
    sqlite-devel readline-devel ncurses-devel gdbm-devel \
    nss-devel expat-devel libuuid-devel
}

install_deps_pacman() {
  sudo pacman -Syu --noconfirm
  sudo pacman -S --noconfirm \
    base-devel git python python-pip \
    jdk17-openjdk unzip zip android-tools \
    autoconf automake libtool pkgconf gettext m4 \
    libffi openssl zlib bzip2 xz sqlite \
    readline ncurses gdbm nss expat util-linux-libs
}

deps() {
  pm="$(detect_pm)"
  case "$pm" in
    apt) install_deps_apt ;;
    dnf) install_deps_dnf ;;
    pacman) install_deps_pacman ;;
    *) echo "Unsupported distro. Install: full build-essential toolchain, git, python3(+venv,pip), JDK 17, unzip, zip, adb, autotools, and Python build deps (libffi, ssl, zlib, bz2, lzma, sqlite, readline, ncurses, gdbm, nss, expat, uuid)" >&2; exit 1;;
  esac
  echo "System dependencies installed."
}

venv() {
  if [ ! -d "$VENV_DIR" ]; then
    "$PYTHON" -m venv "$VENV_DIR"
  fi
  # shellcheck disable=SC1090
  source "$VENV_DIR/bin/activate"
  python -m pip install --upgrade pip setuptools wheel cython
  pip install buildozer
  echo "Virtualenv ready at $VENV_DIR"
}

ensure_buildozer() {
  # shellcheck disable=SC1090
  source "$VENV_DIR/bin/activate"
  if ! has_cmd buildozer; then
    echo "Buildozer not found in venv. Run: ./build.sh venv" >&2
    exit 1
  fi
}

init() {
  ensure_buildozer
  if [ -f "$ROOT_DIR/buildozer.spec" ]; then
    echo "buildozer.spec already exists — skipping init."
  else
    buildozer init
    echo "Initialized buildozer.spec. Review and edit before building."
  fi
}

debug() {
  ensure_buildozer
  buildozer -v android debug
  echo "Debug build complete. APK should be in bin/"
}

run() {
  ensure_buildozer
  buildozer android deploy run
}

logcat() {
  ensure_buildozer
  buildozer android logcat
}

clean() {
  ensure_buildozer
  buildozer android clean
  rm -rf .buildozer
  echo "Cleaned."
}

release_apk() {
  ensure_buildozer
  export P4A_RELEASE_KEYSTORE="${ANDROID_KEYSTORE:-${P4A_RELEASE_KEYSTORE:-}}"
  export P4A_RELEASE_KEYALIAS="${ANDROID_KEYALIAS:-${P4A_RELEASE_KEYALIAS:-}}"
  export P4A_RELEASE_KEYSTORE_PASS="${ANDROID_KEYSTORE_PASSWORD:-${P4A_RELEASE_KEYSTORE_PASS:-}}"
  export P4A_RELEASE_KEYPASS="${ANDROID_KEY_PASSWORD:-${P4A_RELEASE_KEYPASS:-}}"
  buildozer -v android release
  echo "Release APK build complete. See bin/"
}

release_aab() {
  ensure_buildozer
  export P4A_RELEASE_KEYSTORE="${ANDROID_KEYSTORE:-${P4A_RELEASE_KEYSTORE:-}}"
  export P4A_RELEASE_KEYALIAS="${ANDROID_KEYALIAS:-${P4A_RELEASE_KEYALIAS:-}}"
  export P4A_RELEASE_KEYSTORE_PASS="${ANDROID_KEYSTORE_PASSWORD:-${P4A_RELEASE_KEYSTORE_PASS:-}}"
  export P4A_RELEASE_KEYPASS="${ANDROID_KEY_PASSWORD:-${P4A_RELEASE_KEYPASS:-}}"
  buildozer -v android release aab
  echo "Release AAB build complete. See bin/"
}

case "${1:-}" in
  deps) deps ;;
  venv) venv ;;
  init) init ;;
  debug) debug ;;
  run) run ;;
  logcat) logcat ;;
  clean) clean ;;
  release-apk) release_apk ;;
  release-aab) release_aab ;;
  ""|-h|--help|help)
    sed -n '1,160p' "$0"
    ;;
  *)
    echo "Unknown command: $1" >&2
    exit 1
    ;;
esac
