import tkinter as tk

class CustomButton(tk.Canvas):
    def __init__(self, parent, text="", bg_color="#0078D7", fg_color="white", radius=15, command=None):
        tk.Canvas.__init__(self, parent, height=2*radius, width=100, bg=parent['bg'], highlightthickness=0)
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.radius = radius
        self.command = command

        self.create_rounded_rectangle(0, 0, 100, 2*radius, radius=radius, fill=bg_color)
        self.text_id = self.create_text(50, radius, text=text, fill=fg_color, font=("Helvetica", 12, "bold"))

        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1,
                  x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2,
                  x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2,
                  x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
        return self.create_polygon(points, **kwargs, smooth=True)

    def on_click(self, event):
        if self.command:
            self.command()

    def on_enter(self, event):
        self.itemconfig(self.text_id, fill=self.bg_color)
        self.itemconfig(self.find_withtag("current"), fill=self.fg_color)

    def on_leave(self, event):
        self.itemconfig(self.text_id, fill=self.fg_color)
        self.itemconfig(self.find_withtag("current"), fill=self.bg_color)
