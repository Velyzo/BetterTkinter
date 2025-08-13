import tkinter as tk
import colorsys

class BTkColorPicker(tk.Frame):
    def __init__(self, parent, initial_color="#FF0000", callback=None, 
                 width=300, height=200, **kwargs):
        super().__init__(parent, bg=parent.cget('bg'), **kwargs)
        
        self.callback = callback
        self.width = width
        self.height = height
        self.current_color = initial_color
        
        # Convert initial color to HSV
        self.h, self.s, self.v = self.hex_to_hsv(initial_color)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main canvas for color area
        self.canvas = tk.Canvas(self, width=self.width, height=self.height-50,
                              bg="white", highlightthickness=1, highlightcolor="#CCC")
        self.canvas.pack(pady=10)
        
        # Hue slider
        self.hue_canvas = tk.Canvas(self, width=self.width, height=20,
                                  bg="white", highlightthickness=1, highlightcolor="#CCC")
        self.hue_canvas.pack(pady=5)
        
        # Color preview and hex input
        preview_frame = tk.Frame(self, bg=self.master.cget('bg'))
        preview_frame.pack(pady=5)
        
        self.color_preview = tk.Label(preview_frame, width=6, height=2, 
                                    bg=self.current_color, relief="solid", borderwidth=1)
        self.color_preview.pack(side="left", padx=5)
        
        self.hex_entry = tk.Entry(preview_frame, width=10, justify="center")
        self.hex_entry.pack(side="left", padx=5)
        self.hex_entry.insert(0, self.current_color)
        self.hex_entry.bind("<Return>", self.on_hex_change)
        
        # Bind events
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.hue_canvas.bind("<Button-1>", self.on_hue_click)
        self.hue_canvas.bind("<B1-Motion>", self.on_hue_drag)
        
        self.draw_color_area()
        self.draw_hue_bar()
        self.draw_cursors()
        
    def draw_color_area(self):
        """Draw the saturation/value color area"""
        self.canvas.delete("color_area")
        
        # Create color gradient
        for x in range(0, self.width, 2):
            for y in range(0, self.height-50, 2):
                s = x / self.width
                v = 1 - (y / (self.height-50))
                
                rgb = colorsys.hsv_to_rgb(self.h, s, v)
                hex_color = "#{:02x}{:02x}{:02x}".format(
                    int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
                )
                
                self.canvas.create_rectangle(x, y, x+2, y+2, fill=hex_color, 
                                           outline=hex_color, tags="color_area")
    
    def draw_hue_bar(self):
        """Draw the hue slider bar"""
        self.hue_canvas.delete("hue_bar")
        
        for x in range(0, self.width, 2):
            h = x / self.width
            rgb = colorsys.hsv_to_rgb(h, 1, 1)
            hex_color = "#{:02x}{:02x}{:02x}".format(
                int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
            )
            
            self.hue_canvas.create_rectangle(x, 0, x+2, 20, fill=hex_color, 
                                           outline=hex_color, tags="hue_bar")
    
    def draw_cursors(self):
        """Draw selection cursors"""
        self.canvas.delete("cursor")
        self.hue_canvas.delete("hue_cursor")
        
        # Main area cursor
        x = self.s * self.width
        y = (1 - self.v) * (self.height - 50)
        
        self.canvas.create_oval(x-5, y-5, x+5, y+5, outline="white", width=2, tags="cursor")
        self.canvas.create_oval(x-3, y-3, x+3, y+3, outline="black", width=1, tags="cursor")
        
        # Hue cursor
        hue_x = self.h * self.width
        self.hue_canvas.create_polygon([hue_x-5, 0, hue_x+5, 0, hue_x, 5], 
                                     fill="white", outline="black", tags="hue_cursor")
        self.hue_canvas.create_polygon([hue_x-5, 20, hue_x+5, 20, hue_x, 15], 
                                     fill="white", outline="black", tags="hue_cursor")
    
    def on_canvas_click(self, event):
        self.update_sv(event.x, event.y)
        
    def on_canvas_drag(self, event):
        self.update_sv(event.x, event.y)
        
    def on_hue_click(self, event):
        self.update_hue(event.x)
        
    def on_hue_drag(self, event):
        self.update_hue(event.x)
        
    def update_sv(self, x, y):
        """Update saturation and value"""
        self.s = max(0, min(1, x / self.width))
        self.v = max(0, min(1, 1 - (y / (self.height - 50))))
        
        self.update_color()
        
    def update_hue(self, x):
        """Update hue"""
        self.h = max(0, min(1, x / self.width))
        
        self.draw_color_area()
        self.update_color()
        
    def update_color(self):
        """Update current color and UI"""
        rgb = colorsys.hsv_to_rgb(self.h, self.s, self.v)
        self.current_color = "#{:02x}{:02x}{:02x}".format(
            int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)
        )
        
        self.color_preview.config(bg=self.current_color)
        self.hex_entry.delete(0, tk.END)
        self.hex_entry.insert(0, self.current_color)
        
        self.draw_cursors()
        
        if self.callback:
            self.callback(self.current_color)
    
    def on_hex_change(self, event):
        """Handle hex color input"""
        try:
            hex_color = self.hex_entry.get().strip()
            if not hex_color.startswith('#'):
                hex_color = '#' + hex_color
                
            # Validate hex color
            int(hex_color[1:], 16)
            if len(hex_color) == 7:
                self.current_color = hex_color
                self.h, self.s, self.v = self.hex_to_hsv(hex_color)
                self.draw_color_area()
                self.draw_cursors()
                self.color_preview.config(bg=self.current_color)
                
                if self.callback:
                    self.callback(self.current_color)
        except ValueError:
            # Invalid hex color, revert
            self.hex_entry.delete(0, tk.END)
            self.hex_entry.insert(0, self.current_color)
    
    def hex_to_hsv(self, hex_color):
        """Convert hex color to HSV"""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
        return colorsys.rgb_to_hsv(*rgb)
    
    def get_color(self):
        """Get current color as hex"""
        return self.current_color
    
    def set_color(self, hex_color):
        """Set color programmatically"""
        self.current_color = hex_color
        self.h, self.s, self.v = self.hex_to_hsv(hex_color)
        self.draw_color_area()
        self.draw_cursors()
        self.color_preview.config(bg=self.current_color)
        self.hex_entry.delete(0, tk.END)
        self.hex_entry.insert(0, self.current_color)
