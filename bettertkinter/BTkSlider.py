import tkinter as tk
import math

class BTkSlider(tk.Canvas):
    def __init__(self, parent, from_=0, to=100, orientation="horizontal", command=None, 
                 width=300, height=20, bg_color="#E0E0E0", fg_color="#0078D7", 
                 handle_color="#FFFFFF", handle_size=20, border_radius=10, 
                 handle_border_width=2, handle_border_color="#0078D7", **kwargs):
        
        if orientation == "horizontal":
            super().__init__(parent, width=width, height=height, bg=parent.cget('bg'), 
                           highlightthickness=0, **kwargs)
        else:
            super().__init__(parent, width=height, height=width, bg=parent.cget('bg'), 
                           highlightthickness=0, **kwargs)
        
        self.from_ = from_
        self.to = to
        self.orientation = orientation
        self.command = command
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.handle_color = handle_color
        self.handle_size = handle_size
        self.border_radius = border_radius
        self.handle_border_width = handle_border_width
        self.handle_border_color = handle_border_color
        
        self.value = from_
        self.dragging = False
        
        self.draw_slider()
        
        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)
    
    def draw_slider(self):
        self.delete("all")
        
        if self.orientation == "horizontal":
            # Draw track
            track_y = self.winfo_reqheight() // 2
            self.create_rounded_rect(0, track_y - 3, self.winfo_reqwidth(), track_y + 3, 
                                   self.border_radius // 2, fill=self.bg_color, outline="")
            
            # Draw progress
            progress_width = ((self.value - self.from_) / (self.to - self.from_)) * self.winfo_reqwidth()
            self.create_rounded_rect(0, track_y - 3, progress_width, track_y + 3, 
                                   self.border_radius // 2, fill=self.fg_color, outline="")
            
            # Draw handle
            handle_x = progress_width
            handle_y = track_y
            self.create_oval(handle_x - self.handle_size//2, handle_y - self.handle_size//2,
                           handle_x + self.handle_size//2, handle_y + self.handle_size//2,
                           fill=self.handle_color, outline=self.handle_border_color, 
                           width=self.handle_border_width, tags="handle")
        
    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        points = []
        for x, y in [(x1, y1 + radius), (x1, y1), (x1 + radius, y1), 
                     (x2 - radius, y1), (x2, y1), (x2, y1 + radius),
                     (x2, y2 - radius), (x2, y2), (x2 - radius, y2),
                     (x1 + radius, y2), (x1, y2), (x1, y2 - radius)]:
            points.extend([x, y])
        return self.create_polygon(points, smooth=True, **kwargs)
    
    def on_click(self, event):
        self.dragging = True
        self.update_value(event)
    
    def on_drag(self, event):
        if self.dragging:
            self.update_value(event)
    
    def on_release(self, event):
        self.dragging = False
    
    def update_value(self, event):
        if self.orientation == "horizontal":
            ratio = event.x / self.winfo_width()
        else:
            ratio = event.y / self.winfo_height()
        
        ratio = max(0, min(1, ratio))
        self.value = self.from_ + ratio * (self.to - self.from_)
        
        self.draw_slider()
        
        if self.command:
            self.command(self.value)
    
    def get(self):
        return self.value
    
    def set(self, value):
        self.value = max(self.from_, min(self.to, value))
        self.draw_slider()
