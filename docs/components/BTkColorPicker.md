# 🎨 BTkColorPicker - Advanced Color Selection

The `BTkColorPicker` component provides a sophisticated color selection interface with multiple input methods, real-time preview, and support for various color formats.

## 📋 Overview

`BTkColorPicker` offers:
- Multiple color input methods (wheel, sliders, palette)
- Support for RGB, HSV, HSL, and Hex formats
- Real-time color preview
- Custom color palettes
- Color history and favorites
- Eye dropper functionality
- Accessibility features

## 🚀 Basic Usage

```python
from bettertkinter import BTk, BTkColorPicker, BTkButton, BTkLabel

app = BTk()

# Create color picker
color_picker = BTkColorPicker(app, initial_color="#FF6B35")
color_picker.pack(pady=20)

# Display selected color
def on_color_change(color):
    print(f"Selected color: {color}")

color_picker.bind_color_change(on_color_change)

app.mainloop()
```

## 🔧 Constructor

```python
BTkColorPicker(parent, initial_color="#FFFFFF", show_alpha=True, 
               color_format="hex", width=400, height=300,
               show_preview=True, enable_eyedropper=True,
               palette_colors=None, **kwargs)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent` | Widget | - | Parent widget |
| `initial_color` | str | "#FFFFFF" | Starting color (hex, rgb, or name) |
| `show_alpha` | bool | True | Show alpha channel controls |
| `color_format` | str | "hex" | Default format ("hex", "rgb", "hsv", "hsl") |
| `width` | int | 400 | Color picker width |
| `height` | int | 300 | Color picker height |
| `show_preview` | bool | True | Show color preview area |
| `enable_eyedropper` | bool | True | Enable eyedropper tool |
| `palette_colors` | list | None | Custom color palette |

## 🎨 Methods

### Color Selection

#### `get_color(format="hex")`
Returns the currently selected color.

```python
# Get color in different formats
hex_color = color_picker.get_color("hex")        # "#FF6B35"
rgb_color = color_picker.get_color("rgb")        # (255, 107, 53)
rgba_color = color_picker.get_color("rgba")      # (255, 107, 53, 255)
hsv_color = color_picker.get_color("hsv")        # (14, 79, 100)
hsl_color = color_picker.get_color("hsl")        # (14, 100, 60)
```

**Parameters:**
- `format` (str): Output format ("hex", "rgb", "rgba", "hsv", "hsl")

**Returns:**
- Color in specified format

#### `set_color(color, format="hex")`
Sets the current color.

```python
# Set color in different formats
color_picker.set_color("#FF6B35", "hex")
color_picker.set_color((255, 107, 53), "rgb")
color_picker.set_color("coral", "name")
```

#### `get_rgb()`
Returns RGB values as tuple.

```python
r, g, b = color_picker.get_rgb()  # (255, 107, 53)
```

#### `get_hex()`
Returns hex color string.

```python
hex_color = color_picker.get_hex()  # "#FF6B35"
```

### Color Format Conversion

#### `rgb_to_hex(r, g, b)`
Converts RGB to hex format.

```python
hex_color = color_picker.rgb_to_hex(255, 107, 53)  # "#FF6B35"
```

#### `hex_to_rgb(hex_color)`
Converts hex to RGB format.

```python
r, g, b = color_picker.hex_to_rgb("#FF6B35")  # (255, 107, 53)
```

#### `rgb_to_hsv(r, g, b)`
Converts RGB to HSV format.

```python
h, s, v = color_picker.rgb_to_hsv(255, 107, 53)  # (14, 79, 100)
```

#### `hsv_to_rgb(h, s, v)`
Converts HSV to RGB format.

```python
r, g, b = color_picker.hsv_to_rgb(14, 79, 100)  # (255, 107, 53)
```

### Event Binding

#### `bind_color_change(callback)`
Binds callback to color change events.

```python
def color_changed(color):
    print(f"Color changed to: {color}")

color_picker.bind_color_change(color_changed)
```

#### `bind_color_select(callback)`
Binds callback to color selection completion.

