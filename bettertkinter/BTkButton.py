import tkinter as tk
import math

class BTkButton(tk.Canvas):
    """Modern, high-performance BetterTkinter button component"""
    
    # Constants
    DEFAULT_FONT = "Segoe UI"
    DEFAULT_WIDTH = 120
    DEFAULT_HEIGHT = 40
    DEFAULT_RADIUS = 8
    
    def __init__(self, parent, text="Button", style="primary", **kwargs):
        # Extract configuration
        self.text = kwargs.get('text', text)
        self.width = kwargs.get('width', self.DEFAULT_WIDTH)
        self.height = kwargs.get('height', self.DEFAULT_HEIGHT)
        self.command = kwargs.get('command', None)
        self.rounded_radius = kwargs.get('rounded_radius', self.DEFAULT_RADIUS)
        
        # Load style colors
        self._load_style(style, kwargs)
        
        # Initialize canvas with optimized settings
        super().__init__(parent, 
                        width=self.width, 
                        height=self.height, 
                        bg=self._get_parent_bg(parent),
                        highlightthickness=0,
                        bd=0,
                        relief='flat')
        
        # Button state
        self._state = "normal"
        self._rendered = False
        
        # Render and bind events
        self._render()
        self._bind_events()
    
    def _load_style(self, style, kwargs):
        """Load optimized color scheme"""
        # Modern color palette
        color_schemes = {
            "primary": {"bg": "#007BFF", "hover": "#0056B3", "press": "#004085", "fg": "white"},
            "success": {"bg": "#28A745", "hover": "#1E7E34", "press": "#155724", "fg": "white"},
            "warning": {"bg": "#FFC107", "hover": "#E0A800", "press": "#D39E00", "fg": "#212529"},
            "danger": {"bg": "#DC3545", "hover": "#BD2130", "press": "#A71E2A", "fg": "white"},
            "secondary": {"bg": "#6C757D", "hover": "#5A6268", "press": "#494F54", "fg": "white"},
            "light": {"bg": "#F8F9FA", "hover": "#E2E6EA", "press": "#DAE0E5", "fg": "#212529"},
            "dark": {"bg": "#343A40", "hover": "#23272B", "press": "#1D2024", "fg": "white"}
        }
        
        colors = color_schemes.get(style, color_schemes["primary"])
        self.bg_color = kwargs.get('bg_color', colors["bg"])
        self.hover_color = kwargs.get('hover_color', colors["hover"])
        self.press_color = kwargs.get('press_color', colors["press"])
        self.fg_color = kwargs.get('fg_color', colors["fg"])
    
    def _get_parent_bg(self, parent):
        """Get parent background with fallback"""
        try:
            return parent.cget("bg")
        except (AttributeError, tk.TclError):
            return "#FFFFFF"
    
    def _render(self):
        """Optimized rendering with caching"""
        if self._rendered and self.find_all():
            # Update existing elements for performance
            self._update_colors()
            return
        
        # Full render
        self.delete("all")
        
        # Get current state color
        current_color = self._get_current_color()
        
        # Draw button shape
        self._draw_button_shape(current_color)
        
        # Draw text
        self._draw_text()
        
        self._rendered = True
    
    def _get_current_color(self):
        """Get color for current state"""
        if self._state == "pressed":
            return self.press_color
        elif self._state == "hovered":
            return self.hover_color
        else:
            return self.bg_color
    
    def _draw_button_shape(self, color):
        """Draw optimized button shape"""
        if self.rounded_radius <= 0:
            # Simple rectangle for performance
            self.create_rectangle(0, 0, self.width, self.height, 
                                fill=color, outline=color, tags="button_bg")
        else:
            # Optimized rounded rectangle
            self._draw_rounded_rect(color)
    
    def _draw_rounded_rect(self, color):
        """Draw optimized rounded rectangle"""
        # Limit radius
        max_radius = min(self.width, self.height) // 2
        radius = min(self.rounded_radius, max_radius)
        
        if radius <= 2:
            # Use simple rectangle for very small radius
            self.create_rectangle(0, 0, self.width, self.height,
                                fill=color, outline=color, tags="button_bg")
            return
        
        # Create smooth rounded shape with fewer points for performance
        points = self._calculate_rounded_points(radius)
        self.create_polygon(points, fill=color, outline=color, smooth=True, tags="button_bg")
    
    def _calculate_rounded_points(self, radius):
        """Calculate points for rounded rectangle efficiently"""
        points = []
        w, h = self.width, self.height
        
        # Use fewer points for better performance
        steps = max(4, radius // 2)  # Adaptive step count
        
        # Top-left corner
        for i in range(steps):
            angle = math.pi + i * (math.pi/2) / (steps-1)
            x = radius + radius * math.cos(angle)
            y = radius + radius * math.sin(angle)
            points.extend([x, y])
        
        # Top-right corner
        for i in range(steps):
            angle = 1.5 * math.pi + i * (math.pi/2) / (steps-1)
            x = w - radius + radius * math.cos(angle)
            y = radius + radius * math.sin(angle)
            points.extend([x, y])
        
        # Bottom-right corner
        for i in range(steps):
            angle = i * (math.pi/2) / (steps-1)
            x = w - radius + radius * math.cos(angle)
            y = h - radius + radius * math.sin(angle)
            points.extend([x, y])
        
        # Bottom-left corner
        for i in range(steps):
            angle = 0.5 * math.pi + i * (math.pi/2) / (steps-1)
            x = radius + radius * math.cos(angle)
            y = h - radius + radius * math.sin(angle)
            points.extend([x, y])
        
        return points
    
    def _draw_text(self):
        """Draw button text with optimal font"""
        # Calculate font size based on button size
        base_font_size = min(self.width // 10, self.height // 3)
        font_size = max(8, min(12, base_font_size))
        
        self.create_text(self.width/2, self.height/2, 
                        text=self.text, 
                        fill=self.fg_color,
                        font=(self.DEFAULT_FONT, font_size, "normal"),
                        tags="button_text")
    
    def _update_colors(self):
        """Update colors for existing elements (performance optimization)"""
        current_color = self._get_current_color()
        
        # Update background color
        bg_items = self.find_withtag("button_bg")
        for item in bg_items:
            self.itemconfig(item, fill=current_color, outline=current_color)
    
    def _bind_events(self):
        """Bind optimized mouse events"""
        self.bind("<Enter>", self._on_enter, add='+')
        self.bind("<Leave>", self._on_leave, add='+')
        self.bind("<ButtonPress-1>", self._on_press, add='+')
        self.bind("<ButtonRelease-1>", self._on_release, add='+')
        self.bind("<Button-1>", self._on_click, add='+')
    
    def _on_enter(self, event=None):
        """Handle mouse enter with optimized rendering"""
        if self._state != "hovered":
            self._state = "hovered"
            self._update_colors()
    
    def _on_leave(self, event=None):
        """Handle mouse leave with optimized rendering"""
        if self._state != "normal":
            self._state = "normal"
            self._update_colors()
    
    def _on_press(self, event=None):
        """Handle mouse press with optimized rendering"""
        if self._state != "pressed":
            self._state = "pressed"
            self._update_colors()
    
    def _on_release(self, event=None):
        """Handle mouse release"""
        if self.winfo_containing(self.winfo_pointerx(), self.winfo_pointery()) == self:
            self._state = "hovered"
        else:
            self._state = "normal"
        self._update_colors()
    
    def _on_click(self, event=None):
        """Handle button click"""
        if self.command and callable(self.command):
            try:
                self.command()
            except Exception as e:
                print(f"Button command error: {e}")
    
    def configure(self, **kwargs):
        """Configure button properties with re-rendering"""
        if 'text' in kwargs:
            self.text = kwargs['text']
        if 'bg_color' in kwargs:
            self.bg_color = kwargs['bg_color']
        if 'command' in kwargs:
            self.command = kwargs['command']
        
        self._rendered = False  # Force re-render
        self._render()

# Performance test
if __name__ == "__main__":
    def performance_test():
        """Test button performance and appearance"""
        root = tk.Tk()
        root.title("BTkButton")
        root.geometry("900x600")
        root.configure(bg="#FFFFFF")
        
        # Header
        header = tk.Frame(root, bg="#FFFFFF", pady=15)
        header.pack(fill="x")
        
        tk.Label(header, text="BetterTkinter Button Performance Test", 
                font=(BTkButton.DEFAULT_FONT, 16, "bold"),
                bg="#FFFFFF", fg="#333333").pack()
        
        # Test different styles
        styles_frame = tk.Frame(root, bg="#FFFFFF")
        styles_frame.pack(pady=20)
        
        tk.Label(styles_frame, text="All Button Styles:", 
                font=(BTkButton.DEFAULT_FONT, 12, "normal"),
                bg="#FFFFFF", fg="#666666").pack(pady=(0, 10))
        
        button_container = tk.Frame(styles_frame, bg="#FFFFFF")
        button_container.pack()
        
        styles = ["primary", "success", "warning", "danger", "secondary", "light", "dark"]
        for i, style in enumerate(styles):
            btn = BTkButton(button_container, text=style.title(), style=style,
                          command=lambda s=style: print(f"{s} clicked"))
            btn.grid(row=0, column=i, padx=5)
        
        # Test different sizes
        sizes_frame = tk.Frame(root, bg="#FFFFFF")
        sizes_frame.pack(pady=20)
        
        tk.Label(sizes_frame, text="Different Sizes:", 
                font=(BTkButton.DEFAULT_FONT, 12, "normal"),
                bg="#FFFFFF", fg="#666666").pack(pady=(0, 10))
        
        size_container = tk.Frame(sizes_frame, bg="#FFFFFF")
        size_container.pack()
        
        sizes = [("XS", 60, 25), ("S", 80, 30), ("M", 120, 40), ("L", 160, 50), ("XL", 200, 60)]
        for i, (name, w, h) in enumerate(sizes):
            btn = BTkButton(size_container, text=name, width=w, height=h,
                          command=lambda n=name: print(f"{n} size clicked"))
            btn.grid(row=0, column=i, padx=5)
        
        # Test performance with many buttons
        perf_frame = tk.Frame(root, bg="#F8F9FA", pady=20)
        perf_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(perf_frame, text="Performance Test (25 Interactive Buttons):", 
                font=(BTkButton.DEFAULT_FONT, 12, "normal"),
                bg="#F8F9FA", fg="#666666").pack(pady=(0, 10))
        
        # Create grid of buttons for performance testing
        grid_frame = tk.Frame(perf_frame, bg="#F8F9FA")
        grid_frame.pack()
        
        for row in range(5):
            for col in range(5):
                btn_num = row * 5 + col + 1
                btn = BTkButton(grid_frame, text=f"Btn{btn_num}", 
                              style=styles[btn_num % len(styles)],
                              width=80, height=35,
                              command=lambda n=btn_num: print(f"Button {n} clicked"))
                btn.grid(row=row, column=col, padx=2, pady=2)
        
        root.mainloop()
    
    performance_test()
