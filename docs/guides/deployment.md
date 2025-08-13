# 🚀 Deployment & Distribution Guide

Complete guide for packaging and distributing BetterTkinter applications.

## 📦 Packaging Options

### 1. PyInstaller (Recommended)

PyInstaller is the most popular option for creating standalone executables.

#### Installation
```bash
pip install pyinstaller
```

#### Basic Usage
```bash
# Create a single executable file
pyinstaller --onefile your_app.py

# Create a directory distribution
pyinstaller your_app.py

# With custom icon
pyinstaller --onefile --icon=app_icon.ico your_app.py
```

#### Advanced Options
```bash
# Hide console window (for GUI apps)
pyinstaller --onefile --windowed your_app.py

# Include additional files
pyinstaller --onefile --add-data "assets/*;assets/" your_app.py

# Exclude unused modules
pyinstaller --onefile --exclude-module tkinter.test your_app.py

# Custom name and output directory
pyinstaller --onefile --name "MyApp" --distpath ./dist your_app.py
```

#### Complete Example
```bash
pyinstaller \
    --onefile \
    --windowed \
    --icon=app_icon.ico \
    --name "BetterTkinter App" \
    --add-data "assets/*;assets/" \
    --add-data "config.json;." \
    --exclude-module tkinter.test \
    --distpath ./release \
    main.py
```

### 2. cx_Freeze

Cross-platform alternative to PyInstaller.

#### Installation
```bash
pip install cx_freeze
```

#### Setup Script (setup.py)
```python
import sys
from cx_Freeze import setup, Executable

# Dependencies
build_exe_options = {
    "packages": ["bettertkinter"],
    "excludes": ["tkinter.test"],
    "include_files": ["assets/", "config.json"]
}

# Base for GUI applications
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="BetterTkinter App",
    version="1.0",
    description="My BetterTkinter Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="app_icon.ico")]
)
```

#### Build Command
```bash
python setup.py build
```

### 3. Auto-py-to-exe (GUI for PyInstaller)

User-friendly GUI interface for PyInstaller.

#### Installation
```bash
pip install auto-py-to-exe
```

#### Usage
```bash
auto-py-to-exe
```

## 📱 Platform-Specific Deployment

### Windows

#### Creating Windows Installer
Use NSIS (Nullsoft Scriptable Install System) or Inno Setup.

**NSIS Example Script:**
```nsis
!include "MUI2.nsh"

Name "BetterTkinter App"
OutFile "BetterTkinter_App_Setup.exe"
InstallDir "$PROGRAMFILES\BetterTkinter App"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

Section "MainSection" SEC01
    SetOutPath "$INSTDIR"
    File "dist\your_app.exe"
    File /r "assets\"
    
    CreateDirectory "$SMPROGRAMS\BetterTkinter App"
    CreateShortcut "$SMPROGRAMS\BetterTkinter App\BetterTkinter App.lnk" "$INSTDIR\your_app.exe"
    CreateShortcut "$DESKTOP\BetterTkinter App.lnk" "$INSTDIR\your_app.exe"
SectionEnd
```

#### Windows Store Deployment
Use the Desktop Bridge to convert desktop apps to UWP.

### macOS

#### Creating .app Bundle
```bash
# Using PyInstaller
pyinstaller --onefile --windowed --icon=app_icon.icns your_app.py

# The .app will be in dist/
```

#### Creating DMG Installer
```bash
# Install create-dmg
brew install create-dmg

# Create DMG
create-dmg \
    --volname "BetterTkinter App" \
    --volicon "app_icon.icns" \
    --window-pos 200 120 \
    --window-size 600 300 \
    --icon-size 100 \
    --icon "your_app.app" 175 120 \
    --hide-extension "your_app.app" \
    --app-drop-link 425 120 \
    "BetterTkinter_App.dmg" \
    "dist/"
```

#### Code Signing (for distribution)
```bash
# Sign the app
codesign --force --deep --sign "Developer ID Application: Your Name" your_app.app

# Verify signature
codesign --verify --deep --strict your_app.app
```

### Linux