```python
def color_selected(color):
    print(f"Color selected: {color}")

color_picker.bind_color_select(color_selected)
```

### Palette Management

#### `add_to_palette(color)`
Adds color to custom palette.

```python
color_picker.add_to_palette("#FF6B35")
```

#### `remove_from_palette(color)`
Removes color from palette.

```python
color_picker.remove_from_palette("#FF6B35")
```

#### `set_palette(colors)`
Sets the entire color palette.

```python
custom_palette = ["#FF6B35", "#004E89", "#00A896", "#F18F01", "#C73E1D"]
color_picker.set_palette(custom_palette)
```

#### `get_palette()`
Returns current color palette.

```python
palette = color_picker.get_palette()
```

### Color History

#### `get_history()`
Returns color selection history.

```python
history = color_picker.get_history()  # List of recent colors
```

#### `clear_history()`
Clears color history.

```python
color_picker.clear_history()
```

### Eyedropper Tool

#### `start_eyedropper()`
Activates the eyedropper tool.

```python
color_picker.start_eyedropper()
```

#### `stop_eyedropper()`
Deactivates the eyedropper tool.

```python
color_picker.stop_eyedropper()
```

## 📱 Examples

### Basic Color Picker

```python
from bettertkinter import BTk, BTkColorPicker, BTkLabel, BTkFrame

class BasicColorDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Basic Color Picker")
        self.geometry("500x400")
        
        # Create main frame
        main_frame = BTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Color picker
        self.color_picker = BTkColorPicker(
            main_frame,
            initial_color="#FF6B35",
            width=300,
            height=250
        )
        self.color_picker.pack(pady=20)
        
        # Color display
        self.color_display = BTkLabel(
            main_frame,
            text="Selected Color: #FF6B35",
            font_size=14
        )
        self.color_display.pack(pady=10)
        
        # Bind color change
        self.color_picker.bind_color_change(self.on_color_change)
    
    def on_color_change(self, color):
        self.color_display.configure(text=f"Selected Color: {color}")
        print(f"RGB: {self.color_picker.get_color('rgb')}")
        print(f"HSV: {self.color_picker.get_color('hsv')}")

app = BasicColorDemo()
app.mainloop()
```

### Advanced Color Picker with Formats

