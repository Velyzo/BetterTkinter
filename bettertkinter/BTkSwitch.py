import tkinter as tk

class BTkSwitch(tk.Frame):
    def __init__(self, parent, variable=None, command=None, width=50, height=25,
                 bg_color_off="#CCCCCC", bg_color_on="#0078D7", 
                 handle_color="#FFFFFF", border_width=1, border_color="#999999",
                 animated=True, **kwargs):
        super().__init__(parent, bg=parent.cget('bg'), **kwargs)
        
        self.variable = variable or tk.BooleanVar()
        self.command = command
        self.width = width
        self.height = height
        self.bg_color_off = bg_color_off
        self.bg_color_on = bg_color_on
        self.handle_color = handle_color
        self.border_width = border_width
        self.border_color = border_color
        self.animated = animated
        
        self.animation_steps = 0
        self.animation_target = 0
        
        self.canvas = tk.Canvas(self, width=width, height=height, 
                              bg=parent.cget('bg'), highlightthickness=0)
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.toggle)
        self.variable.trace_add("write", self.on_variable_change)
        
        self.draw_switch()
    
    def draw_switch(self):
        self.canvas.delete("all")
        
        radius = self.height // 2
        
        # Get current state and position
        is_on = self.variable.get()
        if self.animated and self.animation_steps > 0:
            # Animate between positions
            progress = 1 - (self.animation_steps / 10)
            if is_on:
                handle_x = radius + progress * (self.width - 2 * radius)
                bg_color = self.interpolate_color(self.bg_color_off, self.bg_color_on, progress)
            else:
                handle_x = radius + (1 - progress) * (self.width - 2 * radius)
                bg_color = self.interpolate_color(self.bg_color_on, self.bg_color_off, progress)
        else:
            # Static position
            if is_on:
                handle_x = self.width - radius
                bg_color = self.bg_color_on
            else:
                handle_x = radius
                bg_color = self.bg_color_off
        
        # Draw background track
        self.canvas.create_oval(0, 0, self.height, self.height, 
                              fill=bg_color, outline=self.border_color, 
                              width=self.border_width)
        self.canvas.create_oval(self.width - self.height, 0, self.width, self.height,
                              fill=bg_color, outline=self.border_color, 
                              width=self.border_width)
        self.canvas.create_rectangle(radius, self.border_width, 
                                   self.width - radius, self.height - self.border_width,
                                   fill=bg_color, outline="")
        
        # Draw handle
        handle_radius = radius - 3
        self.canvas.create_oval(handle_x - handle_radius, radius - handle_radius,
                              handle_x + handle_radius, radius + handle_radius,
                              fill=self.handle_color, outline="#DDDDDD", width=1)
    
    def interpolate_color(self, color1, color2, factor):
        """Interpolate between two hex colors"""
        if color1.startswith('#'):
            color1 = color1[1:]
        if color2.startswith('#'):
            color2 = color2[1:]
        
        r1, g1, b1 = int(color1[0:2], 16), int(color1[2:4], 16), int(color1[4:6], 16)
        r2, g2, b2 = int(color2[0:2], 16), int(color2[2:4], 16), int(color2[4:6], 16)
        
        r = int(r1 + (r2 - r1) * factor)
        g = int(g1 + (g2 - g1) * factor)
        b = int(b1 + (b2 - b1) * factor)
        
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def toggle(self, event=None):
        self.variable.set(not self.variable.get())
        if self.command:
            self.command()
    
    def on_variable_change(self, *args):
        if self.animated:
            self.animation_steps = 10
            self.animate_switch()
        else:
            self.draw_switch()
    
    def animate_switch(self):
        if self.animation_steps > 0:
            self.animation_steps -= 1
            self.draw_switch()
            self.after(20, self.animate_switch)
