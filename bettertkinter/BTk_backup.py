import tkinter as tk
from tkinter import ttk
import json
import os
import math
import threading
import time
from PIL import Image, ImageTk, ImageDraw, ImageFilter

# Constants for better code quality
DEFAULT_FONT = "Segoe UI"
TITLEBAR_HEIGHT = 40
CORNER_RADIUS = 12
SHADOW_BLUR = 10

class BTkWindowConfig:
    """Configuration class for BTk window settings"""
    def __init__(self, **kwargs):
        # Basic window settings
        self.title = kwargs.get('title', "BetterTkinter")
        self.icon_path = kwargs.get('icon_path')
        self.theme = kwargs.get('theme', "light")
        self.resizable = kwargs.get('resizable', True)
        self.transparent = kwargs.get('transparent', False)
        self.always_on_top = kwargs.get('always_on_top', False)
        self.min_size = kwargs.get('min_size', (300, 200))
        self.max_size = kwargs.get('max_size')
        
        # Advanced styling
        self.window_style = kwargs.get('window_style', "modern")
        self.border_radius = kwargs.get('border_radius', 15)
        self.border_width = kwargs.get('border_width', 2)
        self.border_color = kwargs.get('border_color', "#E0E0E0")
        self.rounded_corners = kwargs.get('rounded_corners', True)
        self.corner_radius = kwargs.get('corner_radius', CORNER_RADIUS)
        
        # Titlebar settings
        self.custom_titlebar = kwargs.get('custom_titlebar', True)
        self.titlebar_height = kwargs.get('titlebar_height', TITLEBAR_HEIGHT)
        self.titlebar_color = kwargs.get('titlebar_color')
        self.titlebar_text_color = kwargs.get('titlebar_text_color')
        self.titlebar_font = kwargs.get('titlebar_font', (DEFAULT_FONT, 11, "bold"))
        
        # Background effects
        self.background_gradient = kwargs.get('background_gradient')
        self.background_image = kwargs.get('background_image')
        self.background_blur = kwargs.get('background_blur', 0)
        self.glass_effect = kwargs.get('glass_effect', False)
        self.acrylic_blur = kwargs.get('acrylic_blur', 20)
        
        # Animation settings
        self.animations_enabled = kwargs.get('animations_enabled', True)
        self.fade_in_duration = kwargs.get('fade_in_duration', 0.3)
        self.resize_smooth = kwargs.get('resize_smooth', True)
        self.startup_position = kwargs.get('startup_position', "center")
        self.startup_animation = kwargs.get('startup_animation', "fade_in")
        self.close_animation = kwargs.get('close_animation', "fade_out")
        
        # Window controls
        self.custom_controls = kwargs.get('custom_controls', True)
        self.control_style = kwargs.get('control_style', "windows11")
        self.control_colors = kwargs.get('control_colors', {})
        
        # Shadow and effects
        self.shadow = kwargs.get('shadow', True)
        self.drop_shadow_enabled = kwargs.get('drop_shadow_enabled', True)
        self.drop_shadow_blur = kwargs.get('drop_shadow_blur', SHADOW_BLUR)
        self.drop_shadow_offset = kwargs.get('drop_shadow_offset', (2, 2))
        self.window_effects = kwargs.get('window_effects', [])
        
        # Callbacks
        self.on_close = kwargs.get('on_close')
        self.on_resize = kwargs.get('on_resize')
        self.on_move = kwargs.get('on_move')
        self.shortcuts = kwargs.get('shortcuts', {})
        super().__init__(*args, **kwargs)
        self.title(title)
        self.resizable(resizable, resizable)
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._on_close_callback = on_close
        self._on_resize_callback = on_resize
        self._on_move_callback = on_move
        self._theme = theme
        self._custom_titlebar = custom_titlebar
        self._shadow = shadow
        self._transparent = transparent
        self._always_on_top = always_on_top
        self._shortcuts = shortcuts or {}
        self._min_size = min_size
        self._max_size = max_size

        self.minsize(*self._min_size)
        if self._max_size:
            self.maxsize(*self._max_size)
        if self._always_on_top:
            self.attributes("-topmost", True)
        if self._transparent:
            self.attributes("-alpha", 0.9)
        if icon_path:
            try:
                img = Image.open(icon_path)
                self.iconphoto(False, ImageTk.PhotoImage(img))
            except Exception:
                pass

        self._init_theme()
        if self._custom_titlebar:
            self._init_titlebar(title)
        if self._shadow:
            self._init_shadow()

        self.bind("<Configure>", self._on_configure)
        self.bind("<Key>", self._on_key)

    def _init_theme(self):
        style = ttk.Style(self)
        if self._theme == "dark":
            self.configure(bg="#222")
            style.theme_use("clam")
            style.configure("TFrame", background="#222")
            style.configure("TLabel", background="#222", foreground="#f8f8f8")
        else:
            self.configure(bg="#f8f8f8")
            style.theme_use("clam")
            style.configure("TFrame", background="#f8f8f8")
            style.configure("TLabel", background="#222", foreground="#0078D7")

    def switch_theme(self, theme):
        self._theme = theme
        self._init_theme()

    def _init_titlebar(self, title):
        self.overrideredirect(True)
        self._titlebar = tk.Frame(self, bg="#0078D7", relief="raised", bd=0, height=32)
        self._titlebar.pack(fill="x", side="top")
        self._title_label = tk.Label(self._titlebar, text=title, bg="#0078D7", fg="white", font=("Segoe UI", 12, "bold"))
        self._title_label.pack(side="left", padx=10)
        self._btn_close = tk.Button(self._titlebar, text="✕", bg="#0078D7", fg="white", bd=0, command=self._on_close, font=("Segoe UI", 12))
        self._btn_close.pack(side="right", padx=5)
        self._btn_min = tk.Button(self._titlebar, text="━", bg="#0078D7", fg="white", bd=0, command=self.iconify, font=("Segoe UI", 12))
        self._btn_min.pack(side="right", padx=5)
        self._btn_max = tk.Button(self._titlebar, text="▢", bg="#0078D7", fg="white", bd=0, command=self._toggle_maximize, font=("Segoe UI", 12))
        self._btn_max.pack(side="right", padx=5)
        self._titlebar.bind("<Button-1>", self._start_move)
        self._titlebar.bind("<B1-Motion>", self._on_move)
        self._titlebar.bind("<Double-Button-1>", self._toggle_maximize)

    def _init_shadow(self):
        # Placeholder for window shadow (platform-dependent)
        pass

    def _on_close(self):
        if self._on_close_callback:
            self._on_close_callback()
        self.destroy()

    def _on_configure(self, event):
        if self._on_resize_callback:
            self._on_resize_callback(event)

    def _on_key(self, event):
        if event.keysym in self._shortcuts:
            self._shortcuts[event.keysym]()

    def _start_move(self, event):
        self._x = event.x
        self._y = event.y

    def _on_move(self, event):
        x = self.winfo_pointerx() - self._x
        y = self.winfo_pointery() - self._y
        self.geometry(f"+{x}+{y}")
        if self._on_move_callback:
            self._on_move_callback(event)

    def _toggle_maximize(self, event=None):
        if self.state() == "zoomed":
            self.state("normal")
        else:
            self.state("zoomed")

if __name__ == "__main__":
    def on_close():
        print("Window closed!")

    def on_resize(event):
        print(f"Resized to {event.width}x{event.height}")

    def on_move(event):
        print("Window moved!")

    app = BTk(title="BetterTkinter", theme="dark", icon_path=None, resizable=True, transparent=False,
              always_on_top=False, shadow=True, custom_titlebar=True, min_size=(400, 300),
              on_close=on_close, on_resize=on_resize, on_move=on_move,
              shortcuts={"Escape": lambda: print("Escape pressed!")})
    app.geometry("600x400")
    app.mainloop()