#### Creating AppImage
```bash
# Download AppImage tools
wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
chmod +x appimagetool-x86_64.AppImage

# Create AppDir structure
mkdir -p MyApp.AppDir/usr/bin
cp dist/your_app MyApp.AppDir/usr/bin/

# Create .desktop file
cat > MyApp.AppDir/MyApp.desktop << EOF
[Desktop Entry]
Name=BetterTkinter App
Exec=your_app
Icon=app_icon
Type=Application
Categories=Utility;
EOF

# Add icon
cp app_icon.png MyApp.AppDir/

# Create AppImage
./appimagetool-x86_64.AppImage MyApp.AppDir
```

#### Creating .deb Package
```bash
# Create package structure
mkdir -p myapp_1.0-1_amd64/{DEBIAN,usr/bin,usr/share/applications,usr/share/pixmaps}

# Control file
cat > myapp_1.0-1_amd64/DEBIAN/control << EOF
Package: bettertkinter-app
Version: 1.0-1
Section: utils
Priority: optional
Architecture: amd64
Maintainer: Your Name <your.email@example.com>
Description: BetterTkinter Application
 A sample application built with BetterTkinter
EOF

# Copy files
cp dist/your_app myapp_1.0-1_amd64/usr/bin/
cp app.desktop myapp_1.0-1_amd64/usr/share/applications/
cp app_icon.png myapp_1.0-1_amd64/usr/share/pixmaps/

# Build package
dpkg-deb --build myapp_1.0-1_amd64
```

## ⚙️ Optimization Tips

### Reducing File Size

#### 1. Exclude Unused Modules
```python
# In PyInstaller spec file
excludes = [
    'tkinter.test',
    'unittest',
    'pdb',
    'doctest',
    'difflib'
]
```

#### 2. Use UPX Compression
```bash
# Install UPX
# Windows: Download from https://upx.github.io/
# macOS: brew install upx  
# Linux: apt install upx-ucl

# Use with PyInstaller
pyinstaller --onefile --upx-dir=/path/to/upx your_app.py
```

#### 3. Minimize Dependencies
```python
# Only import what you need
from bettertkinter import BTk, BTkButton, BTkLabel
# Instead of: import bettertkinter as btk
```

### Performance Optimization

#### 1. Lazy Loading
```python
class MyApp(BTk):
    def __init__(self):
        super().__init__()
        self.heavy_component = None
    
    def load_heavy_component(self):
        if self.heavy_component is None:
            # Load only when needed
            self.heavy_component = HeavyComponent(self)
```

#### 2. Thread Management
```python
import threading
import queue

class AsyncApp(BTk):
    def __init__(self):
        super().__init__()
        self.task_queue = queue.Queue()
        self.start_worker_thread()
    
    def start_worker_thread(self):
        def worker():
            while True:
                task = self.task_queue.get()
                if task is None:
                    break
                # Process task
                self.after(0, lambda: self.update_ui(task))
        
        self.worker_thread = threading.Thread(target=worker, daemon=True)
        self.worker_thread.start()
```

## 🔧 Configuration Management

### Settings File Structure
```python
# config.py
import json
import os
from pathlib import Path

class Config:
    def __init__(self):
        self.config_dir = Path.home() / ".myapp"
        self.config_file = self.config_dir / "config.json"
        self.ensure_config_dir()
        self.settings = self.load_settings()
    
    def ensure_config_dir(self):
        self.config_dir.mkdir(exist_ok=True)
    
    def load_settings(self):
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        
        return self.default_settings()
    
    def default_settings(self):
        return {
            "theme": "light",
            "window_geometry": "800x600",
            "auto_save": True,
            "language": "en"
        }
    
    def save_settings(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=2)
    
    def get(self, key, default=None):
        return self.settings.get(key, default)
    
    def set(self, key, value):
        self.settings[key] = value
        self.save_settings()

# Usage in your app
config = Config()
theme = config.get("theme", "light")
config.set("last_file", "/path/to/file.txt")
```

