# 🖼️ BTk - Main Window

The `BTk` class is the foundation of every BetterTkinter application. It creates the main window and provides the container for all other components.

## 📋 Overview

`BTk` extends tkinter's `Tk` class with modern styling, theming support, and enhanced functionality while maintaining full compatibility with standard tkinter methods.

## 🚀 Basic Usage

```python
from bettertkinter import BTk

# Create main window
app = BTk()
app.title("My Application")
app.geometry("800x600")
app.mainloop()
```

## 🔧 Constructor

```python
BTk(theme="light", **kwargs)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `theme` | str | "light" | Initial theme ("light" or "dark") |
| `**kwargs` | dict | {} | Additional tkinter.Tk parameters |

## 🎨 Methods

### Window Configuration

#### `set_theme(theme)`
Sets the application theme.

```python
app.set_theme("dark")   # Dark theme
app.set_theme("light")  # Light theme
```

**Parameters:**
- `theme` (str): Theme name ("light" or "dark")

#### `configure_theme(theme_dict)`
Customizes theme colors.

```python
app.configure_theme({
    'primary_color': '#3498DB',
    'secondary_color': '#95A5A6',
    'bg_color': '#2C3E50',
    'text_color': '#ECF0F1'
})
```

**Parameters:**
- `theme_dict` (dict): Dictionary of theme properties

#### `set_icon(icon_path)`
Sets the window icon.

```python
app.set_icon("assets/icon.png")
app.set_icon("assets/icon.ico")  # Windows ICO format
```

**Parameters:**
- `icon_path` (str): Path to icon file (PNG, ICO, GIF)

### Window Management

#### `center_window(width=None, height=None)`
Centers the window on screen.

```python
app.center_window()           # Center current size
app.center_window(800, 600)   # Center with specific size
```

**Parameters:**
- `width` (int, optional): Window width
- `height` (int, optional): Window height

#### `set_resizable(width=True, height=True)`
Controls window resizing.

```python
app.set_resizable(False, False)  # Fixed size
app.set_resizable(True, False)   # Horizontally resizable only
```

**Parameters:**
- `width` (bool): Allow horizontal resizing
- `height` (bool): Allow vertical resizing

#### `set_minimum_size(width, height)`
Sets minimum window dimensions.

```python
app.set_minimum_size(400, 300)
```

**Parameters:**
- `width` (int): Minimum width in pixels
- `height` (int): Minimum height in pixels

#### `set_maximum_size(width, height)`
Sets maximum window dimensions.

```python
app.set_maximum_size(1920, 1080)
```

**Parameters:**
- `width` (int): Maximum width in pixels
- `height` (int): Maximum height in pixels

### State Management

#### `get_theme()`
Returns the current theme.

```python
current_theme = app.get_theme()  # Returns "light" or "dark"
```

**Returns:**
- `str`: Current theme name

#### `get_window_info()`
Returns window information.

```python
info = app.get_window_info()
# Returns: {'width': 800, 'height': 600, 'x': 100, 'y': 50}
```

**Returns:**
- `dict`: Window dimensions and position

#### `save_state()`
Saves current window state.

```python
state = app.save_state()
# Save to file or database
```

**Returns:**
- `dict`: Serializable window state

#### `restore_state(state)`
Restores window state.

```python
app.restore_state(saved_state)
```

**Parameters:**
- `state` (dict): Previously saved state

## 🎯 Properties

### Theme Properties

| Property | Type | Description |
|----------|------|-------------|
| `theme` | str | Current theme name |
| `theme_colors` | dict | Current theme color palette |
| `is_dark_theme` | bool | True if using dark theme |

### Window Properties

| Property | Type | Description |
|----------|------|-------------|
| `window_width` | int | Current window width |
| `window_height` | int | Current window height |
| `window_x` | int | Window X position |
| `window_y` | int | Window Y position |

## 📱 Examples

### Basic Application

```python
from bettertkinter import BTk, BTkLabel, BTkButton

class MyApp(BTk):
    def __init__(self):
        super().__init__(theme="dark")
        
        # Configure window
        self.title("My BetterTkinter App")
        self.geometry("600x400")
        self.center_window()
        self.set_resizable(True, False)
        
        # Create content
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = BTkLabel(
            self, 
            text="Welcome to My App",
            font_size=20,
            text_color="#4A90E2"
        )
        title.pack(pady=30)
        
        # Action button
        button = BTkButton(
            self,
            text="Get Started",
            command=self.on_start,
            style="primary"
        )
        button.pack(pady=20)
    
    def on_start(self):
        from bettertkinter import BTkDialog
        BTkDialog.show_info("Welcome", "Let's build something amazing!")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
```

### Theme Switching

```python
from bettertkinter import BTk, BTkButton, BTkFrame

class ThemeDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Theme Demo")
        self.geometry("400x300")
        self.center_window()
        
        self.create_ui()
    
    def create_ui(self):
        # Control frame
        control_frame = BTkFrame(self)
        control_frame.pack(pady=20, padx=20, fill="x")
        
        # Theme buttons
        BTkButton(
            control_frame,
            text="Light Theme",
            command=lambda: self.set_theme("light"),
            style="secondary"
        ).pack(side="left", padx=10)
        
        BTkButton(
            control_frame,
            text="Dark Theme", 
            command=lambda: self.set_theme("dark"),
            style="secondary"
        ).pack(side="left", padx=10)
        
        # Custom theme button
        BTkButton(
            control_frame,
            text="Custom Theme",
            command=self.apply_custom_theme,
            style="primary"
        ).pack(side="left", padx=10)
    
    def apply_custom_theme(self):
        self.configure_theme({
            'primary_color': '#E74C3C',
            'secondary_color': '#34495E',
            'success_color': '#27AE60',
            'bg_color': '#2C3E50',
            'text_color': '#ECF0F1'
        })

