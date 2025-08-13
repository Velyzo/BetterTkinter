import tkinter as tk
from PIL import Image, ImageTk
import threading

class BTkButton(tk.Canvas):
    def __init__(self, parent, text="", bg_color="#0078D7", fg_color="white", hover_color="#005A9E",
                 rounded_radius=20, width=100, height=40, command=None, font=("Helvetica", 12, "bold"),
                 icon_path=None, icon_side="left", icon_size=(20, 20), border_color=None, border_width=0,
                 shadow=False, shadow_color="#888", shadow_offset=(2, 2), gradient=None,
                 disabled=False, loading=False, tooltip=None, shortcut=None,
                 on_mouse_enter=None, on_mouse_leave=None, on_mouse_down=None, on_mouse_up=None,
                 animation=None, **kwargs):
        super().__init__(parent, height=height, width=width, bg=parent['bg'], highlightthickness=0, **kwargs)

        self.bg_color = bg_color
        self.hover_color = hover_color
        self.fg_color = fg_color
        self.rounded_radius = rounded_radius
        self.width = width
        self.height = height
        self.command = command
        self.font = font
        self.icon_path = icon_path
        self.icon_side = icon_side
        self.icon_size = icon_size
        self.border_color = border_color
        self.border_width = border_width
        self.shadow = shadow
        self.shadow_color = shadow_color
        self.shadow_offset = shadow_offset
        self.gradient = gradient
        self.disabled = disabled
        self.loading = loading
        self.tooltip = tooltip
        self.shortcut = shortcut
        self.on_mouse_enter = on_mouse_enter
        self.on_mouse_leave = on_mouse_leave
        self.on_mouse_down = on_mouse_down
        self.on_mouse_up = on_mouse_up
        self.animation = animation
        self.text = text

        self._icon_img = None
        self._loading_thread = None
        self._is_hovered = False

        self.draw_button()

        self.bind("<Button-1>", self.on_click)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<ButtonPress-1>", self.on_mouse_down_event)
        self.bind("<ButtonRelease-1>", self.on_mouse_up_event)
        self.bind_all("<Key>", self.on_key_event)

        if self.tooltip:
            self._tip = None
            self.bind("<Enter>", self.show_tooltip)
            self.bind("<Leave>", self.hide_tooltip)

        if self.loading:
            self.start_loading()

    def draw_button(self):
        self.delete("all")
        radius = self.rounded_radius
        # Shadow
        if self.shadow:
            self.create_oval(self.shadow_offset[0], self.shadow_offset[1], radius * 2 + self.shadow_offset[0], radius * 2 + self.shadow_offset[1], fill=self.shadow_color, outline="", tags="shadow")
            self.create_oval(self.width - radius * 2 + self.shadow_offset[0], self.shadow_offset[1], self.width + self.shadow_offset[0], radius * 2 + self.shadow_offset[1], fill=self.shadow_color, outline="", tags="shadow")
            self.create_oval(self.shadow_offset[0], self.height - radius * 2 + self.shadow_offset[1], radius * 2 + self.shadow_offset[0], self.height + self.shadow_offset[1], fill=self.shadow_color, outline="", tags="shadow")
            self.create_oval(self.width - radius * 2 + self.shadow_offset[0], self.height - radius * 2 + self.shadow_offset[1], self.width + self.shadow_offset[0], self.height + self.shadow_offset[1], fill=self.shadow_color, outline="", tags="shadow")
            self.create_rectangle(radius + self.shadow_offset[0], self.shadow_offset[1], self.width - radius + self.shadow_offset[0], self.height + self.shadow_offset[1], fill=self.shadow_color, outline="", tags="shadow")
            self.create_rectangle(self.shadow_offset[0], radius + self.shadow_offset[1], self.width + self.shadow_offset[0], self.height - radius + self.shadow_offset[1], fill=self.shadow_color, outline="", tags="shadow")

        # Border
        if self.border_color and self.border_width > 0:
            self.create_oval(0, 0, radius * 2, radius * 2, fill=self.border_color, outline="", width=self.border_width, tags="border")
            self.create_oval(self.width - radius * 2, 0, self.width, radius * 2, fill=self.border_color, outline="", width=self.border_width, tags="border")
            self.create_oval(0, self.height - radius * 2, radius * 2, self.height, fill=self.border_color, outline="", width=self.border_width, tags="border")
            self.create_oval(self.width - radius * 2, self.height - radius * 2, self.width, self.height, fill=self.border_color, outline="", width=self.border_width, tags="border")
            self.create_rectangle(radius, 0, self.width - radius, self.height, fill=self.border_color, outline="", width=self.border_width, tags="border")
            self.create_rectangle(0, radius, self.width, self.height - radius, fill=self.border_color, outline="", width=self.border_width, tags="border")

        # Gradient or background
        fill_color = self.bg_color if not self.gradient else self._draw_gradient()
        self.create_oval(0, 0, radius * 2, radius * 2, fill=fill_color, outline="", tags="button_bg")
        self.create_oval(self.width - radius * 2, 0, self.width, radius * 2, fill=fill_color, outline="", tags="button_bg")
        self.create_oval(0, self.height - radius * 2, radius * 2, self.height, fill=fill_color, outline="", tags="button_bg")
        self.create_oval(self.width - radius * 2, self.height - radius * 2, self.width, self.height, fill=fill_color, outline="", tags="button_bg")
        self.create_rectangle(radius, 0, self.width - radius, self.height, fill=fill_color, outline="", tags="button_bg")
        self.create_rectangle(0, radius, self.width, self.height - radius, fill=fill_color, outline="", tags="button_bg")

        # Icon
        icon_offset = 0
        if self.icon_path:
            img = Image.open(self.icon_path).resize(self.icon_size)
            self._icon_img = ImageTk.PhotoImage(img)
            if self.icon_side == "left":
                icon_offset = self.icon_size[0] // 2 + 10
                self.create_image(icon_offset, self.height // 2, image=self._icon_img)
            elif self.icon_side == "right":
                icon_offset = self.width - self.icon_size[0] // 2 - 10
                self.create_image(icon_offset, self.height // 2, image=self._icon_img)

        # Text
        text_x = self.width // 2
        if self.icon_path and self.icon_side == "left":
            text_x += self.icon_size[0] // 2
        elif self.icon_path and self.icon_side == "right":
            text_x -= self.icon_size[0] // 2
        self.text_id = self.create_text(text_x, self.height // 2, text=self.text, fill=self.fg_color, font=self.font)

        # Disabled state
        if self.disabled:
            self.itemconfig("button_bg", fill="#cccccc")
            self.itemconfig(self.text_id, fill="#888888")
            self.unbind("<Button-1>")

        # Loading spinner
        if self.loading:
            self._draw_spinner()

    def _draw_gradient(self):
        # Placeholder for gradient fill (could use PIL for advanced gradients)
        return self.bg_color

    def _draw_spinner(self):
        # Simple spinner animation (placeholder)
        self.create_oval(self.width//2-10, self.height//2-10, self.width//2+10, self.height//2+10, outline="#888", width=2, tags="spinner")

    def start_loading(self):
        self.loading = True
        self.draw_button()
        # Could add animation thread here

    def stop_loading(self):
        self.loading = False
        self.draw_button()

    def on_click(self, event):
        if self.disabled or self.loading:
            return
        if self.command:
            self.command()

    def on_enter(self, event):
        self._is_hovered = True
        self.itemconfig("button_bg", fill=self.hover_color)
        if self.on_mouse_enter:
            self.on_mouse_enter(event)

    def on_leave(self, event):
        self._is_hovered = False
        self.itemconfig("button_bg", fill=self.bg_color)
        if self.on_mouse_leave:
            self.on_mouse_leave(event)

    def on_mouse_down_event(self, event):
        if self.on_mouse_down:
            self.on_mouse_down(event)

    def on_mouse_up_event(self, event):
        if self.on_mouse_up:
            self.on_mouse_up(event)

    def on_key_event(self, event):
        if self.shortcut and event.keysym.lower() == self.shortcut.lower():
            if self.command:
                self.command()

    def show_tooltip(self, event=None):
        if not self.tooltip:
            return
        if self._tip:
            return
        x = self.winfo_rootx() + self.width // 2
        y = self.winfo_rooty() + self.height + 10
        self._tip = tw = tk.Toplevel(self)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.tooltip, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        tw = self._tip
        self._tip = None
        if tw:
            tw.destroy()

if __name__ == "__main__":
    def sample_command():
        print("Button clicked!")

    root = tk.Tk()
    root.title("BetterTkinter")

    button1 = BTkButton(root, text="Button 1", bg_color="#FF6347", hover_color="#FF4500", rounded_radius=25, width=120, height=50, command=sample_command, font=("Arial", 14, "bold"), border_color="#222", border_width=2, shadow=True, tooltip="Click me!", shortcut="Return")
    button1.pack(pady=10)

    button2 = BTkButton(root, text="Button 2", bg_color="#4CAF50", fg_color="black", hover_color="#388E3C", rounded_radius=30, width=160, height=50, command=sample_command, icon_path=None, loading=True)
    button2.pack(pady=10)

    button3 = BTkButton(root, text="Button 3", bg_color="#0078D7", hover_color="#005A9E", rounded_radius=40, width=180, height=70, command=sample_command, disabled=True)
    button3.pack(pady=10)

    root.mainloop()
