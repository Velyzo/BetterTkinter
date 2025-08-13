import tkinter as tk
from tkinter import messagebox

class BTkDialog:
    @staticmethod
    def info(title, message):
        messagebox.showinfo(title, message)

    @staticmethod
    def warning(title, message):
        messagebox.showwarning(title, message)

    @staticmethod
    def error(title, message):
        messagebox.showerror(title, message)
