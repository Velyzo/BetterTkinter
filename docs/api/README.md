# 📚 BetterTkinter API Reference

Complete API documentation for all BetterTkinter components, methods, and properties.

## 🏗️ Core Architecture

### BTk (Main Window)
Base window class inheriting from tkinter.Tk with enhanced theming and functionality.

#### Constructor
```python
BTk(title="BetterTkinter App", geometry="800x600", theme="light", 
    resizable=True, min_size=None, max_size=None, **kwargs)
```

#### Properties
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `title` | str | Window title | "BetterTkinter App" |
| `geometry` | str | Window size and position | "800x600" |
| `theme` | str | Color theme ("light", "dark", "auto") | "light" |
| `resizable` | bool/tuple | Window resizability | True |
| `min_size` | tuple | Minimum window size | None |
| `max_size` | tuple | Maximum window size | None |

#### Methods

##### Configuration Methods
```python
configure_theme(theme_name: str) -> None
set_theme_colors(colors: dict) -> None
get_theme_colors() -> dict
toggle_theme() -> None
apply_theme_to_children() -> None
```

##### Window Management
```python
center_window() -> None
set_always_on_top(state: bool) -> None
minimize_to_tray() -> None
restore_from_tray() -> None
set_icon(icon_path: str) -> None
```

##### State Management
```python
save_window_state() -> dict
restore_window_state(state: dict) -> None
get_window_info() -> dict
```

---

## 🧩 Component APIs

### BTkButton

#### Constructor
```python
BTkButton(parent, text="Button", command=None, style="default",
          width=None, height=None, **kwargs)
```

#### Styles
- `"default"` - Standard button
- `"primary"` - Primary action button  
- `"secondary"` - Secondary button
- `"success"` - Success/confirmation button
- `"warning"` - Warning/caution button
- `"danger"` - Destructive action button

#### Methods
```python
configure(text=None, command=None, state=None, style=None, **kwargs) -> None
invoke() -> None
flash() -> None
set_loading(state: bool, text: str = "Loading...") -> None
bind_hover(enter_callback: callable, leave_callback: callable) -> None
```

#### Events
```python
# Standard tkinter events plus:
"<ButtonClick>"     # Button clicked
"<ButtonHover>"     # Mouse entered
"<ButtonLeave>"     # Mouse left
```

---

### BTkFrame

#### Constructor
```python
BTkFrame(parent, bg_color=None, border_width=0, border_color=None,
         corner_radius=0, **kwargs)
```

#### Methods
```python
configure(bg_color=None, border_width=None, border_color=None,
          corner_radius=None, **kwargs) -> None
add_shadow(offset=(2, 2), blur=5, color="#00000040") -> None
remove_shadow() -> None
set_gradient(start_color: str, end_color: str, direction="vertical") -> None
```

---

### BTkLabel

#### Constructor  
```python
BTkLabel(parent, text="", font_size=12, text_color=None,
         bg_color=None, anchor="w", **kwargs)
```

#### Methods
```python
configure(text=None, font_size=None, text_color=None,
          bg_color=None, **kwargs) -> None
set_text(text: str) -> None
get_text() -> str
animate_text(new_text: str, duration: float = 1.0) -> None
```

---

### BTkEntry

#### Constructor
```python
BTkEntry(parent, placeholder_text="", show_char=None, width=None,
         validate_func=None, **kwargs)
```

#### Methods
```python
get() -> str
set(text: str) -> None
clear() -> None
insert(index: int, text: str) -> None
delete(start: int, end: int = None) -> None
select_all() -> None
set_validation(func: callable) -> None
is_valid() -> bool
set_placeholder(text: str) -> None
```

#### Validation
```python
# Built-in validators
BTkEntry.validate_email(email: str) -> bool
BTkEntry.validate_number(text: str) -> bool  
BTkEntry.validate_phone(phone: str) -> bool
BTkEntry.validate_url(url: str) -> bool
```

