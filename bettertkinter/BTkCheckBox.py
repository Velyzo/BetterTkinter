import tkinter as tk
import math

class BTkCheckBox(tk.Canvas):
    """Modern BetterTkinter checkbox component"""
    
    # Constants
    DEFAULT_FONT = "Segoe UI"
    DEFAULT_SIZE = 20
    
    def __init__(self, parent, text="Checkbox", **kwargs):
        # Configuration
        self.text = kwargs.get('text', text)
        self.size = kwargs.get('size', self.DEFAULT_SIZE)
        self.command = kwargs.get('command', None)
        self.variable = kwargs.get('variable', None)
        
        # Calculate total width
        text_width = len(self.text) * 8 + 10
        total_width = self.size + text_width
        
        # Colors
        self.bg_color = kwargs.get('bg_color', "#FFFFFF")
        self.check_color = kwargs.get('check_color', "#007BFF")
        self.border_color = kwargs.get('border_color', "#CED4DA")
        self.text_color = kwargs.get('text_color', "#333333")
        self.hover_color = kwargs.get('hover_color', "#E3F2FD")
        
        # Initialize canvas
        super().__init__(parent,
                        width=total_width,
                        height=self.size + 4,
                        bg=self._get_parent_bg(parent),
                        highlightthickness=0,
                        bd=0)
        
        # State
        self._checked = kwargs.get('checked', False)
        self._hovered = False
        
        # Bind variable if provided
        if self.variable:
            self._checked = bool(self.variable.get())
            self.variable.trace_add('write', self._on_variable_change)
        
        # Render and bind events
        self._render()
        self._bind_events()
    
    def _get_parent_bg(self, parent):
        """Get parent background color"""
        try:
            return parent.cget("bg")
        except (AttributeError, tk.TclError):
            return "#FFFFFF"
    
    def _render(self):
        """Render checkbox"""
        self.delete("all")
        
        # Checkbox background
        bg_color = self.hover_color if self._hovered else self.bg_color
        
        # Draw checkbox square with rounded corners
        self._draw_rounded_rect(2, 2, self.size, self.size, 4, bg_color, self.border_color)
        
        # Draw checkmark if checked
        if self._checked:
            self._draw_checkmark()
        
        # Draw text
        self.create_text(self.size + 8, self.size // 2 + 2,
                        text=self.text,
                        fill=self.text_color,
                        font=(self.DEFAULT_FONT, 10, "normal"),
                        anchor="w",
                        tags="text")
    
    def _draw_rounded_rect(self, x, y, width, height, radius, fill_color, border_color):
        """Draw rounded rectangle"""
        if self._checked:
            fill_color = self.check_color
            border_color = self.check_color
        
        # Simple rounded rectangle using create_rectangle with small radius simulation
        self.create_rectangle(x, y, width, height,
                            fill=fill_color,
                            outline=border_color,
                            width=2)
    
    def _draw_checkmark(self):
        """Draw checkmark inside checkbox"""
        # Calculate checkmark points
        margin = 6
        x1, y1 = margin, self.size // 2
        x2, y2 = self.size // 2 - 2, self.size - margin
        x3, y3 = self.size - margin + 2, margin
        
        # Draw checkmark lines
        self.create_line(x1, y1, x2, y2, fill="white", width=2, capstyle="round")
        self.create_line(x2, y2, x3, y3, fill="white", width=2, capstyle="round")
    
    def _bind_events(self):
        """Bind mouse events"""
        self.bind("<Button-1>", self._on_click)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
    
    def _on_click(self, event=None):
        """Handle click event"""
        self.toggle()
        if self.command:
            try:
                self.command()
            except Exception as e:
                print(f"Checkbox command error: {e}")
    
    def _on_enter(self, event=None):
        """Handle mouse enter"""
        self._hovered = True
        self._render()
    
    def _on_leave(self, event=None):
        """Handle mouse leave"""
        self._hovered = False
        self._render()
    
    def _on_variable_change(self, *args):
        """Handle variable change"""
        if self.variable:
            new_value = bool(self.variable.get())
            if new_value != self._checked:
                self._checked = new_value
                self._render()
    
    def toggle(self):
        """Toggle checkbox state"""
        self._checked = not self._checked
        if self.variable:
            self.variable.set(self._checked)
        self._render()
    
    def get(self):
        """Get checkbox state"""
        return self._checked
    
    def set(self, value):
        """Set checkbox state"""
        self._checked = bool(value)
        if self.variable:
            self.variable.set(self._checked)
        self._render()

# Test function
if __name__ == "__main__":
    def test_checkbox():
        root = tk.Tk()
        root.title("BTkCheckBox Test")
        root.geometry("400x300")
        root.configure(bg="#FFFFFF")
        
        # Header
        tk.Label(root, text="BTkCheckBox Component Test",
                font=("Segoe UI", 14, "bold"),
                bg="#FFFFFF", fg="#333333").pack(pady=20)
        
        # Test checkboxes
        var1 = tk.BooleanVar()
        cb1 = BTkCheckBox(root, text="Option 1", variable=var1,
                         command=lambda: print(f"Option 1: {var1.get()}"))
        cb1.pack(pady=10)
        
        cb2 = BTkCheckBox(root, text="Option 2", checked=True,
                         command=lambda: print(f"Option 2: {cb2.get()}"))
        cb2.pack(pady=10)
        
        cb3 = BTkCheckBox(root, text="Custom styled option",
                         check_color="#28A745",
                         border_color="#28A745",
                         command=lambda: print(f"Option 3: {cb3.get()}"))
        cb3.pack(pady=10)
        
        # Control buttons
        btn_frame = tk.Frame(root, bg="#FFFFFF")
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Toggle All",
                 command=lambda: [cb1.toggle(), cb2.toggle(), cb3.toggle()]).pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="Check All",
                 command=lambda: [cb1.set(True), cb2.set(True), cb3.set(True)]).pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="Uncheck All",
                 command=lambda: [cb1.set(False), cb2.set(False), cb3.set(False)]).pack(side="left", padx=5)
        
        root.mainloop()
    
    test_checkbox()
