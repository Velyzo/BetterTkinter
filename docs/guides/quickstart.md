# 🏁 Quick Start Guide

Get up and running with BetterTkinter in minutes! This guide will walk you through creating your first beautiful GUI application.

## 📚 What You'll Learn

- Basic BetterTkinter concepts
- Creating your first window
- Adding and styling components
- Handling user interactions
- Best practices

## 🚀 Your First BetterTkinter App

### Step 1: Create a Basic Window

```python
from bettertkinter import BTk

# Create the main window
app = BTk()
app.title("My First BetterTkinter App")
app.geometry("400x300")

# Run the application
app.mainloop()
```

**Result:** A clean, modern window with the title "My First BetterTkinter App"

### Step 2: Add Some Content

```python
from bettertkinter import BTk, BTkLabel

app = BTk()
app.title("Hello BetterTkinter")
app.geometry("400x300")

# Add a welcome label
welcome_label = BTkLabel(
    app, 
    text="Welcome to BetterTkinter!",
    font_size=18,
    text_color="#2E8B57"
)
welcome_label.pack(pady=50)

app.mainloop()
```

### Step 3: Add Interactive Elements

```python
from bettertkinter import BTk, BTkLabel, BTkButton

def on_button_click():
    label.configure(text="Hello from BetterTkinter! 👋")

app = BTk()
app.title("Interactive App")
app.geometry("400x300")

# Label that will change
label = BTkLabel(app, text="Click the button below!", font_size=14)
label.pack(pady=30)

# Interactive button
button = BTkButton(
    app, 
    text="Click Me!",
    command=on_button_click,
    style="primary"
)
button.pack(pady=20)

app.mainloop()
```

### Step 4: Complete Example with Multiple Components

```python
from bettertkinter import (
    BTk, BTkLabel, BTkButton, BTkEntry, 
    BTkFrame, BTkCheckBox
)

class GreeterApp(BTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("BetterTkinter Greeter")
        self.geometry("500x400")
        self.set_theme("dark")  # Try "light" too!
        
        # Create interface
        self.create_widgets()
    
    def create_widgets(self):
        # Main container
        main_frame = BTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title = BTkLabel(
            main_frame,
            text="BetterTkinter Greeter",
            font_size=20,
            text_color="#4A90E2"
        )
        title.pack(pady=20)
        
        # Name input
        name_label = BTkLabel(main_frame, text="Enter your name:")
        name_label.pack(pady=(10, 5))
        
        self.name_entry = BTkEntry(
            main_frame,
            placeholder="Your name here..."
        )
        self.name_entry.pack(pady=5, padx=50, fill="x")
        
        # Checkbox option
        self.formal_check = BTkCheckBox(
            main_frame,
            text="Use formal greeting"
        )
        self.formal_check.pack(pady=10)
        
        # Greet button
        greet_btn = BTkButton(
            main_frame,
            text="Greet Me!",
            command=self.greet_user,
            style="primary"
        )
        greet_btn.pack(pady=20)
        
        # Result label
        self.result_label = BTkLabel(
            main_frame,
            text="",
            font_size=14,
            text_color="#2E8B57"
        )
        self.result_label.pack(pady=10)
    
    def greet_user(self):
        name = self.name_entry.get().strip()
        
        if not name:
            self.result_label.configure(
                text="Please enter your name! 😊",
                text_color="#E74C3C"
            )
            return
        
        # Create greeting
        if self.formal_check.get():
            greeting = f"Good day, {name}! 🎩"
        else:
            greeting = f"Hey there, {name}! 👋"
        
        self.result_label.configure(
            text=greeting,
            text_color="#2E8B57"
        )

# Run the app
if __name__ == "__main__":
    app = GreeterApp()
    app.mainloop()
```

## 🎨 Understanding BetterTkinter Concepts

### 1. Components Hierarchy
```
BTk (Main Window)
├── BTkFrame (Container)
│   ├── BTkLabel (Text Display)
│   ├── BTkButton (Interactive Button)
│   ├── BTkEntry (Text Input)
│   └── BTkCheckBox (Toggle Option)
└── BTkDialog (Popup Windows)
```

### 2. Layout Management
BetterTkinter uses tkinter's layout managers:

```python
# Pack layout (simple, vertical/horizontal)
component.pack(pady=10, padx=20, fill="x")

# Grid layout (table-like)
component.grid(row=0, column=1, sticky="ew")

# Place layout (absolute positioning)
component.place(x=100, y=50, width=200, height=30)
```

### 3. Styling Options

```python
# Built-in styles
button = BTkButton(app, text="Primary", style="primary")
button = BTkButton(app, text="Secondary", style="secondary")
button = BTkButton(app, text="Success", style="success")
button = BTkButton(app, text="Warning", style="warning")
button = BTkButton(app, text="Danger", style="danger")

# Custom colors
label = BTkLabel(
    app, 
    text="Custom Style",
    text_color="#FF6B6B",
    bg_color="#4ECDC4",
    font_size=16
)
```

### 4. Event Handling

```python
def handle_click():
    print("Button clicked!")

def handle_entry_change(event):
    print(f"Entry value: {entry.get()}")

# Button click
button = BTkButton(app, text="Click", command=handle_click)

# Entry change
entry = BTkEntry(app)
entry.bind("<KeyRelease>", handle_entry_change)

# Window events
app.protocol("WM_DELETE_WINDOW", on_window_close)
```

## 📱 Common Patterns

