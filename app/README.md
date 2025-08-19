# TCG Info (KivyMD)

A minimal KivyMD mobile app scaffold for tracking TCG data (sets, cards, products). Built with Kivy/KivyMD and packaged for Android using **Buildozer**.

> Current entrypoint: `main.py` → `TCGInfoApp` loads UI from `screen_nav.py` (a KV string named `screen_helper`).

---

## Features

- KivyMD theming (Dark, Purple A700)
- ScreenManager navigation (Dashboard, Sets, Cards, Products, etc.)
- Clean separation: Python controllers in `main.py`, KV layout in `screen_nav.py`

You can extend each `Screen` (e.g., `DashboardScreen`, `SetsScreen`) to add logic, service calls, and widgets.

---

## Project structure

```text
.
├── build.sh          # Linux helper for Buildozer (deps/venv/debug/run/logs/release)
├── buildozer.spec    # Build configuration for Android
├── main.py           # App entry (MDApp), theming, ScreenManager
└── screen_nav.py     # KV layout string (screen_helper)
```

---

## Run on Desktop (Linux/macOS/Windows)

> Desktop is great for fast iteration before packaging for Android.

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install kivy==2.3.0 kivymd
python main.py
```

If you don’t use KivyMD yet, you can temporarily switch `TCGInfoApp` to subclass `App` and remove KivyMD imports.

---

## Android Build with Buildozer

We include a portable Linux helper: **`build.sh`**. It installs system dependencies, sets up the Python venv, and wraps common Buildozer commands.

### Prerequisites

- A Linux environment (bare metal, VM, or WSL2—note: USB/ADB passthrough is limited on WSL2; use Wi‑Fi ADB)
- ~15–20 GB free disk space for Android SDK/NDK
- Android device with USB debugging or Wi‑Fi ADB enabled

### 1) Install system dependencies

```bash
chmod +x build.sh
./build.sh deps
```

This installs:

- Java 17 (OpenJDK)
- Android tools (adb)
- Autotools & C toolchain
- Python build headers (libffi, ssl, zlib, bz2, lzma, sqlite, readline, ncurses, gdbm, nss, expat, uuid)
- Other required SDK/NDK dependencies

### 2) Create and populate the virtualenv

```bash
./build.sh venv
```

This installs **buildozer** (and **cython**) into `.venv`.

### 3) Initialize (optional)

If you don’t have `buildozer.spec` yet:

```bash
./build.sh init
```

### 4) Build, deploy, and run

```bash
./build.sh debug          # Build a debug APK
./build.sh run            # Deploy & run on connected device
./build.sh logcat         # Tail device logs (Ctrl+C to stop)
```

> If `./build.sh run` isn’t available on your shell, you can also do:

```bash
buildozer android deploy run
buildozer android logcat
```

### 5) Release builds

- **APK** (sideload): `./build.sh release-apk`
- **AAB** (Play Store): `./build.sh release-aab`

You’ll need a keystore:

```bash
keytool -genkeypair -v -keystore mykey.jks -alias myalias -keyalg RSA -keysize 4096 -validity 10000
```

Then either add to `buildozer.spec`:

```ini
[android]
android.release_keystore = mykey.jks
android.release_keyalias = myalias
```

Or export env vars before running release:

```bash
export ANDROID_KEYSTORE=./mykey.jks
export ANDROID_KEYALIAS=myalias
export ANDROID_KEYSTORE_PASSWORD=...
export ANDROID_KEY_PASSWORD=...
./build.sh release-aab
```

---

## `buildozer.spec` quick guide

Key fields to review/edit:

```ini
[app]
title = TCG Info
package.name = tcginfo
package.domain = org.example       # reverse DNS; make it unique
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,webp,svg,ttf,otf,json,db,ini,txt,md

# MUST include everything you import in Python
requirements = python3,kivy==2.3.0,kivymd,requests,certifi,urllib3

# Orientation and fullscreen
orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Android target/min API
android.api = 33
android.minapi = 24

# Build artifact for Play Store
android.release_artifact = aab
```

Optional (when you have assets):

```ini
icon.filename = assets/images/icon.png
android.adaptive_icon.foreground = assets/images/ic_adaptive_foreground.png
android.adaptive_icon.background = assets/images/ic_adaptive_background.png
```

Advanced logging (helpful during debugging):

```ini
log_level = 1
android.logcat_filters = *:S python:D AndroidRuntime:E libc:E
```

---

## Troubleshooting

**App opens then closes immediately:**

- Check `buildozer android logcat` for a Python traceback.
- Common causes:
  - `ModuleNotFoundError: kivymd` → ensure `kivymd` is in `requirements`, then `buildozer android clean` and rebuild.
  - KV parse errors → invalid KV in `screen_nav.py` (line/col will be in logcat).

**`autoreconf: not found` while building `libffi`**

- Install autotools. Our `./build.sh deps` handles this (adds `autoconf automake libtool pkg-config m4 gettext`).

**`ModuleNotFoundError: No module named '_ctypes'` (hostpython):**

- Means Python was built without libffi headers.
- Run `./build.sh deps` then `buildozer android clean` and rebuild.

**`Cython (cython) not found`:**

- `./build.sh venv` now installs cython automatically. You can also run:

  ```bash
  source .venv/bin/activate && pip install cython
  ```

**KivyMD not pulled from PyPI:**

- Point to GitHub:

  ```ini
  requirements = python3,kivy==2.3.0,kivymd @ https://github.com/kivymd/KivyMD/archive/refs/heads/master.zip
  ```

**Network/HTTP issues on Android 9+:**

- For dev HTTP endpoints, enable cleartext temporarily:

  ```ini
  android.allow_cleartext = 1
  ```

  Remove before production.

**WSL2 + ADB:**

- Prefer Wi‑Fi ADB (`adb tcpip 5555; adb connect <ip>:5555`) or build on a native Linux host.

---

## Development tips

- Keep `requirements` minimal to avoid heavy/fragile builds.
- Test early on a real device (performance differs from desktop).
- Organize screens/widgets/services into packages as the app grows.
- Use `logging` instead of `print` for structured logs on device.

---

## License

MIT (or your choice). Add a `LICENSE` file in the repo root.
