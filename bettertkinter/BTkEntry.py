import tkinter as tk

class BTkEntry(tk.Entry):
    def __init__(self, parent, font=("Helvetica", 12), fg="#222", bg=None, show=None, **kwargs):
        super().__init__(parent, font=font, fg=fg, bg=bg or parent['bg'], show=show, **kwargs)
