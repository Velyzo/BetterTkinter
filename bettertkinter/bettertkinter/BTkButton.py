import tkinter as tk

class BTkButton(tk.Canvas):
    def __init__(self, parent, text="", bg_color="#0078D7", fg_color="white", hover_color="#005A9E", 
                 hover_transition=0.1, rounded_radius=15, width=100, height=40, command=None):
        tk.Canvas.__init__(self, parent, height=height, width=width, bg=parent['bg'], highlightthickness=0)
        
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.hover_color = hover_color
        self.rounded_radius = rounded_radius
        self.width = width
        self.height = height
        self.command = command

        self.create_rounded_rectangle(0, 0, width, height, radius=rounded_radius, fill=bg_color, tags="button_bg")
        self.text_id = self.create_text(width / 2, height / 2, text=text, fill=fg_color, font=("Helvetica", 12, "bold"))

        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1,
            x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2,
            x2 - radius, y2, x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2,
            x1, y2 - radius, x1, y2 - radius, x1, y1 + radius, x1, y1 + radius, x1, y1
        ]
        return self.create_polygon(points, **kwargs, smooth=True)

    def on_click(self, event):
        if self.command:
            self.command()

    def on_enter(self, event):
        self.itemconfig("button_bg", fill=self.hover_color)
        self.itemconfig(self.text_id, fill=self.bg_color)

    def on_leave(self, event):
        self.itemconfig("button_bg", fill=self.bg_color)
        self.itemconfig(self.text_id, fill=self.fg_color)

if __name__ == "__main__":
    def sample_command():
        print("Button clicked!")

    root = tk.Tk()
    root.title("CustomButton Test")

    button1 = BTkButton(root, text="Button 1", bg_color="#FF6347", hover_color="#FF4500", rounded_radius=10, width=120, height=50, command=sample_command)
    button1.pack(pady=10)

    button2 = BTkButton(root, text="Button 2", bg_color="#4CAF50", fg_color="black", hover_color="#388E3C", rounded_radius=20, width=60, height=30, command=sample_command)
    button2.pack(pady=10)

    button3 = BTkButton(root, text="Button 3", bg_color="#0078D7", hover_color="#005A9E", rounded_radius=30, width=160, height=70, command=sample_command)
    button3.pack(pady=10)

    root.mainloop()