### Environment-Specific Configuration
```python
import os

class AppConfig:
    def __init__(self):
        self.environment = os.getenv("APP_ENV", "production")
        self.debug = self.environment == "development"
        
        if self.environment == "development":
            self.log_level = "DEBUG"
            self.window_size = "1200x800"
        else:
            self.log_level = "INFO"
            self.window_size = "800x600"
    
    @property
    def is_frozen(self):
        """Check if running as compiled executable"""
        return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
    
    def get_resource_path(self, relative_path):
        """Get absolute path to resource for both dev and compiled versions"""
        if self.is_frozen:
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        
        return os.path.join(base_path, relative_path)
```

## 🐛 Troubleshooting Common Issues

### Import Errors

#### Issue: ModuleNotFoundError in compiled executable
```python
# Solution: Ensure all imports are explicit
# Bad:
# from . import module_name

# Good:
from mypackage import module_name

# In PyInstaller spec file:
hiddenimports = ['mypackage.module_name']
```

#### Issue: tkinter import problems
```python
# Solution: Handle different Python versions
try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk
```

### Resource Files

#### Issue: Files not found in compiled executable
```python
# Solution: Use resource path helper
import sys
import os

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Usage
icon_path = resource_path("assets/icon.ico")
config_path = resource_path("config.json")
```

### Permission Issues

#### Issue: Write permission errors
```python
# Solution: Use appropriate directories
import os
from pathlib import Path

# For user data
user_data_dir = Path.home() / ".myapp"
user_data_dir.mkdir(exist_ok=True)

# For temporary files
import tempfile
temp_dir = Path(tempfile.gettempdir()) / "myapp"
temp_dir.mkdir(exist_ok=True)

# For logs (Windows)
if os.name == 'nt':
    log_dir = Path(os.environ['APPDATA']) / "MyApp"
else:
    log_dir = Path.home() / ".myapp" / "logs"
```

### Antivirus False Positives

#### Prevention Strategies
1. **Code Signing**: Sign your executables
2. **VirusTotal Scanning**: Check your builds
3. **Whitelist Requests**: Submit to major antivirus vendors
4. **Documentation**: Provide clear installation instructions

```python
# Add version info to PyInstaller
version_info = """
VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=(1, 0, 0, 0),
        prodvers=(1, 0, 0, 0),
        mask=0x3f,
        flags=0x0,
        OS=0x4,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo([
            StringTable('040904B0', [
                StringStruct('CompanyName', 'Your Company'),
                StringStruct('FileDescription', 'BetterTkinter Application'),
                StringStruct('FileVersion', '1.0.0.0'),
                StringStruct('ProductName', 'Your App Name'),
                StringStruct('ProductVersion', '1.0.0.0')
            ])
        ]),
        VarFileInfo([VarStruct('Translation', [1033, 1200])])
    ]
)
"""

# Use in spec file
exe = EXE(...,
          version='version_info.txt')
```

## 📊 Testing Before Distribution

### Automated Testing Script
```python
# test_build.py
import subprocess
import sys
import os
from pathlib import Path

def test_build():
    """Test the built executable"""
    
    if sys.platform == "win32":
        exe_path = Path("dist/your_app.exe")
    else:
        exe_path = Path("dist/your_app")
    
    if not exe_path.exists():
        print(f"❌ Executable not found: {exe_path}")
        return False
    
    print(f"✅ Executable found: {exe_path}")
    
    # Test executable runs
    try:
        result = subprocess.run([str(exe_path), "--version"], 
                               capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ Executable runs successfully")
            print(f"   Version output: {result.stdout.strip()}")
        else:
            print(f"❌ Executable failed with code {result.returncode}")
            return False
    except subprocess.TimeoutExpired:
        print(f"❌ Executable timed out")
        return False
    except Exception as e:
        print(f"❌ Error running executable: {e}")
        return False
    
    # Check file size
    size_mb = exe_path.stat().st_size / (1024 * 1024)
    print(f"📦 Executable size: {size_mb:.1f} MB")
    
    if size_mb > 100:  # Warn if over 100MB
        print("⚠️  Large executable size - consider optimization")
    
    return True

if __name__ == "__main__":
    success = test_build()
    sys.exit(0 if success else 1)
```

