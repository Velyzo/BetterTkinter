import tkinter as tk
import math

class BTkButton(tk.Canvas):
    """Professional BetterTkinter button component with modern design"""
    
    # Font constant
    DEFAULT_FONT = "Segoe UI"
    
    def __init__(self, parent, text="Button", style="primary", **kwargs):
        # Configuration
        self.text = kwargs.get('text', text)
        self.width = kwargs.get('width', 120)
        self.height = kwargs.get('height', 40)
        self.command = kwargs.get('command', None)
        
        # Colors based on style
        self._load_style(style, kwargs)
        
        # Shape
        self.rounded_radius = kwargs.get('rounded_radius', 8)
        
        # Initialize canvas
        super().__init__(parent, 
                        width=self.width, 
                        height=self.height, 
                        bg=self._get_parent_bg(parent),
                        highlightthickness=0)
        
        # Button state
        self._state = "normal"
        
        # Render and bind events
        self._render()
        self._bind_events()
    
    def _load_style(self, style, kwargs):
        """Load color scheme based on style"""
        styles = {
            "primary": {"bg": "#007BFF", "hover": "#0056B3", "press": "#004085", "fg": "white"},
            "success": {"bg": "#28A745", "hover": "#1E7E34", "press": "#155724", "fg": "white"},
            "warning": {"bg": "#FFC107", "hover": "#E0A800", "press": "#D39E00", "fg": "black"},
            "danger": {"bg": "#DC3545", "hover": "#BD2130", "press": "#A71E2A", "fg": "white"},
            "secondary": {"bg": "#6C757D", "hover": "#5A6268", "press": "#494F54", "fg": "white"},
        }
        
        colors = styles.get(style, styles["primary"])
        self.bg_color = kwargs.get('bg_color', colors["bg"])
        self.hover_color = kwargs.get('hover_color', colors["hover"])
        self.press_color = kwargs.get('press_color', colors["press"])
        self.fg_color = kwargs.get('fg_color', colors["fg"])
    
    def _get_parent_bg(self, parent):
        """Get parent background color"""
        try:
            return parent.cget("bg")
        except (AttributeError, tk.TclError):
            return "#FFFFFF"
    
    def _render(self):
        """Render the button with current state"""
        self.delete("all")
        
        # Get current color based on state
        if self._state == "pressed":
            bg_color = self.press_color
        elif self._state == "hovered":
            bg_color = self.hover_color
        else:
            bg_color = self.bg_color
        
        # Draw rounded rectangle
        self._draw_rounded_rect(0, 0, self.width, self.height, self.rounded_radius, bg_color)
        
        # Draw text
        self.create_text(self.width/2, self.height/2, 
                        text=self.text, 
                        fill=self.fg_color,
                        font=(self.DEFAULT_FONT, 10, "normal"))
    
    def _draw_rounded_rect(self, x1, y1, x2, y2, radius, color):
        """Draw rounded rectangle using mathematical curves"""
        if radius <= 0:
            # Simple rectangle
            self.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            return
        
        # Limit radius to half of smallest dimension
        max_radius = min((x2-x1)/2, (y2-y1)/2)
        radius = min(radius, max_radius)
        
        # Create points for rounded corners
        points = []
        
        # Top-left corner
        for i in range(0, 90, 10):
            angle = math.radians(90 + i)
            px = x1 + radius - radius * math.cos(angle)
            py = y1 + radius - radius * math.sin(angle)
            points.extend([px, py])
        
        # Top-right corner
        for i in range(0, 90, 10):
            angle = math.radians(i)
            px = x2 - radius + radius * math.cos(angle)
            py = y1 + radius - radius * math.sin(angle)
            points.extend([px, py])
        
        # Bottom-right corner
        for i in range(0, 90, 10):
            angle = math.radians(270 + i)
            px = x2 - radius + radius * math.cos(angle)
            py = y2 - radius + radius * math.sin(angle)
            points.extend([px, py])
        
        # Bottom-left corner
        for i in range(0, 90, 10):
            angle = math.radians(180 + i)
            px = x1 + radius + radius * math.cos(angle)
            py = y2 - radius + radius * math.sin(angle)
            points.extend([px, py])
        
        # Draw the polygon
        self.create_polygon(points, fill=color, outline=color, smooth=True)
    
    def _bind_events(self):
        """Bind mouse events"""
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Button-1>", self._on_click)
    
    def _on_click(self, event=None):
        """Handle button click"""
        if self.command:
            self.command()
    
    def _on_enter(self, event=None):
        """Handle mouse enter"""
        self._state = "hovered"
        self._render()
    
    def _on_leave(self, event=None):
        """Handle mouse leave"""
        self._state = "normal"
        self._render()
    
    def _on_press(self, event=None):
        """Handle mouse press"""
        self._state = "pressed"
        self._render()
    
    def _on_release(self, event=None):
        """Handle mouse release"""
        self._state = "hovered"
        self._render()
    
    def configure(self, **kwargs):
        """Configure button properties"""
        if 'text' in kwargs:
            self.text = kwargs['text']
        if 'bg_color' in kwargs:
            self.bg_color = kwargs['bg_color']
        self._render()

