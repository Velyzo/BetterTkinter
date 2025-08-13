# 🔘 BTkButton - Interactive Button

The `BTkButton` component provides modern, stylish buttons with various styles, hover effects, and customization options.

## 📋 Overview

`BTkButton` is a modern replacement for tkinter's Button widget, featuring:
- Built-in styling system with predefined styles
- Smooth hover and click animations
- Icon support
- Rounded corners and modern aesthetics
- Fully customizable appearance

## 🚀 Basic Usage

```python
from bettertkinter import BTk, BTkButton

app = BTk()

# Simple button
button = BTkButton(app, text="Click Me!", command=lambda: print("Clicked!"))
button.pack(pady=10)

app.mainloop()
```

## 🔧 Constructor

```python
BTkButton(parent, text="", command=None, style="default", 
          width=120, height=32, font_size=12, text_color=None,
          bg_color=None, hover_color=None, icon=None, **kwargs)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent` | Widget | Required | Parent container |
| `text` | str | "" | Button text |
| `command` | callable | None | Function to call when clicked |
| `style` | str | "default" | Button style preset |
| `width` | int | 120 | Button width in pixels |
| `height` | int | 32 | Button height in pixels |
| `font_size` | int | 12 | Text font size |
| `text_color` | str | None | Text color (hex) |
| `bg_color` | str | None | Background color (hex) |
| `hover_color` | str | None | Hover state color (hex) |
| `icon` | str/Image | None | Button icon |
| `**kwargs` | dict | {} | Additional tkinter parameters |

## 🎨 Button Styles

### Built-in Styles

```python
# Primary button (blue)
primary_btn = BTkButton(app, text="Primary", style="primary")

# Secondary button (gray)
secondary_btn = BTkButton(app, text="Secondary", style="secondary")

# Success button (green)
success_btn = BTkButton(app, text="Success", style="success")

# Warning button (orange)
warning_btn = BTkButton(app, text="Warning", style="warning")

# Danger button (red)
danger_btn = BTkButton(app, text="Danger", style="danger")

# Default button (neutral)
default_btn = BTkButton(app, text="Default", style="default")
```

### Style Specifications

| Style | Background | Text Color | Hover Color | Use Case |
|-------|------------|------------|-------------|----------|
| `primary` | #007BFF | White | #0056B3 | Main actions |
| `secondary` | #6C757D | White | #545B62 | Secondary actions |
| `success` | #28A745 | White | #1E7E34 | Success/confirm |
| `warning` | #FFC107 | Dark | #E0A800 | Warnings |
| `danger` | #DC3545 | White | #B02A37 | Delete/dangerous |
| `default` | #F8F9FA | Dark | #E2E6EA | Neutral actions |

## 🔧 Methods

### Configuration

#### `configure(option=None, **kwargs)`
Updates button properties.

```python
button.configure(text="New Text")
button.configure(style="primary", width=150)
button.configure(text="Save", bg_color="#28A745")
```

#### `set_style(style)`
Changes the button style.

```python
button.set_style("primary")
button.set_style("danger")
```

**Parameters:**
- `style` (str): Style name

#### `set_text(text)`
Updates button text.

```python
button.set_text("Updated Text")
```

**Parameters:**
- `text` (str): New button text

#### `set_command(command)`
Updates the click handler.

```python
def new_action():
    print("New action!")

button.set_command(new_action)
```

**Parameters:**
- `command` (callable): New click handler function

### State Management

#### `set_enabled(enabled)`
Enables or disables the button.

```python
button.set_enabled(False)  # Disable button
button.set_enabled(True)   # Enable button
```

**Parameters:**
- `enabled` (bool): Whether button is enabled

#### `is_enabled()`
Returns button enabled state.

```python
if button.is_enabled():
    print("Button is enabled")
```

**Returns:**
- `bool`: True if button is enabled

#### `set_loading(loading, text="Loading...")`
Shows loading state.

```python
button.set_loading(True, "Processing...")
button.set_loading(False)  # Stop loading
```

**Parameters:**
- `loading` (bool): Whether to show loading state
- `text` (str): Loading text to display

### Visual Effects

#### `animate_click()`
Triggers click animation programmatically.

```python
button.animate_click()
```

#### `set_hover_effect(enabled)`
Enables or disables hover effects.

```python
button.set_hover_effect(False)  # Disable hover
```

**Parameters:**
- `enabled` (bool): Whether hover effects are enabled

## 🎯 Properties

### Text Properties

| Property | Type | Description |
|----------|------|-------------|
| `text` | str | Current button text |
| `font_size` | int | Text font size |
| `text_color` | str | Text color |

### Appearance Properties

| Property | Type | Description |
|----------|------|-------------|
| `style` | str | Current style name |
| `bg_color` | str | Background color |
| `hover_color` | str | Hover state color |
| `width` | int | Button width |
| `height` | int | Button height |

### State Properties

| Property | Type | Description |
|----------|------|-------------|
| `enabled` | bool | Whether button is enabled |
| `loading` | bool | Whether in loading state |
| `pressed` | bool | Whether currently pressed |

## 📱 Examples

### Basic Buttons