app = ThemeDemo()
app.mainloop()
```

### Advanced Window Management

```python
from bettertkinter import BTk, BTkButton, BTkLabel
import json

class AdvancedWindow(BTk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Window Demo")
        
        # Try to restore previous state
        self.restore_previous_state()
        
        # Setup close handler
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.create_ui()
    
    def create_ui(self):
        # Window info display
        self.info_label = BTkLabel(self, text="", font_size=12)
        self.info_label.pack(pady=20)
        
        # Update info
        self.update_window_info()
        
        # Control buttons
        button_frame = BTkFrame(self)
        button_frame.pack(pady=20)
        
        BTkButton(
            button_frame,
            text="Center Window",
            command=self.center_window
        ).pack(side="left", padx=5)
        
        BTkButton(
            button_frame,
            text="Minimize",
            command=self.iconify
        ).pack(side="left", padx=5)
        
        BTkButton(
            button_frame,
            text="Toggle Fullscreen",
            command=self.toggle_fullscreen
        ).pack(side="left", padx=5)
        
        # Bind events
        self.bind("<Configure>", self.on_window_configure)
    
    def update_window_info(self):
        info = self.get_window_info()
        text = f"Size: {info['width']}x{info['height']} | Position: ({info['x']}, {info['y']})"
        self.info_label.configure(text=text)
    
    def on_window_configure(self, event):
        if event.widget == self:
            self.update_window_info()
    
    def toggle_fullscreen(self):
        current = self.attributes('-fullscreen')
        self.attributes('-fullscreen', not current)
    
    def restore_previous_state(self):
        try:
            with open('window_state.json', 'r') as f:
                state = json.load(f)
                self.restore_state(state)
        except FileNotFoundError:
            # Default size and center
            self.geometry("500x350")
            self.center_window()
    
    def on_closing(self):
        # Save state before closing
        try:
            state = self.save_state()
            with open('window_state.json', 'w') as f:
                json.dump(state, f)
        except Exception as e:
            print(f"Failed to save state: {e}")
        
        self.destroy()

app = AdvancedWindow()
app.mainloop()
```

## 🔧 Theming System

### Built-in Themes

#### Light Theme
```python
light_theme = {
    'primary_color': '#007BFF',
    'secondary_color': '#6C757D',
    'success_color': '#28A745',
    'warning_color': '#FFC107',
    'danger_color': '#DC3545',
    'bg_color': '#FFFFFF',
    'surface_color': '#F8F9FA',
    'text_color': '#212529',
    'border_color': '#DEE2E6'
}
```

#### Dark Theme
```python
dark_theme = {
    'primary_color': '#0D6EFD',
    'secondary_color': '#6C757D',
    'success_color': '#198754',
    'warning_color': '#FFC107',
    'danger_color': '#DC3545',
    'bg_color': '#212529',
    'surface_color': '#343A40',
    'text_color': '#F8F9FA',
    'border_color': '#495057'
}
```

### Custom Theme Creation

```python
custom_theme = {
    # Brand colors
    'primary_color': '#FF6B6B',
    'secondary_color': '#4ECDC4',
    'accent_color': '#45B7D1',
    
    # Status colors
    'success_color': '#96CEB4',
    'warning_color': '#FFEAA7',
    'danger_color': '#FF7675',
    'info_color': '#74B9FF',
    
    # Surface colors
    'bg_color': '#2D3436',
    'surface_color': '#636E72',
    'card_color': '#74B9FF',
    
    # Text colors
    'text_color': '#DDD',
    'text_secondary': '#AAA',
    'text_disabled': '#666',
    
    # Border colors
    'border_color': '#555',
    'border_active': '#FFF',
    'border_disabled': '#444'
}

app.configure_theme(custom_theme)
```

## 🐛 Common Issues

### Issue: Window not centering properly
```python
# Solution: Call after geometry is set
app.geometry("800x600")
app.update_idletasks()  # Ensure geometry is applied
app.center_window()
```

### Issue: Theme not applying to all components
```python
# Solution: Set theme before creating components
app = BTk()
app.set_theme("dark")  # Set theme first
# Then create components...
```

### Issue: Icon not displaying
```python
# Ensure icon file exists and is accessible
import os
icon_path = "assets/icon.png"
if os.path.exists(icon_path):
    app.set_icon(icon_path)
else:
    print(f"Icon not found: {icon_path}")
```

## 🎯 Best Practices

1. **Set theme early**: Configure theme before creating components
2. **Use classes**: Inherit from BTk for complex applications
3. **Handle window events**: Implement proper close handlers
4. **Center responsively**: Call center_window() after setting geometry
5. **Save user preferences**: Store theme and window state
6. **Test on different screens**: Ensure your app works on various resolutions

## 🔗 Related Components

- [BTkFrame](BTkFrame.md) - Layout containers
- [BTkDialog](BTkDialog.md) - Popup windows
- [BTkSystemTray](BTkSystemTray.md) - System tray integration

---

**Ready to create amazing main windows with BTk!** 🎉
