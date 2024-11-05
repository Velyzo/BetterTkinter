import tkinter as tk
from tkinter import Canvas

class BTkFrame(tk.Frame):
    def __init__(self, parent, radius=0, width=100, height=100, color="#005A9E", border=False, border_color="#FF4500", border_thick=0, border_bg_color="#000000"):
        super().__init__(parent)
        self.radius = radius
        self.width = width
        self.height = height
        self.color = color
        self.border = border
        self.border_color = border_color
        self.border_thick = border_thick
        self.border_bg_color = border_bg_color

        # Create a canvas to draw the frame
        self.canvas = Canvas(self, width=self.width, height=self.height, highlightthickness=0, bg=self.border_bg_color)
        self.canvas.pack()

        # Draw the rounded rectangle frame
        self.draw_rounded_rect()

    def draw_rounded_rect(self):
        if self.border:
            # Draw the border with a larger rounded rectangle
            self.create_rounded_rectangle(
                self.border_thick, self.border_thick,
                self.width - self.border_thick,
                self.height - self.border_thick,
                radius=self.radius + self.border_thick,
                fill=self.border_color,
                outline=self.border_color
            )

        # Draw the inner rectangle for the actual frame
        self.create_rounded_rectangle(
            self.border_thick, self.border_thick,
            self.width - self.border_thick,
            self.height - self.border_thick,
            radius=self.radius,
            fill=self.color,
            outline=self.color
        )

    # Define create_rounded_rectangle within the class
    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        # Calculate the points for the rounded corners
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1, 
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        # Draw the rounded rectangle as a polygon on the canvas
        return self.canvas.create_polygon(points, **kwargs, smooth=True)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Frame Test")

    # Create an instance of BTkFrame with border and rounded corners
    frame1 = BTkFrame(root, radius=20, width=200, height=100, color="#005A9E", border=True, border_color="#FF4500", border_thick=5)
    frame1.pack()
    
    frame2 = BTkFrame(root, radius=20, width=200, height=100, color="#005A9E", border=True, border_color="#FF4500", border_thick=5)
    frame2.pack()

    root.mainloop()
