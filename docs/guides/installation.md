# 🚀 Installation & Setup Guide

This guide will help you install and set up BetterTkinter for your Python projects.

## 📋 Prerequisites

### System Requirements
- **Python**: Version 3.7 or higher
- **Operating System**: Windows 10+, macOS 10.12+, or Linux (Ubuntu 18.04+)
- **Memory**: At least 512MB RAM available
- **Storage**: 50MB free space for installation

### Required Python Packages
BetterTkinter automatically installs these dependencies:
- `tkinter` (included with Python)
- `Pillow` (PIL) - For image handling
- `pystray` - For system tray integration (Windows/macOS)

## 🔧 Installation Methods

### Method 1: Install from PyPI (Recommended)

```bash
# Install the latest stable version
pip install bettertkinter

# Install with all optional dependencies
pip install bettertkinter[all]

# Upgrade to latest version
pip install --upgrade bettertkinter
```

### Method 2: Install from Source (Development)

```bash
# Clone the repository
git clone https://github.com/Velyzo/BetterTkinter.git
cd BetterTkinter

# Create virtual environment (recommended)
python -m venv btk_env
source btk_env/bin/activate  # On Windows: btk_env\Scripts\activate

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e .[dev]
```

### Method 3: Download and Install

1. Download the latest release from [GitHub Releases](https://github.com/Velyzo/BetterTkinter/releases)
2. Extract the archive
3. Navigate to the extracted folder
4. Run: `pip install .`

## 🛠️ Virtual Environment Setup (Recommended)

Using a virtual environment prevents conflicts with other Python packages:

### Windows
```cmd
# Create virtual environment
python -m venv btk_project
cd btk_project
Scripts\activate

# Install BetterTkinter
pip install bettertkinter

# Your environment is ready!
```

### macOS/Linux
```bash
# Create virtual environment
python3 -m venv btk_project
cd btk_project
source bin/activate

# Install BetterTkinter
pip install bettertkinter

# Your environment is ready!
```

## ✅ Verify Installation

Create a test file `test_installation.py`:

```python
#!/usr/bin/env python3
"""
BetterTkinter Installation Test
"""

try:
    # Test basic imports
    from bettertkinter import BTk, BTkButton, BTkLabel
    print("✅ Core components imported successfully")
    
    # Test advanced components
    from bettertkinter import BTkDialog, BTkSystemTray, BTkColorPicker
    print("✅ Advanced components imported successfully")
    
    # Test creating a basic window
    app = BTk()
    app.title("Installation Test")
    app.geometry("300x200")
    
    label = BTkLabel(app, text="BetterTkinter is working!", font_size=14)
    label.pack(pady=20)
    
    button = BTkButton(app, text="Close", command=app.quit)
    button.pack(pady=10)
    
    print("✅ Basic window created successfully")
    print("🎉 Installation verified! Close the test window to continue.")
    
    # Show the test window
    app.mainloop()
    
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Please check your installation and try again.")
except Exception as e:
    print(f"❌ Error: {e}")
    print("Installation may be incomplete.")
```

Run the test:
```bash
python test_installation.py
```

If you see the test window and all checkmarks, your installation is successful!

## 🔧 Optional Dependencies

### For System Tray Features (Windows/macOS)
```bash
pip install pystray
```

### For Advanced Image Processing
```bash
pip install Pillow
```

### For Development
```bash
pip install bettertkinter[dev]
# Includes: pytest, black, flake8, sphinx
```

## 🏗️ Project Structure Setup

### Basic Project Structure
```
my_btk_project/
├── main.py                 # Your main application file
├── components/             # Custom components
│   └── __init__.py
├── assets/                # Images, icons, etc.
│   ├── icons/
│   └── images/
├── config/                # Configuration files
│   └── settings.py
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

### Create a New Project
```bash
# Create project directory
mkdir my_btk_app
cd my_btk_app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Create requirements.txt
echo "bettertkinter>=2.0.0" > requirements.txt

# Install dependencies
pip install -r requirements.txt

# Create main application file
touch main.py  # Windows: type nul > main.py
```

### Sample main.py
```python
#!/usr/bin/env python3
"""
My BetterTkinter Application
"""

from bettertkinter import BTk, BTkButton, BTkLabel, BTkFrame

class MyApp(BTk):
    def __init__(self):
        super().__init__()
        
        # Configure main window
        self.title("My BetterTkinter App")
        self.geometry("600x400")
        self.set_theme("dark")  # or "light"
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # Main frame
        main_frame = BTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Welcome label
        welcome_label = BTkLabel(
            main_frame, 
            text="Welcome to My App!", 
            font_size=18,
            text_color="#2E8B57"
        )
        welcome_label.pack(pady=20)
        
        # Action button
        action_button = BTkButton(
            main_frame,
            text="Get Started",
            command=self.on_get_started,
            style="primary"
        )
        action_button.pack(pady=10)
    
    def on_get_started(self):
        from bettertkinter import BTkDialog
        BTkDialog.show_info("Welcome", "Let's build something amazing!")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
```

## 🔍 Troubleshooting

### Common Issues

#### Issue: "No module named 'bettertkinter'"
**Solution:**
```bash
# Make sure you're in the right environment
pip list | grep bettertkinter

# If not found, install it
pip install bettertkinter
```

#### Issue: "tkinter not found" (Linux)
**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter

# Fedora
sudo dnf install python3-tkinter
```

#### Issue: System tray not working
**Solution:**
```bash
# Install system tray support
pip install pystray

# For Linux, ensure system tray is available
sudo apt-get install libappindicator3-1
```

#### Issue: Import errors with PIL/Pillow
**Solution:**
```bash
# Reinstall Pillow
pip uninstall Pillow
pip install Pillow
```

### Getting Help

If you encounter issues:

1. **Check Python version**: `python --version` (must be 3.7+)
2. **Check pip version**: `pip --version`
3. **Update pip**: `pip install --upgrade pip`
4. **Clear pip cache**: `pip cache purge`
5. **Reinstall**: `pip uninstall bettertkinter && pip install bettertkinter`

### System-Specific Notes

#### Windows
- Use `py` instead of `python` if you have Python Launcher
- Some antivirus software may block system tray features
- Ensure Windows 10+ for full feature support

#### macOS
- May need to install Xcode Command Line Tools: `xcode-select --install`
- System tray features require macOS 10.12+

#### Linux
- Install tkinter development package
- For system tray: ensure desktop environment supports it
- Some distributions require additional packages

## 🎯 Next Steps

After successful installation:

1. **Read the [Quick Start Guide](quickstart.md)**
2. **Explore [Component Documentation](../components/)**
3. **Try the [Examples](../examples/)**
4. **Join our [Community](https://github.com/Velyzo/BetterTkinter/discussions)**

---

**Ready to build amazing GUIs with BetterTkinter!** 🎉