```python
from bettertkinter import BTk, BTkButton, BTkFrame

class ButtonDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Button Demo")
        self.geometry("600x400")
        
        self.create_button_demo()
    
    def create_button_demo(self):
        # Main container
        main_frame = BTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        from bettertkinter import BTkLabel
        BTkLabel(main_frame, text="Button Styles Demo", 
                font_size=18).pack(pady=20)
        
        # Button styles
        styles = ["primary", "secondary", "success", "warning", "danger"]
        
        for style in styles:
            btn = BTkButton(
                main_frame,
                text=f"{style.title()} Button",
                style=style,
                command=lambda s=style: self.on_button_click(s)
            )
            btn.pack(pady=5)
    
    def on_button_click(self, style):
        from bettertkinter import BTkDialog
        BTkDialog.show_info("Clicked", f"You clicked the {style} button!")

app = ButtonDemo()
app.mainloop()
```

### Custom Styled Buttons

```python
from bettertkinter import BTk, BTkButton, BTkFrame

class CustomButtonDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Button Demo")
        self.geometry("500x400")
        
        self.create_custom_buttons()
    
    def create_custom_buttons(self):
        container = BTkFrame(self)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Custom color button
        custom_btn = BTkButton(
            container,
            text="Custom Colors",
            bg_color="#FF6B6B",
            text_color="white",
            hover_color="#FF5252",
            width=200,
            height=40,
            font_size=14,
            command=lambda: print("Custom button clicked!")
        )
        custom_btn.pack(pady=10)
        
        # Large button
        large_btn = BTkButton(
            container,
            text="Large Button",
            style="primary",
            width=300,
            height=50,
            font_size=16
        )
        large_btn.pack(pady=10)
        
        # Small button
        small_btn = BTkButton(
            container,
            text="Small",
            style="secondary",
            width=80,
            height=24,
            font_size=10
        )
        small_btn.pack(pady=10)
        
        # Icon button (if you have emoji or Unicode icons)
        icon_btn = BTkButton(
            container,
            text="💾 Save",
            style="success",
            width=150
        )
        icon_btn.pack(pady=10)

app = CustomButtonDemo()
app.mainloop()
```

### Interactive Button States

```python
from bettertkinter import BTk, BTkButton, BTkFrame, BTkLabel
import threading
import time

class InteractiveButtonDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Interactive Button Demo")
        self.geometry("400x300")
        
        self.create_interactive_demo()
    
    def create_interactive_demo(self):
        container = BTkFrame(self)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Status label
        self.status_label = BTkLabel(container, text="Ready", font_size=12)
        self.status_label.pack(pady=10)
        
        # Toggle button
        self.toggle_btn = BTkButton(
            container,
            text="Enable",
            style="success",
            command=self.toggle_button
        )
        self.toggle_btn.pack(pady=5)
        
        # Target button (to be toggled)
        self.target_btn = BTkButton(
            container,
            text="Target Button",
            style="primary",
            command=lambda: self.status_label.configure(text="Target clicked!")
        )
        self.target_btn.pack(pady=5)
        self.target_btn.set_enabled(False)
        
        # Loading button
        self.loading_btn = BTkButton(
            container,
            text="Start Process",
            style="warning",
            command=self.start_loading
        )
        self.loading_btn.pack(pady=5)
        
        # Style changer
        self.style_btn = BTkButton(
            container,
            text="Change Style",
            style="secondary",
            command=self.cycle_style
        )
        self.style_btn.pack(pady=5)
        self.current_style_index = 0
        self.styles = ["primary", "secondary", "success", "warning", "danger"]
    
    def toggle_button(self):
        is_enabled = self.target_btn.is_enabled()
        self.target_btn.set_enabled(not is_enabled)
        
        if is_enabled:
            self.toggle_btn.configure(text="Enable", style="success")
            self.status_label.configure(text="Target button disabled")
        else:
            self.toggle_btn.configure(text="Disable", style="danger")
            self.status_label.configure(text="Target button enabled")
    
    def start_loading(self):
        self.loading_btn.set_loading(True, "Processing...")
        self.status_label.configure(text="Processing started...")
        
        # Simulate work in background thread
        def background_work():
            time.sleep(3)  # Simulate 3-second process
            
            # Update UI in main thread
            self.after(0, self.finish_loading)
        
        thread = threading.Thread(target=background_work, daemon=True)
        thread.start()
    
    def finish_loading(self):
        self.loading_btn.set_loading(False)
        self.status_label.configure(text="Process completed!")
    
    def cycle_style(self):
        style = self.styles[self.current_style_index]
        self.style_btn.set_style(style)
        self.style_btn.set_text(f"Style: {style.title()}")
        
        self.current_style_index = (self.current_style_index + 1) % len(self.styles)

app = InteractiveButtonDemo()
app.mainloop()
```

### Form with Validation

