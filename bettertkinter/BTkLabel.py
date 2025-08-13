import tkinter as tk

class BTkLabel(tk.Label):
    def __init__(self, parent, text="", font=("Helvetica", 12), fg="#222", bg=None, **kwargs):
        super().__init__(parent, text=text, font=font, fg=fg, bg=bg or parent['bg'], **kwargs)