```python
from bettertkinter import (
    BTk, BTkColorPicker, BTkLabel, BTkFrame,
    BTkButton, BTkEntry, BTkComboBox
)

class AdvancedColorDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Color Picker")
        self.geometry("600x500")
        
        self.create_ui()
    
    def create_ui(self):
        # Main container
        container = BTkFrame(self)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title = BTkLabel(container, text="Advanced Color Picker", font_size=18)
        title.pack(pady=(0, 20))
        
        # Color picker frame
        picker_frame = BTkFrame(container)
        picker_frame.pack(fill="x", pady=(0, 20))
        
        # Color picker
        self.color_picker = BTkColorPicker(
            picker_frame,
            initial_color="#FF6B35",
            show_alpha=True,
            enable_eyedropper=True,
            width=400,
            height=280
        )
        self.color_picker.pack(side="left", padx=(0, 20))
        
        # Controls frame
        controls_frame = BTkFrame(picker_frame)
        controls_frame.pack(side="right", fill="y")
        
        # Format selector
        BTkLabel(controls_frame, text="Output Format:", font_size=12).pack(anchor="w", pady=(10, 5))
        self.format_combo = BTkComboBox(
            controls_frame,
            values=["hex", "rgb", "rgba", "hsv", "hsl"],
            state="readonly"
        )
        self.format_combo.set("hex")
        self.format_combo.pack(fill="x", pady=(0, 15))
        
        # Color value display
        BTkLabel(controls_frame, text="Color Value:", font_size=12).pack(anchor="w", pady=(0, 5))
        self.color_value = BTkEntry(controls_frame, state="readonly")
        self.color_value.pack(fill="x", pady=(0, 15))
        
        # Custom color input
        BTkLabel(controls_frame, text="Set Color:", font_size=12).pack(anchor="w", pady=(0, 5))
        self.color_input = BTkEntry(controls_frame, placeholder_text="Enter color...")
        self.color_input.pack(fill="x", pady=(0, 5))
        
        BTkButton(
            controls_frame,
            text="Apply Color",
            command=self.apply_color,
            style="primary"
        ).pack(fill="x", pady=(0, 15))
        
        # Eyedropper button
        BTkButton(
            controls_frame,
            text="🎯 Eyedropper",
            command=self.toggle_eyedropper,
            style="secondary"
        ).pack(fill="x", pady=(0, 10))
        
        # Random color button
        BTkButton(
            controls_frame,
            text="🎲 Random Color",
            command=self.random_color,
            style="secondary"
        ).pack(fill="x")
        
        # Color history frame
        history_frame = BTkFrame(container)
        history_frame.pack(fill="x", pady=(0, 10))
        
        BTkLabel(history_frame, text="Recent Colors:", font_size=12).pack(anchor="w", pady=(5, 10))
        
        self.history_frame = BTkFrame(history_frame)
        self.history_frame.pack(fill="x", pady=(0, 10))
        
        # Bind events
        self.color_picker.bind_color_change(self.on_color_change)
        self.format_combo.bind("<<ComboboxSelected>>", self.on_format_change)
        
        # Initialize
        self.on_color_change(self.color_picker.get_color())
    
    def on_color_change(self, color):
        # Update color value display
        format_type = self.format_combo.get()
        color_value = self.color_picker.get_color(format_type)
        
        # Format display string
        if format_type in ["rgb", "rgba", "hsv", "hsl"]:
            if isinstance(color_value, tuple):
                color_str = f"{format_type.upper()}{color_value}"
            else:
                color_str = str(color_value)
        else:
            color_str = str(color_value)
        
        self.color_value.configure(state="normal")
        self.color_value.delete(0, "end")
        self.color_value.insert(0, color_str)
        self.color_value.configure(state="readonly")
        
        # Update history
        self.update_history()
    
    def on_format_change(self, event=None):
        # Update display when format changes
        self.on_color_change(self.color_picker.get_color())
    
    def apply_color(self):
        color_input = self.color_input.get().strip()
        if color_input:
            try:
                # Try to set the color
                if color_input.startswith('#'):
                    self.color_picker.set_color(color_input, "hex")
                elif color_input.startswith('rgb'):
                    # Parse RGB string
                    import re
                    numbers = re.findall(r'\d+', color_input)
                    if len(numbers) >= 3:
                        rgb = tuple(int(n) for n in numbers[:3])
                        self.color_picker.set_color(rgb, "rgb")
                else:
                    # Try as color name
                    self.color_picker.set_color(color_input, "name")
                
                self.color_input.delete(0, "end")
                
            except Exception as e:
                from bettertkinter import BTkDialog
                BTkDialog.show_error("Invalid Color", f"Could not parse color: {color_input}")
    
    def toggle_eyedropper(self):
        try:
            self.color_picker.start_eyedropper()
        except Exception as e:
            from bettertkinter import BTkDialog
            BTkDialog.show_info("Eyedropper", "Eyedropper functionality requires additional system permissions")
    
    def random_color(self):
        import random
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        self.color_picker.set_color((r, g, b), "rgb")
    
    def update_history(self):
        # Clear current history display
        for widget in self.history_frame.winfo_children():
            widget.destroy()
        
        # Get recent colors (simulate history for demo)
        history = getattr(self, '_color_history', [])
        current_color = self.color_picker.get_color("hex")
        
        # Add current color to history if not already there
        if current_color not in history:
            history.insert(0, current_color)
            history = history[:8]  # Keep last 8 colors
            self._color_history = history
        
        # Create color swatches
        for i, color in enumerate(history):
            swatch = BTkButton(
                self.history_frame,
                text="",
                width=30,
                height=30,
                corner_radius=15,
                bg_color=color,
                hover_color=color,
                border_width=2,
                border_color="#CCCCCC",
                command=lambda c=color: self.color_picker.set_color(c, "hex")
            )
            swatch.pack(side="left", padx=2)

app = AdvancedColorDemo()
app.mainloop()
```