# Test window
if __name__ == "__main__":
    def test_button():
        """Professional button demonstration"""
        root = tk.Tk()
        root.title("BetterTkinter Button Demo")
        root.geometry("800x600")
        root.configure(bg="#FFFFFF")
        
        # Header
        header_frame = tk.Frame(root, bg="#FFFFFF", pady=20)
        header_frame.pack(fill="x")
        
        tk.Label(header_frame, text="BetterTkinter Button Components", 
                font=(BTkButton.DEFAULT_FONT, 18, "normal"), 
                bg="#FFFFFF", fg="#333333").pack()
        
        tk.Label(header_frame, text="Professional UI components for modern applications", 
                font=(BTkButton.DEFAULT_FONT, 10, "normal"), 
                bg="#FFFFFF", fg="#666666").pack(pady=(5, 0))
        
        # Style variations
        styles_frame = tk.Frame(root, bg="#FFFFFF")
        styles_frame.pack(pady=20)
        
        tk.Label(styles_frame, text="Button Styles", 
                font=(BTkButton.DEFAULT_FONT, 14, "normal"), 
                bg="#FFFFFF", fg="#333333").pack(pady=(0, 15))
        
        style_container = tk.Frame(styles_frame, bg="#FFFFFF")
        style_container.pack()
        
        styles = ["primary", "success", "warning", "danger", "secondary"]
        for style in styles:
            btn = BTkButton(style_container, text=style.title(), style=style,
                          command=lambda s=style: print(f"{s.title()} button activated"))
            btn.pack(side="left", padx=8)
        
        # Size variations
        sizes_frame = tk.Frame(root, bg="#FFFFFF")
        sizes_frame.pack(pady=20)
        
        tk.Label(sizes_frame, text="Button Sizes", 
                font=(BTkButton.DEFAULT_FONT, 14, "normal"), 
                bg="#FFFFFF", fg="#333333").pack(pady=(0, 15))
        
        size_container = tk.Frame(sizes_frame, bg="#FFFFFF")
        size_container.pack()
        
        sizes = [("Small", 80, 30), ("Medium", 120, 40), ("Large", 160, 50)]
        for name, w, h in sizes:
            btn = BTkButton(size_container, text=name, width=w, height=h,
                          command=lambda n=name: print(f"{n} size selected"))
            btn.pack(side="left", padx=8)
        
        # Corner radius variations
        radius_frame = tk.Frame(root, bg="#FFFFFF")
        radius_frame.pack(pady=20)
        
        tk.Label(radius_frame, text="Corner Radius Options", 
                font=(BTkButton.DEFAULT_FONT, 14, "normal"), 
                bg="#FFFFFF", fg="#333333").pack(pady=(0, 15))
        
        radius_container = tk.Frame(radius_frame, bg="#FFFFFF")
        radius_container.pack()
        
        radii = [0, 5, 10, 15, 20]
        for radius in radii:
            btn = BTkButton(radius_container, text=f"R{radius}", rounded_radius=radius,
                          command=lambda r=radius: print(f"Radius {r}px applied"))
            btn.pack(side="left", padx=8)
        
        root.mainloop()
    
    test_button()