### Pattern 1: Input Form
```python
class InputForm(BTk):
    def __init__(self):
        super().__init__()
        self.title("Input Form")
        self.geometry("400x500")
        
        # Form fields
        self.create_form()
    
    def create_form(self):
        # Title
        BTkLabel(self, text="User Registration", font_size=18).pack(pady=20)
        
        # Name field
        BTkLabel(self, text="Name:").pack(anchor="w", padx=50)
        self.name_entry = BTkEntry(self)
        self.name_entry.pack(fill="x", padx=50, pady=5)
        
        # Email field
        BTkLabel(self, text="Email:").pack(anchor="w", padx=50, pady=(10,0))
        self.email_entry = BTkEntry(self, placeholder="user@example.com")
        self.email_entry.pack(fill="x", padx=50, pady=5)
        
        # Submit button
        BTkButton(self, text="Submit", command=self.submit, 
                 style="primary").pack(pady=20)
    
    def submit(self):
        from bettertkinter import BTkDialog
        name = self.name_entry.get()
        email = self.email_entry.get()
        BTkDialog.show_info("Success", f"Welcome, {name}!")
```

### Pattern 2: Menu Application
```python
class MenuApp(BTk):
    def __init__(self):
        super().__init__()
        self.title("Menu Application")
        self.geometry("600x400")
        
        self.create_menu_layout()
    
    def create_menu_layout(self):
        # Sidebar
        sidebar = BTkFrame(self, width=150)
        sidebar.pack(side="left", fill="y", padx=(10,5), pady=10)
        
        # Menu buttons
        buttons = [
            ("Home", self.show_home),
            ("Profile", self.show_profile),
            ("Settings", self.show_settings),
            ("About", self.show_about)
        ]
        
        for text, command in buttons:
            BTkButton(sidebar, text=text, command=command, 
                     style="secondary").pack(fill="x", pady=5, padx=10)
        
        # Content area
        self.content_frame = BTkFrame(self)
        self.content_frame.pack(side="right", fill="both", expand=True, 
                               padx=(5,10), pady=10)
        
        # Show home by default
        self.show_home()
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def show_home(self):
        self.clear_content()
        BTkLabel(self.content_frame, text="Welcome Home!", 
                font_size=20).pack(pady=50)
    
    def show_profile(self):
        self.clear_content()
        BTkLabel(self.content_frame, text="User Profile", 
                font_size=18).pack(pady=20)
        BTkLabel(self.content_frame, text="Name: John Doe").pack()
        BTkLabel(self.content_frame, text="Email: john@example.com").pack()
    
    def show_settings(self):
        self.clear_content()
        BTkLabel(self.content_frame, text="Settings", 
                font_size=18).pack(pady=20)
        BTkCheckBox(self.content_frame, text="Dark Mode").pack(pady=5)
        BTkCheckBox(self.content_frame, text="Notifications").pack(pady=5)
    
    def show_about(self):
        self.clear_content()
        BTkLabel(self.content_frame, text="About This App", 
                font_size=18).pack(pady=20)
        BTkLabel(self.content_frame, 
                text="Built with BetterTkinter v2.0").pack()
```

## 🎯 Best Practices

### 1. **Use Classes for Complex Apps**
```python
# Good ✅
class MyApp(BTk):
    def __init__(self):
        super().__init__()
        self.setup_ui()

# Avoid for complex apps ❌
app = BTk()
# ... lots of global variables and functions
```

### 2. **Organize with Frames**
```python
# Create logical sections
header_frame = BTkFrame(app)
content_frame = BTkFrame(app)
footer_frame = BTkFrame(app)
```

### 3. **Handle Errors Gracefully**
```python
def safe_operation():
    try:
        # Your code here
        pass
    except Exception as e:
        from bettertkinter import BTkDialog
        BTkDialog.show_error("Error", f"Something went wrong: {e}")
```

### 4. **Use Meaningful Variable Names**
```python
# Good ✅
username_entry = BTkEntry(app)
submit_button = BTkButton(app, text="Submit")

# Avoid ❌
e1 = BTkEntry(app)
b1 = BTkButton(app, text="Submit")
```

## 🔧 Customization Tips

### Themes
```python
# Set theme for entire app
app.set_theme("dark")  # or "light"

# Custom theme colors
app.configure_theme({
    'primary_color': '#3498DB',
    'secondary_color': '#95A5A6',
    'success_color': '#2ECC71',
    'warning_color': '#F39C12',
    'danger_color': '#E74C3C'
})
```

### Icons and Images
```python
# Add icons to buttons
button = BTkButton(app, text="Save", icon="💾")

# Custom images (requires PIL)
from PIL import Image
button = BTkButton(app, text="Custom", image=Image.open("icon.png"))
```

## 🚀 Next Steps

Now that you've learned the basics:

1. **Explore Components**: Check out the [component documentation](../components/)
2. **Advanced Features**: Learn about [theming](theming.md) and [styling](advanced-styling.md)
3. **Examples**: See more [complete examples](../examples/)
4. **Deploy**: Learn how to [package your app](deployment.md)

## 💡 Quick Reference

### Essential Imports
```python
from bettertkinter import (
    BTk,           # Main window
    BTkLabel,      # Text display
    BTkButton,     # Clickable button
    BTkEntry,      # Text input
    BTkFrame,      # Container
    BTkCheckBox,   # Checkbox
    BTkDialog,     # Popup dialogs
)
```

### Common Methods
```python
# Window configuration
app.title("Window Title")
app.geometry("800x600")
app.set_theme("dark")

# Component configuration
component.pack(pady=10)
component.configure(text="New Text")
value = component.get()

# Event binding
component.bind("<Button-1>", callback)
```

---

**Congratulations! You're ready to build amazing GUIs with BetterTkinter!** 🎉

Need help? Check our [FAQ](faq.md) or [join the community](https://github.com/Velyzo/BetterTkinter/discussions)!
