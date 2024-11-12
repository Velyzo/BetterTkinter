import tkinter as tk

class BTkButton(tk.Canvas):
    def __init__(self, parent, text="", bg_color="#0078D7", fg_color="white", hover_color="#005A9E", 
                 rounded_radius=20, width=100, height=40, command=None):
        super().__init__(parent, height=height, width=width, bg=parent['bg'], highlightthickness=0)
        
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.fg_color = fg_color
        self.rounded_radius = rounded_radius
        self.width = width
        self.height = height
        self.command = command

        self.draw_button(text)

        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def draw_button(self, text):
        radius = self.rounded_radius
        self.create_oval(0, 0, radius * 2, radius * 2, fill=self.bg_color, outline="", tags="button_bg")
        self.create_oval(self.width - radius * 2, 0, self.width, radius * 2, fill=self.bg_color, outline="", tags="button_bg")
        self.create_oval(0, self.height - radius * 2, radius * 2, self.height, fill=self.bg_color, outline="", tags="button_bg")
        self.create_oval(self.width - radius * 2, self.height - radius * 2, self.width, self.height, fill=self.bg_color, outline="", tags="button_bg")

        self.create_rectangle(radius, 0, self.width - radius, self.height, fill=self.bg_color, outline="", tags="button_bg")
        self.create_rectangle(0, radius, self.width, self.height - radius, fill=self.bg_color, outline="", tags="button_bg")

        self.text_id = self.create_text(self.width / 2, self.height / 2, text=text, fill=self.fg_color, font=("Helvetica", 12, "bold"))

    def on_click(self, event):
        if self.command:
            self.command()

    def on_enter(self, event):
        self.itemconfig("button_bg", fill=self.hover_color)

    def on_leave(self, event):
        self.itemconfig("button_bg", fill=self.bg_color)

if __name__ == "__main__":
    def sample_command():
        print("Button clicked!")

    root = tk.Tk()
    root.title("BetterTkinter")

    button1 = BTkButton(root, text="Button 1", bg_color="#FF6347", hover_color="#FF4500", rounded_radius=25, width=120, height=50, command=sample_command)
    button1.pack(pady=10)

    button2 = BTkButton(root, text="Button 2", bg_color="#4CAF50", fg_color="black", hover_color="#388E3C", rounded_radius=30, width=60, height=30, command=sample_command)
    button2.pack(pady=10)

    button3 = BTkButton(root, text="Button 3", bg_color="#0078D7", hover_color="#005A9E", rounded_radius=40, width=160, height=70, command=sample_command)
    button3.pack(pady=10)

    root.mainloop()