---

### BTkCheckBox

#### Constructor
```python
BTkCheckBox(parent, text="", variable=None, command=None,
            style="default", **kwargs)
```

#### Methods
```python
get() -> bool
set(value: bool) -> None
toggle() -> None
select() -> None
deselect() -> None
configure(text=None, variable=None, command=None, **kwargs) -> None
```

---

### BTkProgressBar

#### Constructor
```python
BTkProgressBar(parent, orientation="horizontal", mode="determinate",
               width=None, height=None, **kwargs)
```

#### Methods
```python
set_value(value: float) -> None
get_value() -> float
start(interval: int = 10) -> None
stop() -> None
step(amount: float = 1.0) -> None
configure(mode=None, **kwargs) -> None
```

#### Modes
- `"determinate"` - Shows specific progress percentage
- `"indeterminate"` - Shows activity without specific progress

---

### BTkSlider

#### Constructor
```python
BTkSlider(parent, from_=0, to=100, orientation="horizontal", 
          command=None, variable=None, **kwargs)
```

#### Methods
```python
get() -> float
set(value: float) -> None
configure(from_=None, to=None, command=None, **kwargs) -> None
bind_change(callback: callable) -> None
```

---

### BTkNavBar

#### Constructor
```python
BTkNavBar(parent, items=None, orientation="horizontal", 
          style="default", **kwargs)
```

#### Methods
```python
add_item(text: str, command: callable = None, icon: str = None) -> None
remove_item(index: int) -> None
set_active(index: int) -> None
get_active() -> int
configure_item(index: int, text=None, command=None, icon=None) -> None
```

---

### BTkColorPicker

#### Constructor
```python
BTkColorPicker(parent, initial_color="#FFFFFF", show_alpha=True,
               color_format="hex", **kwargs)
```

#### Methods
```python
get_color(format="hex") -> str/tuple
set_color(color, format="hex") -> None
get_rgb() -> tuple[int, int, int]
get_hex() -> str
bind_color_change(callback: callable) -> None
```

