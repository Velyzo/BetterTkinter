class BTkTheme:
    THEMES = {
        "light": {
            "bg": "#f8f8f8",
            "fg": "#222",
            "accent": "#0078D7"
        },
        "dark": {
            "bg": "#222",
            "fg": "#f8f8f8",
            "accent": "#FF6347"
        }
    }

    @staticmethod
    def apply(widget, theme="light"):
        t = BTkTheme.THEMES.get(theme, BTkTheme.THEMES["light"])
        widget.configure(bg=t["bg"])
        if hasattr(widget, "children"):
            for child in widget.children.values():
                try:
                    child.configure(bg=t["bg"], fg=t["fg"])
                except Exception:
                    pass
