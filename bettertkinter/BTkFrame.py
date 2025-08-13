import tkinter as tk
import math

class BTkFrame(tk.Frame):
    """Professional BetterTkinter frame component with modern design"""
    
    # Font constant
    DEFAULT_FONT = "Segoe UI"
    
    def __init__(self, parent, style="default", **kwargs):
        # Configuration
        self.width = kwargs.get('width', 200)
        self.height = kwargs.get('height', 150)
        
        # Load style
        self._load_style(style, kwargs)
        
        # Initialize frame
        super().__init__(parent, bg=self._get_parent_bg(parent), bd=0, highlightthickness=0)
        
        # Create canvas for custom drawing
        self.canvas = tk.Canvas(self,
                               width=self.width,
                               height=self.height,
                               bg=self._get_parent_bg(parent),
                               highlightthickness=0,
                               bd=0)
        self.canvas.pack(fill='both', expand=True)
        
        # Render the frame
        self._render()
    
    def _load_style(self, style, kwargs):
        """Load frame style"""
        styles = {
            "default": {"bg": "#FFFFFF", "border": "#E0E0E0", "radius": 8},
            "card": {"bg": "#FFFFFF", "border": "#D0D0D0", "radius": 12},
            "modern": {"bg": "#F8F9FA", "border": "#DEE2E6", "radius": 10},
            "dark": {"bg": "#343A40", "border": "#495057", "radius": 8},
        }
        
        colors = styles.get(style, styles["default"])
        self.bg_color = kwargs.get('bg_color', colors["bg"])
        self.border_color = kwargs.get('border_color', colors["border"])
        self.rounded_radius = kwargs.get('rounded_radius', colors["radius"])
        self.border_width = kwargs.get('border_width', 1)
    
    def _get_parent_bg(self, parent):
        """Get parent background color"""
        try:
            return parent.cget('bg')
        except (AttributeError, tk.TclError):
            return "#F0F0F0"
    
    def _render(self):
        """Render the frame"""
        self.canvas.delete("all")
        
        # Draw background with rounded corners
        self._draw_rounded_rect(0, 0, self.width, self.height, 
                               self.rounded_radius, self.bg_color, self.border_color)
    
    def _draw_rounded_rect(self, x1, y1, x2, y2, radius, fill_color, border_color=None):
        """Draw rounded rectangle with optional border"""
        if radius <= 0:
            # Simple rectangle
            self.canvas.create_rectangle(x1, y1, x2, y2, 
                                       fill=fill_color, 
                                       outline=border_color or fill_color,
                                       width=self.border_width)
            return
        
        # Limit radius
        max_radius = min((x2-x1)/2, (y2-y1)/2)
        radius = min(radius, max_radius)
        
        # Create points for rounded rectangle
        points = []
        
        # Top-left corner
        for i in range(0, 90, 15):
            angle = math.radians(90 + i)
            px = x1 + radius - radius * math.cos(angle)
            py = y1 + radius - radius * math.sin(angle)
            points.extend([px, py])
        
        # Top-right corner
        for i in range(0, 90, 15):
            angle = math.radians(i)
            px = x2 - radius + radius * math.cos(angle)
            py = y1 + radius - radius * math.sin(angle)
            points.extend([px, py])
        
        # Bottom-right corner
        for i in range(0, 90, 15):
            angle = math.radians(270 + i)
            px = x2 - radius + radius * math.cos(angle)
            py = y2 - radius + radius * math.sin(angle)
            points.extend([px, py])
        
        # Bottom-left corner
        for i in range(0, 90, 15):
            angle = math.radians(180 + i)
            px = x1 + radius + radius * math.cos(angle)
            py = y2 - radius + radius * math.sin(angle)
            points.extend([px, py])
        
        # Draw the polygon
        if border_color and self.border_width > 0:
            self.canvas.create_polygon(points, fill=fill_color, 
                                     outline=border_color, width=self.border_width, smooth=True)
        else:
            self.canvas.create_polygon(points, fill=fill_color, outline=fill_color, smooth=True)
    
    def configure(self, **kwargs):
        """Configure frame properties"""
        if 'bg_color' in kwargs:
            self.bg_color = kwargs['bg_color']
        if 'border_color' in kwargs:
            self.border_color = kwargs['border_color']
        if 'rounded_radius' in kwargs:
            self.rounded_radius = kwargs['rounded_radius']
        
        self._render()

