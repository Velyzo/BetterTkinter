import tkinter as tk
from bettertkinter.BTk import BTk
from bettertkinter.BTkButton import BTkButton
from bettertkinter.BTkFrame import BTkFrame
from bettertkinter.BTkLabel import BTkLabel
from bettertkinter.BTkEntry import BTkEntry
from bettertkinter.BTkDialog import BTkDialog
from bettertkinter.BTkTooltip import BTkTooltip
from bettertkinter.BTkTheme import BTkTheme
from bettertkinter.BTkNavBar import BTkNavBar

class DemoApp(BTk):
    def __init__(self):
        super().__init__(title="BetterTkinter Demo", theme="light", resizable=True)
        self.geometry("800x500")
        BTkTheme.apply(self, "light")

        # Navigation bar demo
        nav_items = [
            {"text": "Home", "icon": None},
            {"text": "Settings", "icon": None},
            {"text": "Profile", "icon": None},
            {"text": "Help", "icon": None}
        ]
        nav_options = {
            "position": "top",
            "bg": "#0078D7",
            "fg": "white",
            "active_bg": "#005A9E",
            "active_fg": "#FFD700",
            "border": True,
            "border_color": "#222",
            "border_width": 2,
            "callback": self.on_nav,
            "font": ("Segoe UI", 13),
            "height": 48,
            "icon_size": (28, 28),
            "style": "flat",
            "spacing": 16
        }
        self.navbar = BTkNavBar(self, items=nav_items, **nav_options)

        frame = BTkFrame(self, radius=30, width=600, height=350, color="#f0f4fa", border=True, border_color="#0078D7", border_thick=4, border_bg_color="#e0e0e0")
        frame.pack(pady=60)

        label = BTkLabel(frame, text="Welcome to BetterTkinter!", font=("Helvetica", 20, "bold"), fg="#0078D7")
        label.pack(pady=16)

        entry = BTkEntry(frame, font=("Consolas", 14), fg="#222", bg="#fff")
        entry.pack(pady=12)
        BTkTooltip(entry, "Type something here!")

        def on_button():
            BTkDialog.info("Info", f"You typed: {entry.get()}")

        button = BTkButton(frame, text="Show Dialog", command=on_button, bg_color="#0078D7", fg_color="white", hover_color="#005A9E", rounded_radius=24, width=180, height=54, font=("Segoe UI", 14, "bold"), border_color="#222", border_width=2, shadow=True, tooltip="Click to show your input!")
        button.pack(pady=18)

    def on_nav(self, idx, item):
        BTkDialog.info("Navigation", f"Selected: {item['text']}")

if __name__ == "__main__":
    app = DemoApp()
    app.mainloop()
