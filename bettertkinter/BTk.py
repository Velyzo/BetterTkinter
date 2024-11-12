import tkinter as tk

class BTk(tk.Tk):
    def __init__(self, title="BetterTkinter", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(title)
        
if __name__ == "__main__":
    app = BTk()
    app.geometry("400x300")
    app.mainloop()