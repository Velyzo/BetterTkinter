import tkinter as tk
import math

class BTkProgressBar(tk.Canvas):
    def __init__(self, parent, width=200, height=20, bg_color="#E0E0E0", 
                 fg_color="#0078D7", border_radius=10, animated=False, 
                 animation_speed=0.1, gradient=True, **kwargs):
        super().__init__(parent, width=width, height=height, bg=parent.cget('bg'), 
                        highlightthickness=0, **kwargs)
        
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.border_radius = border_radius
        self.animated = animated
        self.animation_speed = animation_speed
        self.gradient = gradient
        
        self.value = 0
        self.animation_offset = 0
        
        self.draw_progress()
        
        if self.animated:
            self.animate()
    
    def draw_progress(self):
        self.delete("all")
        
        # Draw background
        self.create_rounded_rect(0, 0, self.width, self.height, 
                               self.border_radius, fill=self.bg_color, outline="")
        
        # Draw progress
        if self.value > 0:
            progress_width = (self.value / 100) * self.width
            
            if self.gradient:
                # Create gradient effect
                for i in range(int(progress_width)):
                    color_intensity = 0.7 + 0.3 * math.sin(i * 0.1 + self.animation_offset)
                    color = self.lighten_color(self.fg_color, color_intensity)
                    self.create_line(i, 2, i, self.height - 2, fill=color, width=1)
            else:
                self.create_rounded_rect(0, 0, progress_width, self.height, 
                                       self.border_radius, fill=self.fg_color, outline="")
    
    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        points = []
        for x, y in [(x1, y1 + radius), (x1, y1), (x1 + radius, y1), 
                     (x2 - radius, y1), (x2, y1), (x2, y1 + radius),
                     (x2, y2 - radius), (x2, y2), (x2 - radius, y2),
                     (x1 + radius, y2), (x1, y2), (x1, y2 - radius)]:
            points.extend([x, y])
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def lighten_color(self, color, factor):
        if color.startswith('#'):
            color = color[1:]
        r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
        r = int(r * factor)
        g = int(g * factor)
        b = int(b * factor)
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def animate(self):
        if self.animated:
            self.animation_offset += self.animation_speed
            self.draw_progress()
            self.after(50, self.animate)
    
    def set(self, value):
        self.value = max(0, min(100, value))
        self.draw_progress()
    
    def get(self):
        return self.value