```python
from bettertkinter import BTk, BTkButton, BTkEntry, BTkLabel, BTkFrame

class FormDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Form Demo")
        self.geometry("400x350")
        
        self.create_form()
    
    def create_form(self):
        # Main container
        form_frame = BTkFrame(self)
        form_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Title
        BTkLabel(form_frame, text="User Registration", 
                font_size=16).pack(pady=(0, 20))
        
        # Name field
        BTkLabel(form_frame, text="Name:", font_size=12).pack(anchor="w")
        self.name_entry = BTkEntry(form_frame, placeholder="Enter your name")
        self.name_entry.pack(fill="x", pady=(5, 15))
        
        # Email field
        BTkLabel(form_frame, text="Email:", font_size=12).pack(anchor="w")
        self.email_entry = BTkEntry(form_frame, placeholder="your@email.com")
        self.email_entry.pack(fill="x", pady=(5, 15))
        
        # Status label
        self.status_label = BTkLabel(form_frame, text="", font_size=10)
        self.status_label.pack(pady=(0, 15))
        
        # Button frame
        btn_frame = BTkFrame(form_frame)
        btn_frame.pack(fill="x", pady=10)
        
        # Clear button
        self.clear_btn = BTkButton(
            btn_frame,
            text="Clear",
            style="secondary",
            command=self.clear_form
        )
        self.clear_btn.pack(side="left", padx=(0, 10))
        
        # Submit button
        self.submit_btn = BTkButton(
            btn_frame,
            text="Submit",
            style="primary",
            command=self.submit_form
        )
        self.submit_btn.pack(side="left")
        
        # Bind entry events for validation
        self.name_entry.bind("<KeyRelease>", self.validate_form)
        self.email_entry.bind("<KeyRelease>", self.validate_form)
        
        # Initial validation
        self.validate_form()
    
    def validate_form(self, event=None):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        
        # Simple validation
        is_valid = bool(name and email and "@" in email)
        
        # Update submit button state
        self.submit_btn.set_enabled(is_valid)
        
        # Update status
        if not name and not email:
            self.status_label.configure(text="Please fill in the form")
        elif not name:
            self.status_label.configure(text="Name is required")
        elif not email:
            self.status_label.configure(text="Email is required")
        elif "@" not in email:
            self.status_label.configure(text="Please enter a valid email")
        else:
            self.status_label.configure(text="Form is valid ✓")
    
    def clear_form(self):
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.validate_form()
    
    def submit_form(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        
        # Show loading
        self.submit_btn.set_loading(True, "Submitting...")
        
        # Simulate API call
        def submit_data():
            time.sleep(2)  # Simulate network delay
            
            # Update UI in main thread
            self.after(0, lambda: self.submission_complete(name))
        
        import threading
        thread = threading.Thread(target=submit_data, daemon=True)
        thread.start()
    
    def submission_complete(self, name):
        self.submit_btn.set_loading(False)
        
        from bettertkinter import BTkDialog
        BTkDialog.show_success("Success", f"Welcome, {name}! Registration completed.")
        
        # Clear form
        self.clear_form()

app = FormDemo()
app.mainloop()
```

## 🔧 Advanced Customization

### Custom Button Class

```python
from bettertkinter import BTkButton

class IconButton(BTkButton):
    """Custom button with icon and text"""
    
    def __init__(self, parent, text="", icon="", **kwargs):
        # Combine icon and text
        display_text = f"{icon} {text}" if icon else text
        super().__init__(parent, text=display_text, **kwargs)
        
        self._icon = icon
        self._text = text
    
    def set_icon(self, icon):
        self._icon = icon
        self.update_display()
    
    def set_text(self, text):
        self._text = text
        self.update_display()
    
    def update_display(self):
        display_text = f"{self._icon} {self._text}" if self._icon else self._text
        super().set_text(display_text)

# Usage
save_btn = IconButton(app, text="Save", icon="💾", style="success")
delete_btn = IconButton(app, text="Delete", icon="🗑️", style="danger")
```

## 🐛 Common Issues

### Issue: Button not responding to clicks
```python
# Ensure command is callable
def my_command():
    print("Button clicked")

button = BTkButton(app, text="Click", command=my_command)  # ✓ Correct
# Not: command="my_command"  # ❌ Wrong - string instead of function
```

### Issue: Button appears too small
```python
# Set explicit dimensions
button = BTkButton(app, text="Long Button Text", width=200, height=40)
```

### Issue: Hover effects not working
```python
# Ensure hover is enabled and colors are different
button = BTkButton(
    app, 
    text="Hover Me",
    bg_color="#007BFF",
    hover_color="#0056B3"  # Must be different from bg_color
)
button.set_hover_effect(True)
```

## 🎯 Best Practices

1. **Use meaningful text**: Button text should clearly indicate the action
2. **Choose appropriate styles**: Use semantic styles (success for save, danger for delete)
3. **Provide feedback**: Show loading states for long operations
4. **Handle disabled states**: Disable buttons when actions aren't available
5. **Consider accessibility**: Ensure sufficient color contrast
6. **Test hover states**: Verify hover effects work on different themes

## 🔗 Related Components

- [BTkFrame](BTkFrame.md) - Button containers
- [BTkDialog](BTkDialog.md) - Buttons in dialogs
- [BTkEntry](BTkEntry.md) - Form buttons with inputs

---

**Ready to create interactive buttons with BTkButton!** 🎉