### Color Palette Manager

```python
from bettertkinter import (
    BTk, BTkColorPicker, BTkFrame, BTkLabel,
    BTkButton, BTkEntry, BTkDialog
)
import json

class ColorPaletteManager(BTk):
    def __init__(self):
        super().__init__()
        self.title("Color Palette Manager")
        self.geometry("800x600")
        
        self.palettes = {
            "Default": ["#FF6B35", "#004E89", "#00A896", "#F18F01", "#C73E1D"],
            "Pastel": ["#FFB3BA", "#BAFFC9", "#BAE1FF", "#FFFFBA", "#FFD1BA"],
            "Vibrant": ["#FF0040", "#FF8C00", "#FFFF00", "#00FF00", "#0080FF"],
            "Earth": ["#8B4513", "#D2B48C", "#F4A460", "#CD853F", "#A0522D"]
        }
        
        self.current_palette = "Default"
        self.create_ui()
    
    def create_ui(self):
        # Main container
        container = BTkFrame(self)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        BTkLabel(container, text="Color Palette Manager", font_size=18).pack(pady=(0, 20))
        
        # Top frame for picker and palette selector
        top_frame = BTkFrame(container)
        top_frame.pack(fill="x", pady=(0, 20))
        
        # Color picker
        self.color_picker = BTkColorPicker(
            top_frame,
            initial_color="#FF6B35",
            width=350,
            height=250,
            palette_colors=self.palettes[self.current_palette]
        )
        self.color_picker.pack(side="left", padx=(0, 20))
        
        # Palette controls
        controls_frame = BTkFrame(top_frame)
        controls_frame.pack(side="right", fill="y")
        
        # Palette selector
        BTkLabel(controls_frame, text="Select Palette:", font_size=12).pack(anchor="w", pady=(10, 5))
        self.palette_combo = BTkComboBox(
            controls_frame,
            values=list(self.palettes.keys()),
            state="readonly"
        )
        self.palette_combo.set(self.current_palette)
        self.palette_combo.pack(fill="x", pady=(0, 15))
        self.palette_combo.bind("<<ComboboxSelected>>", self.on_palette_change)
        
        # Add color to palette
        BTkLabel(controls_frame, text="Add to Palette:", font_size=12).pack(anchor="w", pady=(0, 5))
        BTkButton(
            controls_frame,
            text="Add Current Color",
            command=self.add_current_color,
            style="primary"
        ).pack(fill="x", pady=(0, 15))
        
        # Create new palette
        BTkLabel(controls_frame, text="New Palette:", font_size=12).pack(anchor="w", pady=(0, 5))
        self.new_palette_entry = BTkEntry(controls_frame, placeholder_text="Palette name...")
        self.new_palette_entry.pack(fill="x", pady=(0, 5))
        
        BTkButton(
            controls_frame,
            text="Create Palette",
            command=self.create_new_palette,
            style="success"
        ).pack(fill="x", pady=(0, 15))
        
        # Save/Load buttons
        BTkButton(
            controls_frame,
            text="Save Palettes",
            command=self.save_palettes,
            style="secondary"
        ).pack(fill="x", pady=(0, 5))
        
        BTkButton(
            controls_frame,
            text="Load Palettes",
            command=self.load_palettes,
            style="secondary"
        ).pack(fill="x")
        
        # Palette display frame
        palette_frame = BTkFrame(container)
        palette_frame.pack(fill="both", expand=True)
        
        BTkLabel(palette_frame, text="Current Palette Colors:", font_size=14).pack(anchor="w", pady=(10, 10))
        
        self.palette_display = BTkFrame(palette_frame)
        self.palette_display.pack(fill="x", pady=(0, 20))
        
        # Initialize display
        self.update_palette_display()
    
    def on_palette_change(self, event=None):
        self.current_palette = self.palette_combo.get()
        self.color_picker.set_palette(self.palettes[self.current_palette])
        self.update_palette_display()
    
    def add_current_color(self):
        current_color = self.color_picker.get_color("hex")
        if current_color not in self.palettes[self.current_palette]:
            self.palettes[self.current_palette].append(current_color)
            self.color_picker.set_palette(self.palettes[self.current_palette])
            self.update_palette_display()
            BTkDialog.show_success("Success", f"Added {current_color} to {self.current_palette} palette!")
        else:
            BTkDialog.show_info("Info", "Color already exists in palette.")
    
    def create_new_palette(self):
        name = self.new_palette_entry.get().strip()
        if name and name not in self.palettes:
            self.palettes[name] = [self.color_picker.get_color("hex")]
            self.palette_combo.configure(values=list(self.palettes.keys()))
            self.palette_combo.set(name)
            self.current_palette = name
            self.new_palette_entry.delete(0, "end")
            self.on_palette_change()
            BTkDialog.show_success("Success", f"Created palette '{name}'!")
        elif name in self.palettes:
            BTkDialog.show_warning("Warning", "Palette name already exists!")
        else:
            BTkDialog.show_error("Error", "Please enter a palette name.")
    
    def update_palette_display(self):
        # Clear current display
        for widget in self.palette_display.winfo_children():
            widget.destroy()
        
        # Display current palette colors
        colors = self.palettes[self.current_palette]
        for i, color in enumerate(colors):
            color_frame = BTkFrame(self.palette_display)
            color_frame.pack(side="left", padx=5)
            
            # Color swatch
            swatch = BTkButton(
                color_frame,
                text="",
                width=50,
                height=50,
                corner_radius=25,
                bg_color=color,
                hover_color=color,
                border_width=2,
                border_color="#CCCCCC",
                command=lambda c=color: self.color_picker.set_color(c, "hex")
            )
            swatch.pack()
            
            # Color label
            BTkLabel(color_frame, text=color, font_size=8).pack(pady=(5, 0))
            
            # Remove button
            BTkButton(
                color_frame,
                text="✕",
                width=20,
                height=20,
                corner_radius=10,
                bg_color="#FF4444",
                hover_color="#FF6666",
                text_color="white",
                font_size=8,
                command=lambda c=color: self.remove_color(c)
            ).pack(pady=(2, 0))
    
    def remove_color(self, color):
        if len(self.palettes[self.current_palette]) > 1:
            self.palettes[self.current_palette].remove(color)
            self.color_picker.set_palette(self.palettes[self.current_palette])
            self.update_palette_display()
        else:
            BTkDialog.show_warning("Warning", "Cannot remove the last color from palette!")
    
    def save_palettes(self):
        try:
            with open("color_palettes.json", "w") as f:
                json.dump(self.palettes, f, indent=2)
            BTkDialog.show_success("Success", "Palettes saved to color_palettes.json!")
        except Exception as e:
            BTkDialog.show_error("Error", f"Failed to save palettes: {str(e)}")
    
    def load_palettes(self):
        try:
            with open("color_palettes.json", "r") as f:
                loaded_palettes = json.load(f)
            
            self.palettes.update(loaded_palettes)
            self.palette_combo.configure(values=list(self.palettes.keys()))
            BTkDialog.show_success("Success", "Palettes loaded successfully!")
            
        except FileNotFoundError:
            BTkDialog.show_warning("Warning", "No saved palettes file found.")
        except Exception as e:
            BTkDialog.show_error("Error", f"Failed to load palettes: {str(e)}")

app = ColorPaletteManager()
app.mainloop()
```