# Test window
if __name__ == "__main__":
    def test_frame():
        """Professional frame demonstration"""
        root = tk.Tk()
        root.title("BetterTkinter Frame Demo")
        root.geometry("900x700")
        root.configure(bg="#FFFFFF")
        
        # Header
        header_frame = tk.Frame(root, bg="#FFFFFF", pady=20)
        header_frame.pack(fill="x")
        
        tk.Label(header_frame, text="BetterTkinter Frame Components", 
                font=(BTkFrame.DEFAULT_FONT, 18, "normal"), 
                bg="#FFFFFF", fg="#333333").pack()
        
        tk.Label(header_frame, text="Professional container components for modern applications", 
                font=(BTkFrame.DEFAULT_FONT, 10, "normal"), 
                bg="#FFFFFF", fg="#666666").pack(pady=(5, 0))
        
        # Style showcase
        styles_frame = tk.Frame(root, bg="#FFFFFF")
        styles_frame.pack(pady=20)
        
        tk.Label(styles_frame, text="Frame Styles", 
                font=(BTkFrame.DEFAULT_FONT, 14, "normal"), 
                bg="#FFFFFF", fg="#333333").pack(pady=(0, 15))
        
        # First row of frames
        frames_row1 = tk.Frame(styles_frame, bg="#FFFFFF")
        frames_row1.pack(pady=10)
        
        styles = ["default", "card"]
        for style in styles:
            container = tk.Frame(frames_row1, bg="#FFFFFF")
            container.pack(side="left", padx=15)
            
            tk.Label(container, text=style.title(), 
                    font=(BTkFrame.DEFAULT_FONT, 12, "normal"), 
                    bg="#FFFFFF", fg="#333333").pack(pady=(0, 8))
            
            frame = BTkFrame(container, style=style, width=250, height=120)
            frame.pack()
            
            # Add content to frame
            content_label = tk.Label(frame, text=f"{style.title()} Frame Content", 
                                   font=(BTkFrame.DEFAULT_FONT, 10, "normal"),
                                   bg=frame.bg_color, fg="#333333")
            content_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Second row of frames
        frames_row2 = tk.Frame(styles_frame, bg="#FFFFFF")
        frames_row2.pack(pady=10)
        
        styles = ["modern", "dark"]
        for style in styles:
            container = tk.Frame(frames_row2, bg="#FFFFFF")
            container.pack(side="left", padx=15)
            
            tk.Label(container, text=style.title(), 
                    font=(BTkFrame.DEFAULT_FONT, 12, "normal"), 
                    bg="#FFFFFF", fg="#333333").pack(pady=(0, 8))
            
            frame = BTkFrame(container, style=style, width=250, height=120)
            frame.pack()
            
            # Add content to frame
            text_color = "#FFFFFF" if style == "dark" else "#333333"
            content_label = tk.Label(frame, text=f"{style.title()} Frame Content", 
                                   font=(BTkFrame.DEFAULT_FONT, 10, "normal"),
                                   bg=frame.bg_color, fg=text_color)
            content_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Size variations
        sizes_frame = tk.Frame(root, bg="#FFFFFF")
        sizes_frame.pack(pady=20)
        
        tk.Label(sizes_frame, text="Frame Sizes", 
                font=(BTkFrame.DEFAULT_FONT, 14, "normal"), 
                bg="#FFFFFF", fg="#333333").pack(pady=(0, 15))
        
        size_container = tk.Frame(sizes_frame, bg="#FFFFFF")
        size_container.pack()
        
        sizes = [("Small", 150, 80), ("Medium", 250, 120), ("Large", 350, 160)]
        for name, w, h in sizes:
            container = tk.Frame(size_container, bg="#FFFFFF")
            container.pack(side="left", padx=15)
            
            tk.Label(container, text=name, 
                    font=(BTkFrame.DEFAULT_FONT, 12, "normal"), 
                    bg="#FFFFFF", fg="#333333").pack(pady=(0, 8))
            
            frame = BTkFrame(container, style="card", width=w, height=h)
            frame.pack()
            
            # Add content to frame
            content_label = tk.Label(frame, text=f"{name} Frame", 
                                   font=(BTkFrame.DEFAULT_FONT, 10, "normal"),
                                   bg=frame.bg_color, fg="#333333")
            content_label.place(relx=0.5, rely=0.5, anchor="center")
        
        root.mainloop()
    
    test_frame()
