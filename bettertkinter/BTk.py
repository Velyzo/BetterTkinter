import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class BTk(tk.Tk):
    def __init__(self, title="BetterTkinter", icon_path=None, theme="light", resizable=True, transparent=False,
                 always_on_top=False, shadow=True, custom_titlebar=True, min_size=(300, 200), max_size=None,
                 on_close=None, on_resize=None, on_move=None, shortcuts=None, *args, **kwargs):
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