### Integration with Other Components

```python
from bettertkinter import (
    BTk, BTkColorPicker, BTkButton, BTkFrame,
    BTkLabel, BTkCanvas, BTkDialog
)

class ColorDrawingApp(BTk):
    """Integration example with canvas drawing"""
    
    def __init__(self):
        super().__init__()
        self.title("Color Drawing App")
        self.geometry("900x600")
        
        self.current_color = "#000000"
        self.brush_size = 5
        
        self.create_ui()
    
    def create_ui(self):
        # Main container
        container = BTkFrame(self)
        container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Left panel for tools
        tools_frame = BTkFrame(container, width=300)
        tools_frame.pack(side="left", fill="y", padx=(0, 10))
        tools_frame.pack_propagate(False)
        
        # Color picker
        BTkLabel(tools_frame, text="Color Selection", font_size=14).pack(pady=(10, 10))
        
        self.color_picker = BTkColorPicker(
            tools_frame,
            initial_color=self.current_color,
            width=280,
            height=200,
            show_alpha=False
        )
        self.color_picker.pack(pady=(0, 20))
        self.color_picker.bind_color_change(self.on_color_change)
        
        # Brush size
        BTkLabel(tools_frame, text="Brush Size", font_size=12).pack(anchor="w", padx=10)
        self.size_slider = BTkSlider(
            tools_frame,
            from_=1,
            to=20,
            number_of_steps=19
        )
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(fill="x", padx=10, pady=(5, 20))
        self.size_slider.configure(command=self.on_size_change)
        
        # Control buttons
        BTkButton(
            tools_frame,
            text="Clear Canvas",
            command=self.clear_canvas,
            style="warning"
        ).pack(fill="x", padx=10, pady=5)
        
        BTkButton(
            tools_frame,
            text="Save Drawing",
            command=self.save_drawing,
            style="success"
        ).pack(fill="x", padx=10, pady=5)
        
        # Canvas frame
        canvas_frame = BTkFrame(container)
        canvas_frame.pack(side="right", fill="both", expand=True)
        
        # Canvas
        self.canvas = BTkCanvas(canvas_frame, bg="white")
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Bind canvas events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        
        self.last_x = None
        self.last_y = None
    
    def on_color_change(self, color):
        self.current_color = color
        print(f"Drawing color changed to: {color}")
    
    def on_size_change(self, value):
        self.brush_size = int(value)
    
    def start_draw(self, event):
        self.last_x = event.x
        self.last_y = event.y
    
    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                width=self.brush_size,
                fill=self.current_color,
                capstyle="round",
                smooth=True
            )
        self.last_x = event.x
        self.last_y = event.y
    
    def clear_canvas(self):
        result = BTkDialog.ask_yes_no("Clear Canvas", "Are you sure you want to clear the canvas?")
        if result == "Yes":
            self.canvas.delete("all")
    
    def save_drawing(self):
        try:
            # This would require additional PIL functionality
            BTkDialog.show_info("Save", "Save functionality would require PIL/Pillow integration")
        except Exception as e:
            BTkDialog.show_error("Error", f"Failed to save: {str(e)}")

app = ColorDrawingApp()
app.mainloop()
```

