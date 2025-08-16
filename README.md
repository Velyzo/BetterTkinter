# BetterTkinter

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/pypi/v/bettertkinter?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI">
  <img src="https://img.shields.io/github/stars/Velyzo/BetterTkinter?style=for-the-badge&logo=github" alt="Stars">
  <img src="https://img.shields.io/pypi/dm/bettertkinter?style=for-the-badge&logo=pypi&logoColor=white" alt="Downloads">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <strong>🎨 A modern, beautiful, and feature-rich Tkinter UI framework for Python</strong>
</p>

<p align="center">
  Transform your Python desktop applications with stunning modern interfaces, advanced widgets, and effortless theming.
</p>

<div align="center">

[📚 **Documentation**](https://velyzo.github.io/BetterTkinterDocs/) • [🎮 **Live Demo**](demo/) • [🚀 **Get Started**](#-quick-start) • [💡 **Examples**](#-examples--demos)

</div>

---

## ✨ **Why BetterTkinter?**

**BetterTkinter** revolutionizes Python GUI development by providing a modern, intuitive framework built on Tkinter's solid foundation. Create professional-grade desktop applications with minimal code and maximum visual impact.

### 🎯 **Key Highlights**

| 🌟 **Feature** | 🎨 **Description** |
|---------------|------------------|
| **Modern Design** | Beautiful, contemporary widgets that look native on all platforms |
| **Smart Theming** | Light/Dark/Auto themes with customizable color schemes |
| **Advanced Widgets** | Color pickers, dialogs, navigation bars, progress bars, and more |
| **Developer Friendly** | Intuitive API, comprehensive documentation, rich examples |
| **Production Ready** | Robust, tested, and used in real-world applications |
| **Cross Platform** | Windows, macOS, and Linux support out of the box |

---

## 📦 **Installation**

### Quick Install
```bash
pip install bettertkinter
```

### Development Install
```bash
git clone https://github.com/Velyzo/BetterTkinter.git
cd BetterTkinter
pip install -e .
```

> 💡 **Tip:** Use a virtual environment for better dependency management. See our [Installation Guide](https://velyzo.github.io/BetterTkinterDocs/guides/installation/) for detailed instructions.

---

## 🚀 **Quick Start**

Get up and running in under 2 minutes:

```python
from bettertkinter import BTk, BTkButton, BTkFrame, BTkLabel

# Create a modern window
app = BTk(title="🎨 My Beautiful App", theme="dark", geometry="500x350")

# Add a stylish frame
frame = BTkFrame(app, corner_radius=15)
frame.pack(fill="both", expand=True, padx=20, pady=20)

# Beautiful label
BTkLabel(frame, text="Welcome to BetterTkinter! 🚀", 
         font_size=18).pack(pady=20)

# Modern buttons with different styles
BTkButton(frame, text="Primary Action", style="primary").pack(pady=5)
BTkButton(frame, text="Success Action", style="success").pack(pady=5)
BTkButton(frame, text="Warning Action", style="warning").pack(pady=5)

app.mainloop()
```

**That's it!** You now have a beautiful, modern GUI application.

---

## 🎮 **Examples & Demos**

### 🔥 **Try the Interactive Demo**
Experience BetterTkinter's full power with our comprehensive demo:

```bash
# Run the main demo
python demo.py

# Or explore the demo folder
cd demo/
python advanced_demo.py
```

### 📂 **Demo Directory**
Our [`demo/`](demo/) folder contains:
- **Complete Applications** - Full-featured apps showcasing real-world usage
- **Component Demos** - Individual widget demonstrations
- **Theme Showcases** - Different styling approaches
- **Integration Examples** - Working with databases, APIs, and more

### 💡 **Code Examples**
Quick examples for common tasks:

<details>
<summary>📝 <strong>Form with Validation</strong></summary>

```python
from bettertkinter import BTk, BTkFrame, BTkLabel, BTkEntry, BTkButton, BTkDialog

class LoginForm(BTk):
    def __init__(self):
        super().__init__(title="Login", geometry="400x300", theme="light")
        
        frame = BTkFrame(self)
        frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        BTkLabel(frame, text="🔐 Login", font_size=20).pack(pady=20)
        
        self.username = BTkEntry(frame, placeholder_text="Username")
        self.username.pack(fill="x", pady=10)
        
        self.password = BTkEntry(frame, placeholder_text="Password", show="*")
        self.password.pack(fill="x", pady=10)
        
        BTkButton(frame, text="Login", style="primary", 
                 command=self.login).pack(pady=20, fill="x")
    
    def login(self):
        if self.username.get() and self.password.get():
            BTkDialog.show_success("Success", "Welcome back!")
        else:
            BTkDialog.show_error("Error", "Please fill all fields")

LoginForm().mainloop()
```
</details>

<details>
<summary>🎨 <strong>Color Picker App</strong></summary>

```python
from bettertkinter import BTk, BTkColorPicker, BTkLabel, BTkFrame

class ColorApp(BTk):
    def __init__(self):
        super().__init__(title="Color Studio", geometry="600x500")
        
        frame = BTkFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        BTkLabel(frame, text="🎨 Color Picker Studio", font_size=18).pack(pady=10)
        
        self.color_picker = BTkColorPicker(frame, width=400, height=300)
        self.color_picker.pack(pady=20)
        
        self.color_label = BTkLabel(frame, text="Selected: #FF6B35", font_size=14)
        self.color_label.pack(pady=10)
        
        self.color_picker.bind_color_change(self.on_color_change)
    
    def on_color_change(self, color):
        self.color_label.configure(text=f"Selected: {color}")

ColorApp().mainloop()
```
</details>

<details>
<summary>📊 <strong>Dashboard Example</strong></summary>

```python
from bettertkinter import BTk, BTkFrame, BTkLabel, BTkProgressBar, BTkNavBar

class Dashboard(BTk):
    def __init__(self):
        super().__init__(title="Analytics Dashboard", geometry="800x600", theme="dark")
        
        # Navigation
        nav = BTkNavBar(self, items=["Overview", "Analytics", "Settings"])
        nav.pack(fill="x", padx=10, pady=10)
        
        # Content frame
        content = BTkFrame(self)
        content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Metrics
        BTkLabel(content, text="📈 Key Metrics", font_size=16).pack(pady=10)
        
        metrics_frame = BTkFrame(content)
        metrics_frame.pack(fill="x", pady=10)
        
        # Progress indicators
        for metric, value in [("Revenue", 85), ("Users", 92), ("Growth", 78)]:
            metric_frame = BTkFrame(metrics_frame)
            metric_frame.pack(side="left", fill="both", expand=True, padx=5)
            
            BTkLabel(metric_frame, text=metric).pack(pady=5)
            progress = BTkProgressBar(metric_frame)
            progress.set_value(value)
            progress.pack(fill="x", padx=10, pady=5)
            BTkLabel(metric_frame, text=f"{value}%").pack()

Dashboard().mainloop()
```
</details>

---

## 🧩 **Component Library**

BetterTkinter provides a comprehensive set of modern widgets:

<table>
  <tr>
    <td align="center">🪟<br><strong>BTk</strong><br>Main Window</td>
    <td align="center">🔳<br><strong>BTkButton</strong><br>Modern Buttons</td>
    <td align="center">🖼️<br><strong>BTkFrame</strong><br>Containers</td>
    <td align="center">🏷️<br><strong>BTkLabel</strong><br>Text Display</td>
  </tr>
  <tr>
    <td align="center">📝<br><strong>BTkEntry</strong><br>Input Fields</td>
    <td align="center">💬<br><strong>BTkDialog</strong><br>Message Boxes</td>
    <td align="center">🎨<br><strong>BTkColorPicker</strong><br>Color Selection</td>
    <td align="center">☑️<br><strong>BTkCheckBox</strong><br>Checkboxes</td>
  </tr>
  <tr>
    <td align="center">📊<br><strong>BTkProgressBar</strong><br>Progress Indicators</td>
    <td align="center">🧭<br><strong>BTkNavBar</strong><br>Navigation</td>
    <td align="center">🎚️<br><strong>BTkSlider</strong><br>Range Input</td>
    <td align="center">🖌️<br><strong>BTkCanvas</strong><br>Drawing Surface</td>
  </tr>
</table>

> 📖 **Full Component Reference:** [Component Documentation](https://velyzo.github.io/BetterTkinterDocs/components/)

---

## 📚 **Documentation & Resources**

### 🌐 **Complete Documentation Website**
**[📖 velyzo.github.io/BetterTkinterDocs](https://velyzo.github.io/BetterTkinterDocs/)**

Our comprehensive documentation includes:
- 📘 **Getting Started Guide** - Step-by-step tutorials
- 🧩 **Component Reference** - Detailed API documentation  
- 💡 **Examples Collection** - Real-world code samples
- 🎨 **Theming Guide** - Customization and styling
- 🚀 **Deployment Guide** - Packaging and distribution

### 📁 **Local Documentation**
- [`docs/`](docs/) - Complete local documentation
- [`docs/guides/`](docs/guides/) - Installation, quick start, deployment
- [`docs/components/`](docs/components/) - Individual component docs
- [`docs/examples/`](docs/examples/) - Code examples and tutorials
- [`docs/api/`](docs/api/) - Full API reference

---

## 🤝 **Community & Support**

<div align="center">

[![GitHub Discussions](https://img.shields.io/badge/GitHub-Discussions-blue?style=for-the-badge&logo=github)](https://github.com/Velyzo/BetterTkinter/discussions)
[![Issues](https://img.shields.io/badge/Report-Issues-red?style=for-the-badge&logo=github)](https://github.com/Velyzo/BetterTkinter/issues)
[![Documentation](https://img.shields.io/badge/Read-Docs-green?style=for-the-badge&logo=readthedocs)](https://velyzo.github.io/BetterTkinterDocs/)

</div>

### 💪 **Contributing**
We welcome contributions! Here's how you can help:

- 🐛 **Report bugs** and request features
- 📝 **Improve documentation** and examples  
- 🔧 **Submit pull requests** with enhancements
- 💬 **Help others** in discussions
- ⭐ **Star the repository** to show your support

See our [Contributing Guide](docs/CONTRIBUTING.md) for detailed guidelines.

---

## 🏆 **Showcase**

**BetterTkinter** powers a variety of applications:
- 🖥️ **Desktop Applications** - Business tools, utilities, games
- 🔧 **Development Tools** - IDEs, file managers, system monitors  
- 🎨 **Creative Software** - Image editors, drawing apps, design tools
- 📊 **Data Applications** - Dashboards, analytics, visualization tools

> 📸 **Share Your Creation:** Built something amazing? [Share it with us](https://github.com/Velyzo/BetterTkinter/discussions)!

---

## 📜 **License**

BetterTkinter is released under the **MIT License**. See [`LICENSE`](LICENSE) for details.

```
MIT License - Feel free to use BetterTkinter in personal and commercial projects!
```

---

## ⭐ **Star History**

<div align="center">
  
[![Star History Chart](https://api.star-history.com/svg?repos=Velyzo/BetterTkinter&type=Date)](https://star-history.com/#Velyzo/BetterTkinter&Date)

</div>

---

<div align="center">

### 🚀 **Ready to Build Something Amazing?**

**[📖 Read the Docs](https://velyzo.github.io/BetterTkinterDocs/)** • **[🎮 Try the Demo](demo.py)** • **[⭐ Star the Repo](https://github.com/Velyzo/BetterTkinter)**

<br>

**Made with ❤️ by the BetterTkinter Team**

[![Follow on GitHub](https://img.shields.io/github/followers/Velyzo?style=social)](https://github.com/Velyzo)

</div>
