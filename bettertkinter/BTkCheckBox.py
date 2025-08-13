import tkinter as tk

class BTkCheckBox(tk.Frame):
    def __init__(self, parent, text="", variable=None, command=None, 
                 fg_color="#0078D7", bg_color="#FFFFFF", check_color="#FFFFFF",
                 border_color="#CCCCCC", border_width=2, size=20, 
                 font=("Segoe UI", 11), **kwargs):
        super().__init__(parent, bg=parent.cget('bg'), **kwargs)
        
        self.text = text
        self.variable = variable or tk.BooleanVar()
        self.command = command
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.check_color = check_color
        self.border_color = border_color
        self.border_width = border_width
        self.size = size
        self.font = font
        
        self.create_widgets()
        
    def create_widgets(self):
        # Checkbox canvas
        self.checkbox_canvas = tk.Canvas(self, width=self.size, height=self.size,
                                       bg=self.master.cget('bg'), highlightthickness=0)
        self.checkbox_canvas.pack(side=tk.LEFT, padx=(0, 8))
        
        # Text label
        if self.text:
            self.label = tk.Label(self, text=self.text, font=self.font,
                                bg=self.master.cget('bg'), fg="#333333")
            self.label.pack(side=tk.LEFT)
            self.label.bind("<Button-1>", self.toggle)
        
        self.checkbox_canvas.bind("<Button-1>", self.toggle)
        self.draw_checkbox()
        
        # Bind variable trace
        self.variable.trace_add("write", self.on_variable_change)
    
    def draw_checkbox(self):
        self.checkbox_canvas.delete("all")
        
        # Draw checkbox background
        if self.variable.get():
            fill_color = self.fg_color
            border_color = self.fg_color
        else:
            fill_color = self.bg_color
            border_color = self.border_color
        
        # Rounded square
        self.checkbox_canvas.create_rounded_rect(0, 0, self.size, self.size, 4,
                                                fill=fill_color, outline=border_color,
                                                width=self.border_width)
        
        # Draw checkmark
        if self.variable.get():
            # Draw checkmark lines
            points = [
                self.size * 0.2, self.size * 0.5,
                self.size * 0.4, self.size * 0.7,
                self.size * 0.8, self.size * 0.3
            ]
            self.checkbox_canvas.create_line(points, fill=self.check_color, 
                                           width=2, capstyle=tk.ROUND)
    
    def toggle(self, event=None):
        self.variable.set(not self.variable.get())
        if self.command:
            self.command()
    
    def on_variable_change(self, *args):
        self.draw_checkbox()

# Add method to Canvas class for rounded rectangles
def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
    points = []
    for x, y in [(x1, y1 + radius), (x1, y1), (x1 + radius, y1), 
                 (x2 - radius, y1), (x2, y1), (x2, y1 + radius),
                 (x2, y2 - radius), (x2, y2), (x2 - radius, y2),
                 (x1 + radius, y2), (x1, y2), (x1, y2 - radius)]:
        points.extend([x, y])
    return self.create_polygon(points, smooth=True, **kwargs)

tk.Canvas.create_rounded_rect = create_rounded_rect
