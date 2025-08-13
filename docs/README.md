# BetterTkinter Documentation

Welcome to the comprehensive documentation for **BetterTkinter** - a modern, beautiful GUI framework built on top of tkinter.

## 📚 Table of Contents

### Getting Started
- [🚀 Installation & Setup](guides/installation.md)
- [🏁 Quick Start Guide](guides/quickstart.md)
- [🔧 Configuration](guides/configuration.md)
- [🎨 Theming & Styling](guides/theming.md)

### Components Documentation
- [🖼️ BTk (Main Window)](components/BTk.md)
- [🔘 BTkButton](components/BTkButton.md)
- [📦 BTkFrame](components/BTkFrame.md)
- [📝 BTkLabel](components/BTkLabel.md)
- [📄 BTkEntry](components/BTkEntry.md)
- [☑️ BTkCheckBox](components/BTkCheckBox.md)
- [📊 BTkProgressBar](components/BTkProgressBar.md)
- [🧭 BTkNavBar](components/BTkNavBar.md)
- [🎨 BTkColorPicker](components/BTkColorPicker.md)
- [💬 BTkDialog](components/BTkDialog.md)
- [🖱️ BTkSlider](components/BTkSlider.md)
- [🔄 BTkSystemTray](components/BTkSystemTray.md)
- [✏️ BTkTextEditor](components/BTkTextEditor.md)

### API Reference
- [📋 Complete API Reference](api/complete-api.md)
- [🏗️ Component Base Classes](api/base-classes.md)
- [🎛️ Event System](api/events.md)
- [🎨 Style System](api/styling.md)

### Guides & Tutorials
- [🏗️ Building Your First App](guides/first-app.md)
- [🎨 Advanced Styling](guides/advanced-styling.md)
- [🔄 State Management](guides/state-management.md)
- [🚀 Deployment](guides/deployment.md)
- [🐛 Debugging & Troubleshooting](guides/debugging.md)

### Examples
- [📱 Simple Apps](examples/simple-apps.md)
- [🖥️ Complex Applications](examples/complex-apps.md)
- [🎨 Styling Examples](examples/styling-examples.md)
- [🔧 Integration Examples](examples/integration-examples.md)

## 🌟 Features

BetterTkinter provides modern, beautiful GUI components with:

- **🎨 Modern Design**: Beautiful, flat design with customizable themes
- **📱 Responsive**: Adaptive layouts that work on different screen sizes
- **🚀 Performance**: Optimized rendering and event handling
- **🔧 Extensible**: Easy to customize and extend components
- **🖥️ Cross-Platform**: Works on Windows, macOS, and Linux
- **🎯 Easy Integration**: Drop-in replacement for tkinter components

## 🚀 Quick Example

```python
from bettertkinter import BTk, BTkButton, BTkLabel

# Create main window
app = BTk()
app.title("My BetterTkinter App")
app.geometry("400x300")

# Add components
label = BTkLabel(app, text="Welcome to BetterTkinter!", 
                 font_size=16, text_color="#2E8B57")
label.pack(pady=20)

button = BTkButton(app, text="Click Me!", 
                   command=lambda: print("Button clicked!"),
                   style="primary")
button.pack(pady=10)

# Run the app
app.mainloop()
```

## 📦 Installation

Install BetterTkinter using pip:

```bash
pip install bettertkinter
```

Or install from source:

```bash
git clone https://github.com/Velyzo/BetterTkinter.git
cd BetterTkinter
pip install -e .
```

## 🆘 Support

- [❓ FAQ](guides/faq.md)
- [🐛 Issue Tracker](https://github.com/Velyzo/BetterTkinter/issues)
- [💬 Discussions](https://github.com/Velyzo/BetterTkinter/discussions)
- [📧 Contact](mailto:support@bettertkinter.dev)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](../CONTRIBUTING.md) for details.

## 📄 License

BetterTkinter is released under the MIT License. See [LICENSE](../LICENSE) for details.

---

**Happy coding with BetterTkinter!** 🎉
