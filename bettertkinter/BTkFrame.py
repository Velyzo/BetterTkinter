import tkinter as tk

class BTkFrame(tk.Frame):
    def __init__(self, parent, radius=25, width=100, height=100, color="#005A9E", 
                 border=False, border_color="#FF4500", border_thick=0, border_bg_color="#000000"):
        super().__init__(parent)
        
        self.radius = radius
        self.width = width
        self.height = height
        self.color = color
        self.border = border
        self.border_color = border_color
        self.border_thick = border_thick
        self.border_bg_color = border_bg_color

        self.canvas = tk.Canvas(self, width=self.width, height=self.height, highlightthickness=0, bg=self.border_bg_color)
        self.canvas.pack()

        self.draw_rounded_rect()

    def draw_rounded_rect(self):
        if self.border:
            self.create_rounded_rectangle(
                self.border_thick, self.border_thick,
                self.width - self.border_thick,
                self.height - self.border_thick,
                radius=self.radius + self.border_thick,
                fill=self.border_color,
                outline=self.border_color
            )

        self.create_rounded_rectangle(
            self.border_thick, self.border_thick,
            self.width - self.border_thick,
            self.height - self.border_thick,
            radius=self.radius,
            fill=self.color,
            outline=self.color
        )

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        self.canvas.create_oval(x1, y1, x1 + radius*2, y1 + radius*2, **kwargs)
        self.canvas.create_oval(x2 - radius*2, y1, x2, y1 + radius*2, **kwargs)
        self.canvas.create_oval(x1, y2 - radius*2, x1 + radius*2, y2, **kwargs)
        self.canvas.create_oval(x2 - radius*2, y2 - radius*2, x2, y2, **kwargs)
        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("BetterTkinter")

    frame1 = BTkFrame(root, radius=25, width=200, height=100, color="#005A9E", border=True, border_color="#FF4500", border_thick=5)
    frame1.pack(pady=10)

    root.mainloop()