### Manual Testing Checklist

- [ ] Application starts without errors
- [ ] All features work correctly
- [ ] Files can be opened/saved
- [ ] Settings are preserved between runs
- [ ] Application closes cleanly
- [ ] No console windows appear (for GUI apps)
- [ ] Icons display correctly
- [ ] Menu items work
- [ ] Keyboard shortcuts function
- [ ] Error handling works properly

## 🚀 Distribution Platforms

### Desktop Application Stores

#### Microsoft Store
- Use Desktop Bridge for Win32 apps
- Follow Store policies and guidelines
- Implement Store-specific features

#### Mac App Store  
- Code signing required
- Sandboxing restrictions
- Follow App Store Review Guidelines

#### Snap Store (Linux)
```bash
# Create snapcraft.yaml
name: bettertkinter-app
version: '1.0'
summary: BetterTkinter Application
description: A sample application built with BetterTkinter

base: core20
confinement: strict
grade: stable

apps:
  bettertkinter-app:
    command: usr/bin/your_app
    desktop: usr/share/applications/your_app.desktop

parts:
  my-app:
    plugin: dump
    source: dist/
    organize:
      your_app: usr/bin/your_app
```

### Web Distribution

#### GitHub Releases
```bash
# Create release with GitHub CLI
gh release create v1.0.0 \
    --title "Version 1.0.0" \
    --notes "First release" \
    dist/your_app.exe#Windows \
    dist/your_app.dmg#macOS \
    dist/your_app.AppImage#Linux
```

#### Custom Website
- Provide download links for all platforms
- Include installation instructions
- Offer checksums for verification

## 📈 Analytics and Updates

### Usage Analytics
```python
import requests
import json
import uuid
import os

class Analytics:
    def __init__(self, app_version):
        self.app_version = app_version
        self.user_id = self.get_or_create_user_id()
        self.analytics_url = "https://your-analytics-endpoint.com/track"
    
    def get_or_create_user_id(self):
        config_file = Path.home() / ".myapp" / "user_id"
        if config_file.exists():
            return config_file.read_text().strip()
        else:
            user_id = str(uuid.uuid4())
            config_file.parent.mkdir(exist_ok=True)
            config_file.write_text(user_id)
            return user_id
    
    def track_event(self, event_name, properties=None):
        try:
            data = {
                'user_id': self.user_id,
                'event': event_name,
                'properties': properties or {},
                'app_version': self.app_version,
                'platform': sys.platform
            }
            
            requests.post(self.analytics_url, json=data, timeout=5)
        except:
            # Fail silently - don't break app for analytics
            pass
```

### Update Checking
```python
import requests
import json
from packaging import version

class UpdateChecker:
    def __init__(self, current_version, update_url):
        self.current_version = current_version
        self.update_url = update_url
    
    def check_for_updates(self):
        try:
            response = requests.get(self.update_url, timeout=10)
            response.raise_for_status()
            
            update_info = response.json()
            latest_version = update_info.get('latest_version')
            
            if version.parse(latest_version) > version.parse(self.current_version):
                return {
                    'available': True,
                    'version': latest_version,
                    'download_url': update_info.get('download_url'),
                    'release_notes': update_info.get('release_notes', '')
                }
            else:
                return {'available': False}
                
        except Exception as e:
            print(f"Update check failed: {e}")
            return {'available': False, 'error': str(e)}

# Usage
checker = UpdateChecker("1.0.0", "https://api.myapp.com/version")
update_info = checker.check_for_updates()

if update_info['available']:
    result = BTkDialog.ask_yes_no(
        "Update Available",
        f"Version {update_info['version']} is available.\n"
        "Would you like to download it?"
    )
    if result == "Yes":
        import webbrowser
        webbrowser.open(update_info['download_url'])
```

---

**Ready to distribute your BetterTkinter applications to the world!** 🌍

For more information, see:
- [Installation Guide](installation.md)
- [API Reference](../api/README.md)
- [Examples Collection](../examples/README.md)