## 🎯 Best Practices

1. **Initialize with sensible defaults**: Start with commonly used colors
2. **Bind color change events**: Provide real-time feedback
3. **Support multiple formats**: Allow users to work in their preferred format
4. **Provide color history**: Help users find recently used colors
5. **Use appropriate size**: Don't make the picker too small or too large
6. **Handle errors gracefully**: Validate color inputs
7. **Consider accessibility**: Provide alternative input methods

## 🐛 Common Issues

### Issue: Color not updating in real-time
```python
# Ensure proper event binding
color_picker.bind_color_change(callback_function)

# Check if callback is properly defined
def color_changed(color):
    print(f"New color: {color}")
```

### Issue: Invalid color format
```python
# Validate color inputs
def set_safe_color(color_picker, color, format_type):
    try:
        color_picker.set_color(color, format_type)
    except ValueError:
        print(f"Invalid color: {color}")
```

### Issue: Eyedropper not working
```python
# Check system permissions and availability
try:
    color_picker.start_eyedropper()
except Exception as e:
    print("Eyedropper not available:", e)
```

## 🔗 Related Components

- [BTkButton](BTkButton.md) - Color picker triggers
- [BTkCanvas](BTkCanvas.md) - Drawing applications
- [BTkSlider](BTkSlider.md) - RGB/HSV sliders

---

**Ready to add beautiful color selection with BTkColorPicker!** 🎨
