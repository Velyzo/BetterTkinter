# BetterTkinter

[![License](https://img.shields.io/badge/License-MIT-blue)](https://github.com/Velyzo/BetterTkinter#license)  [![PyPi](https://img.shields.io/badge/PyPi%20Link-FFFF00)](https://pypi.org/project/BetterTkinter/)  [![Downloads](https://static.pepy.tech/badge/bettertkinter)](https://pepy.tech/project/BetterTkinter)

**BetterTkinter** is a modern, feature-rich UI toolkit for Python, built on top of Tkinter. It provides beautiful, customizable widgets, advanced utilities, and easy theming for rapid desktop app development.

## Installation

```bash
pip install BetterTkinter
```

## Features
- Modern window class (`BTk`)
- Beautiful rounded buttons (`BTkButton`)
- Custom frames with rounded corners (`BTkFrame`)
- Stylish labels (`BTkLabel`)
- Enhanced entry fields (`BTkEntry`)
- Dialog utilities (`BTkDialog`)
- Tooltips (`BTkTooltip`)
- Theme manager (`BTkTheme`)
- Demo app (`BTkDemo`)
- Extensible and easy to use

## Quick Start

```python
from bettertkinter import BTk, BTkButton, BTkFrame, BTkLabel, BTkEntry, BTkDialog, BTkTooltip, BTkTheme

app = BTk(title="My App")
BTkTheme.apply(app, "light")

frame = BTkFrame(app, radius=20, width=300, height=150, color="#e0e0e0", border=True, border_color="#0078D7", border_thick=3)
frame.pack(pady=20)

label = BTkLabel(frame, text="Hello, BetterTkinter!", font=("Helvetica", 14, "bold"), fg="#0078D7")
label.pack(pady=10)

entry = BTkEntry(frame)
entry.pack(pady=10)
BTkTooltip(entry, "Type here!")

button = BTkButton(frame, text="Show Dialog", command=lambda: BTkDialog.info("Info", f"You typed: {entry.get()}"))
button.pack(pady=10)

app.geometry("400x300")
app.mainloop()
```

## Demo
Run the demo app:
```bash
python -m bettertkinter.BTkDemo
```

## Documentation
Full docs: [https://Velyzo.github.io/BetterTkinterDocs/](https://Velyzo.github.io/BetterTkinterDocs/)

## Contributing
Pull requests and suggestions are welcome! See [CONTRIBUTING.md](https://github.com/Velyzo/BetterTkinter/blob/master/CONTRIBUTING.md).

## License
MIT
