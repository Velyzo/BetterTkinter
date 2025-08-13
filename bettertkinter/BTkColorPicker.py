import tkinter as tk
from tkinter import messagebox
import math

class BTkColorPicker(tk.Canvas):
    """Modern BetterTkinter color picker component"""
    
    # Constants
    DEFAULT_FONT = "Segoe UI"
    DEFAULT_WIDTH = 250
    DEFAULT_HEIGHT = 200
    
    def __init__(self, parent, **kwargs):
        # Configuration
        self.width = kwargs.get('width', self.DEFAULT_WIDTH)
        self.height = kwargs.get('height', self.DEFAULT_HEIGHT)
        self.command = kwargs.get('command', None)
        self.bg_color = kwargs.get('bg_color', "#FFFFFF")
        
        # Initialize canvas
        super().__init__(parent,
                        width=self.width,
                        height=self.height,
                        bg=self.bg_color,
                        highlightthickness=0,
                        bd=0)
        
        # Color state
        self._selected_color = kwargs.get('color', "#FF0000")
        self._hue = 0
        self._saturation = 1.0
        self._value = 1.0
        
        # UI elements
        self.hue_bar_width = 20
        self.color_area_width = self.width - self.hue_bar_width - 20
        self.color_area_height = self.height - 50
        
        # Convert initial color to HSV
        self._rgb_to_hsv(*self._hex_to_rgb(self._selected_color))
        
        # Render and bind events
        self._render()
        self._bind_events()
    
    def _hex_to_rgb(self, hex_color):
        """Convert hex color to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def _rgb_to_hex(self, r, g, b):
        """Convert RGB to hex"""
        return f"#{int(r):02x}{int(g):02x}{int(b):02x}"
    
    def _hsv_to_rgb(self, h, s, v):
        """Convert HSV to RGB"""
        h = h / 360.0
        c = v * s
        x = c * (1 - abs((h * 6) % 2 - 1))
        m = v - c
        
        if 0 <= h < 1/6:
            r, g, b = c, x, 0
        elif 1/6 <= h < 2/6:
            r, g, b = x, c, 0
        elif 2/6 <= h < 3/6:
            r, g, b = 0, c, x
        elif 3/6 <= h < 4/6:
            r, g, b = 0, x, c
        elif 4/6 <= h < 5/6:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        
        return ((r + m) * 255, (g + m) * 255, (b + m) * 255)
    
    def _rgb_to_hsv(self, r, g, b):
        """Convert RGB to HSV"""
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        max_val = max(r, g, b)
        min_val = min(r, g, b)
        diff = max_val - min_val
        
        # Hue
        if diff == 0:
            h = 0
        elif max_val == r:
            h = (60 * ((g - b) / diff) + 360) % 360
        elif max_val == g:
            h = (60 * ((b - r) / diff) + 120) % 360
        else:
            h = (60 * ((r - g) / diff) + 240) % 360
        
        # Saturation
        s = 0 if max_val == 0 else diff / max_val
        
        # Value
        v = max_val
        
        self._hue = h
        self._saturation = s
        self._value = v
    
    def _render(self):
        """Render color picker"""
        self.delete("all")
        
        # Draw color area (saturation/value)
        self._draw_color_area()
        
        # Draw hue bar
        self._draw_hue_bar()
        
        # Draw selected color preview
        self._draw_color_preview()
        
        # Draw selector indicators
        self._draw_selectors()
    
    def _draw_color_area(self):
        """Draw the main color selection area"""
        area_x = 10
        area_y = 10
        
        # Create gradient from white to pure hue to black
        for x in range(self.color_area_width):
            for y in range(self.color_area_height):
                sat = x / self.color_area_width
                val = 1 - (y / self.color_area_height)
                
                r, g, b = self._hsv_to_rgb(self._hue, sat, val)
                color = self._rgb_to_hex(r, g, b)
                
                # Only draw every 4th pixel for performance
                if x % 4 == 0 and y % 4 == 0:
                    self.create_rectangle(
                        area_x + x, area_y + y,
                        area_x + x + 4, area_y + y + 4,
                        fill=color, outline=color
                    )
    
    def _draw_hue_bar(self):
        """Draw hue selection bar"""
        bar_x = self.width - self.hue_bar_width - 5
        bar_y = 10
        bar_height = self.color_area_height
        
        # Draw hue gradient
        for y in range(bar_height):
            hue = (y / bar_height) * 360
            r, g, b = self._hsv_to_rgb(hue, 1.0, 1.0)
            color = self._rgb_to_hex(r, g, b)
            
            if y % 2 == 0:  # Performance optimization
                self.create_rectangle(
                    bar_x, bar_y + y,
                    bar_x + self.hue_bar_width, bar_y + y + 2,
                    fill=color, outline=color
                )
    
    def _draw_color_preview(self):
        """Draw selected color preview"""
        preview_x = 10
        preview_y = self.height - 30
        preview_width = 80
        preview_height = 20
        
        # Draw preview rectangle
        self.create_rectangle(
            preview_x, preview_y,
            preview_x + preview_width, preview_y + preview_height,
            fill=self._selected_color,
            outline="#CCCCCC",
            width=1
        )
        
        # Draw color text
        self.create_text(
            preview_x + preview_width + 10, preview_y + preview_height // 2,
            text=self._selected_color,
            fill="#333333",
            font=(self.DEFAULT_FONT, 9, "normal"),
            anchor="w"
        )
    
    def _draw_selectors(self):
        """Draw selection indicators"""
        # Color area selector
        area_x = 10 + (self._saturation * self.color_area_width)
        area_y = 10 + ((1 - self._value) * self.color_area_height)
        
        # Draw crosshair
        self.create_oval(
            area_x - 4, area_y - 4,
            area_x + 4, area_y + 4,
            outline="white", width=2, fill=""
        )
        self.create_oval(
            area_x - 3, area_y - 3,
            area_x + 3, area_y + 3,
            outline="black", width=1, fill=""
        )
        
        # Hue bar selector
        hue_x = self.width - self.hue_bar_width - 5
        hue_y = 10 + (self._hue / 360) * self.color_area_height
        
        # Draw hue indicator
        self.create_rectangle(
            hue_x - 2, hue_y - 2,
            hue_x + self.hue_bar_width + 2, hue_y + 2,
            outline="white", width=2, fill=""
        )
        self.create_rectangle(
            hue_x - 1, hue_y - 1,
            hue_x + self.hue_bar_width + 1, hue_y + 1,
            outline="black", width=1, fill=""
        )
    
    def _bind_events(self):
        """Bind mouse events"""
        self.bind("<Button-1>", self._on_click)
        self.bind("<B1-Motion>", self._on_drag)
    
    def _on_click(self, event):
        """Handle mouse click"""
        self._update_color_from_position(event.x, event.y)
    
    def _on_drag(self, event):
        """Handle mouse drag"""
        self._update_color_from_position(event.x, event.y)
    
    def _update_color_from_position(self, x, y):
        """Update color based on mouse position"""
        # Check if click is in color area
        if 10 <= x <= 10 + self.color_area_width and 10 <= y <= 10 + self.color_area_height:
            self._saturation = max(0, min(1, (x - 10) / self.color_area_width))
            self._value = max(0, min(1, 1 - (y - 10) / self.color_area_height))
            self._update_selected_color()
        
        # Check if click is in hue bar
        elif (self.width - self.hue_bar_width - 5) <= x <= self.width - 5 and 10 <= y <= 10 + self.color_area_height:
            self._hue = max(0, min(360, (y - 10) / self.color_area_height * 360))
            self._update_selected_color()
    
    def _update_selected_color(self):
        """Update the selected color and trigger callback"""
        r, g, b = self._hsv_to_rgb(self._hue, self._saturation, self._value)
        self._selected_color = self._rgb_to_hex(r, g, b)
        
        self._render()
        
        if self.command:
            try:
                self.command(self._selected_color)
            except Exception as e:
                print(f"Color picker command error: {e}")
    
    def get_color(self):
        """Get selected color"""
        return self._selected_color
    
    def set_color(self, color):
        """Set selected color"""
        self._selected_color = color
        self._rgb_to_hsv(*self._hex_to_rgb(color))
        self._render()

# Test function
if __name__ == "__main__":
    def test_colorpicker():
        root = tk.Tk()
        root.title("BTkColorPicker Test")
        root.geometry("400x350")
        root.configure(bg="#FFFFFF")
        
        # Header
        tk.Label(root, text="BTkColorPicker Component Test",
                font=("Segoe UI", 14, "bold"),
                bg="#FFFFFF", fg="#333333").pack(pady=10)
        
        # Color change callback
        def on_color_change(color):
            print(f"Color selected: {color}")
            result_label.config(text=f"Selected: {color}", fg=color)
        
        # Color picker
        picker = BTkColorPicker(root, command=on_color_change)
        picker.pack(pady=20)
        
        # Result label
        result_label = tk.Label(root, text="Selected: #FF0000",
                              font=("Segoe UI", 12, "normal"),
                              bg="#FFFFFF", fg="#FF0000")
        result_label.pack(pady=10)
        
        # Control buttons
        btn_frame = tk.Frame(root, bg="#FFFFFF")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Red",
                 command=lambda: picker.set_color("#FF0000")).pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="Green",
                 command=lambda: picker.set_color("#00FF00")).pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="Blue",
                 command=lambda: picker.set_color("#0000FF")).pack(side="left", padx=5)
        
        root.mainloop()
    
    test_colorpicker()