#### Color Formats
- `"hex"` - Hexadecimal string (#RRGGBB)
- `"rgb"` - RGB tuple (r, g, b)
- `"rgba"` - RGBA tuple (r, g, b, a)
- `"hsv"` - HSV tuple (h, s, v)
- `"hsl"` - HSL tuple (h, s, l)

---

### BTkDialog

#### Static Methods
```python
BTkDialog.show_info(title: str, message: str, parent=None) -> None
BTkDialog.show_success(title: str, message: str, parent=None) -> None
BTkDialog.show_warning(title: str, message: str, parent=None) -> None
BTkDialog.show_error(title: str, message: str, parent=None) -> None
BTkDialog.ask_yes_no(title: str, message: str, parent=None) -> str
```

#### Instance Methods
```python
show() -> str
close(result=None) -> None
add_button(text: str, style="default", command=None) -> None
clear_buttons() -> None
set_message(message: str) -> None
```

---

### BTkCanvas

#### Constructor
```python
BTkCanvas(parent, width=None, height=None, bg="white", **kwargs)
```

#### Enhanced Methods
```python
create_rounded_rectangle(x1, y1, x2, y2, radius=10, **kwargs) -> int
create_gradient_rectangle(x1, y1, x2, y2, start_color, end_color) -> int
create_shadow(item_id, offset=(2, 2), blur=5, color="#00000040") -> int
animate_item(item_id, end_coords, duration=1.0) -> None
```

---

### BTkTextEditor

#### Constructor
```python
BTkTextEditor(parent, width=None, height=None, wrap="word",
              syntax_highlight=True, **kwargs)
```

#### Methods
```python
get_text() -> str
set_text(text: str) -> None
insert_text(text: str, position="end") -> None
find_text(pattern: str, start="1.0") -> str
replace_text(old: str, new: str, count=-1) -> int
set_syntax_theme(theme: str) -> None
enable_line_numbers(state: bool) -> None
```

---

### BTkSystemTray

#### Constructor
```python
BTkSystemTray(app, icon_path=None, menu_items=None, **kwargs)
```

#### Methods
```python
show_tray() -> None
hide_tray() -> None
update_icon(icon_path: str) -> None
show_notification(title: str, message: str) -> None
add_menu_item(text: str, command: callable) -> None
```

---

## 🎨 Theming System

### Theme Structure
```python
{
    "bg_color": "#FFFFFF",           # Background color
    "fg_color": "#000000",           # Foreground/text color
    "button_color": "#E1E1E1",       # Button background
    "button_hover": "#D1D1D1",       # Button hover state
    "entry_bg": "#FFFFFF",           # Entry background
    "entry_border": "#CCCCCC",       # Entry border
    "accent_color": "#0078D4",       # Accent/highlight color
    "success_color": "#107C10",      # Success state color
    "warning_color": "#FF8C00",      # Warning state color
    "error_color": "#D13438"         # Error state color
}
```

### Creating Custom Themes
```python
# Define custom theme
custom_theme = {
    "bg_color": "#2D2D30",
    "fg_color": "#FFFFFF",
    "button_color": "#3F3F46",
    "button_hover": "#4F4F56",
    "entry_bg": "#1E1E1E",
    "entry_border": "#404040",
    "accent_color": "#007ACC"
}

# Apply to window
app = BTk(theme="custom")
app.set_theme_colors(custom_theme)
```

### Built-in Themes
- `"light"` - Light theme (default)
- `"dark"` - Dark theme
- `"blue"` - Blue accent theme
- `"green"` - Green accent theme
- `"auto"` - System theme detection

---

## 🎯 Event System

### Standard Events
All components support standard tkinter events plus enhanced BetterTkinter events.

#### Mouse Events
```python
"<Button-1>"         # Left click
"<Button-3>"         # Right click
"<Double-Button-1>"  # Double click
"<Enter>"            # Mouse enter
"<Leave>"            # Mouse leave
"<Motion>"           # Mouse motion
```

#### Keyboard Events
```python
"<Key>"              # Any key press
"<Return>"           # Enter key
"<Escape>"           # Escape key
"<Tab>"              # Tab key
"<Control-a>"        # Ctrl+A (select all)
```

#### Custom Events
```python
"<ThemeChanged>"     # Theme changed
"<WindowResize>"     # Window resized
"<FocusIn>"          # Component gained focus
"<FocusOut>"         # Component lost focus
```

### Event Binding
```python
# Bind to standard events
widget.bind("<Button-1>", callback_function)

# Bind to custom events  
widget.bind("<ThemeChanged>", theme_change_handler)

# Bind with additional data
widget.bind("<Button-1>", lambda e: callback_with_data(e, extra_data))
```

---

## 🔧 Utility Functions

### Color Utilities
```python
from bettertkinter.utils import ColorUtils

# Convert between color formats
rgb = ColorUtils.hex_to_rgb("#FF6B35")          # (255, 107, 53)
hex_color = ColorUtils.rgb_to_hex(255, 107, 53) # "#FF6B35"
hsl = ColorUtils.rgb_to_hsl(255, 107, 53)       # (14, 100, 60)

# Generate color variations
darker = ColorUtils.darken_color("#FF6B35", 0.2)   # Darken by 20%
lighter = ColorUtils.lighten_color("#FF6B35", 0.2) # Lighten by 20%
```

### Animation Utilities
```python
from bettertkinter.utils import AnimationUtils

# Animate property changes
AnimationUtils.animate_property(
    widget,
    property="bg_color", 
    start_value="#FF0000",
    end_value="#00FF00",
    duration=1.0
)

# Fade in/out effects
AnimationUtils.fade_in(widget, duration=0.5)
AnimationUtils.fade_out(widget, duration=0.5)
```

### Layout Utilities
```python
from bettertkinter.utils import LayoutUtils

# Auto-arrange components
LayoutUtils.auto_grid(parent, components, columns=3, padding=10)

# Responsive layout
LayoutUtils.make_responsive(parent, breakpoints={
    "small": 480,
    "medium": 768, 
    "large": 1024
})
```

### Validation Utilities
```python
from bettertkinter.utils import ValidationUtils

# Built-in validators
is_email = ValidationUtils.is_valid_email("test@example.com")
is_phone = ValidationUtils.is_valid_phone("+1-555-123-4567") 
is_url = ValidationUtils.is_valid_url("https://example.com")

# Custom validation
def validate_password(password):
    return (len(password) >= 8 and 
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password))
```

---

## 📊 Constants and Enums

### Component States
```python
from bettertkinter.constants import ComponentState

ComponentState.NORMAL    # Component is normal
ComponentState.DISABLED  # Component is disabled  
ComponentState.ACTIVE    # Component is active
ComponentState.HOVER     # Component is being hovered
ComponentState.FOCUS     # Component has focus
```

### Alignment Constants
```python
from bettertkinter.constants import Alignment

Alignment.LEFT    # Left alignment
Alignment.CENTER  # Center alignment
Alignment.RIGHT   # Right alignment
Alignment.TOP     # Top alignment
Alignment.BOTTOM  # Bottom alignment
```

### Animation Easing
```python
from bettertkinter.constants import Easing

Easing.LINEAR      # Linear animation
Easing.EASE_IN     # Ease in
Easing.EASE_OUT    # Ease out
Easing.EASE_IN_OUT # Ease in and out
Easing.BOUNCE      # Bounce effect
```

---

## 🚨 Exception Classes

### BetterTkinter Exceptions
```python
from bettertkinter.exceptions import (
    BTkError,           # Base BetterTkinter exception
    ThemeError,         # Theme-related errors
    ComponentError,     # Component-related errors  
    ValidationError,    # Validation errors
    AnimationError      # Animation errors
)

# Example usage
try:
    app.configure_theme("invalid_theme")
except ThemeError as e:
    print(f"Theme error: {e}")
```

---

## 📈 Performance Considerations

### Optimization Tips

1. **Component Creation**
   ```python
   # Efficient: Create components once
   button = BTkButton(parent, text="Click me")
   
   # Inefficient: Recreating components
   def update_button():
       old_button.destroy()
       new_button = BTkButton(parent, text="Updated")
   ```

2. **Event Binding**
   ```python
   # Efficient: Single event handler
   def handle_all_buttons(event):
       button_id = event.widget.id
       # Handle based on ID
   
   # Less efficient: Multiple handlers
   button1.bind("<Button-1>", handler1)
   button2.bind("<Button-1>", handler2)
   ```

3. **Theme Updates**
   ```python
   # Efficient: Batch theme updates
   with app.batch_theme_update():
       app.set_theme_colors(new_colors)
       app.apply_theme_to_children()
   ```

### Memory Management
```python
# Properly destroy components
def cleanup():
    for widget in widgets_to_destroy:
        widget.destroy()
    
    # Clear references
    widgets_to_destroy.clear()
```

---

## 🔍 Debugging and Development

### Debug Mode
```python
import bettertkinter as btk

# Enable debug mode
btk.set_debug_mode(True)

# Debug specific components
btk.debug_component(my_button, level="verbose")
```

### Logging
```python
import logging
from bettertkinter.utils import setup_logging

# Setup BetterTkinter logging
setup_logging(level=logging.DEBUG, file="btk.log")
```

### Component Inspection
```python
# Inspect component properties
component_info = widget.inspect()
print(f"Component: {component_info['type']}")
print(f"Properties: {component_info['properties']}")
print(f"Children: {component_info['children']}")
```

---

This API reference provides comprehensive documentation for all BetterTkinter functionality. For implementation examples and tutorials, see the [component documentation](../components/) and [guides](../guides/).
