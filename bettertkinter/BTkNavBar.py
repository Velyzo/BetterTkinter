import tkinter as tk
from PIL import Image, ImageTk

class BTkNavBar(tk.Frame):
    def __init__(self, parent, items=None, position="top", bg=None, fg=None, font=None,
                 height=None, icon_size=None, active_bg=None, active_fg=None, border=None,
                 border_color=None, border_width=None, callback=None, style=None, spacing=None, **kwargs):
        # Allow full customization, fallback to defaults if not provided
        bg = bg if bg is not None else "#0078D7"
        fg = fg if fg is not None else "white"
        font = font if font is not None else ("Segoe UI", 12)
        height = height if height is not None else 40
        icon_size = icon_size if icon_size is not None else (24, 24)
        active_bg = active_bg if active_bg is not None else "#005A9E"
        active_fg = active_fg if active_fg is not None else "#FFD700"
        border = border if border is not None else False
        border_color = border_color if border_color is not None else "#222"
        border_width = border_width if border_width is not None else 2
        style = style if style is not None else "flat"
        spacing = spacing if spacing is not None else 10
        super().__init__(parent, bg=bg, height=height, **kwargs)
        self.items = items or []
        self.position = position
        self.bg = bg
        self.fg = fg
        self.font = font
        self.height = height
        self.icon_size = icon_size
        self.active_bg = active_bg
        self.active_fg = active_fg
        self.border = border
        self.border_color = border_color
        self.border_width = border_width
        self.callback = callback
        self.style = style
        self.spacing = spacing
        self.active_index = None
        self._icons = []
        self._buttons = []
        self._build_navbar()

    def _build_navbar(self):
        if self.border:
            self.config(highlightbackground=self.border_color, highlightthickness=self.border_width)
        side = "top" if self.position in ["top", "bottom"] else "left"
        self.pack(side=side, fill="x" if side in ["top", "bottom"] else "y")
        for idx, item in enumerate(self.items):
            icon_img = None
            if item.get("icon"):
                img = Image.open(item["icon"]).resize(self.icon_size)
                icon_img = ImageTk.PhotoImage(img)
                self._icons.append(icon_img)
            btn = tk.Button(self, text=item.get("text", ""), image=icon_img, compound="left" if icon_img else None,
                            font=self.font, bg=self.bg, fg=self.fg, bd=0 if self.style=="flat" else 2,
                            activebackground=self.active_bg, activeforeground=self.active_fg,
                            padx=self.spacing, pady=5,
                            command=lambda i=idx: self._on_item_click(i))
            btn.pack(side="left" if self.position in ["top", "bottom"] else "top", padx=self.spacing)
            self._buttons.append(btn)

    def _on_item_click(self, idx):
        self.active_index = idx
        for i, btn in enumerate(self._buttons):
            if i == idx:
                btn.config(bg=self.active_bg, fg=self.active_fg)
            else:
                btn.config(bg=self.bg, fg=self.fg)
        if self.callback:
            self.callback(idx, self.items[idx])
