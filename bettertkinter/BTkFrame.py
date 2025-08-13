import tkinter as tk
import math

class BTkFrame(tk.Frame):
    """Modern, high-performance BetterTkinter frame component"""
    
    # Constants
    DEFAULT_FONT = "Segoe UI"
    DEFAULT_WIDTH = 200
    DEFAULT_HEIGHT = 150
    DEFAULT_RADIUS = 8
    
    def __init__(self, parent, style="default", **kwargs):
        # Configuration
        self.width = kwargs.get('width', self.DEFAULT_WIDTH)
        self.height = kwargs.get('height', self.DEFAULT_HEIGHT)
        self.rounded_radius = kwargs.get('rounded_radius', self.DEFAULT_RADIUS)
        
        # Load style
        self._load_style(style, kwargs)
        
        # Initialize frame with optimal settings
        super().__init__(parent, 
                        bg=self._get_parent_bg(parent), 
                        bd=0, 
                        highlightthickness=0,
                        relief='flat')
        
        # Create optimized canvas for custom drawing
        self.canvas = tk.Canvas(self,
                               width=self.width,
                               height=self.height,
                               bg=self._get_parent_bg(parent),
                               highlightthickness=0,
                               bd=0,
                               relief='flat')
        self.canvas.pack(fill='both', expand=True)
        
        # Render frame
        self._render()
        
        # Store original place method for content positioning
        self._original_place = super().place
    
    def _load_style(self, style, kwargs):
        """Load optimized style configuration"""
        # Modern style presets
        style_presets = {
            "default": {
                "bg": "#FFFFFF", 
                "border": "#E0E0E0", 
                "radius": 8,
                "shadow": False
            },
            "card": {
                "bg": "#FFFFFF", 
                "border": "#D0D0D0", 
                "radius": 12,
                "shadow": True
            },
            "modern": {
                "bg": "#F8F9FA", 
                "border": "#DEE2E6", 
                "radius": 10,
                "shadow": False
            },
            "dark": {
                "bg": "#343A40", 
                "border": "#495057", 
                "radius": 8,
                "shadow": True
            },
            "light": {
                "bg": "#F8F9FA",
                "border": "#E9ECEF",
                "radius": 6,
                "shadow": False
            },
            "primary": {
                "bg": "#E3F2FD",
                "border": "#2196F3",
                "radius": 8,
                "shadow": False
            },
            "success": {
                "bg": "#E8F5E8",
                "border": "#4CAF50",
                "radius": 8,
                "shadow": False
            }
        }
        
        preset = style_presets.get(style, style_presets["default"])
        
        # Apply configuration
        self.bg_color = kwargs.get('bg_color', preset["bg"])
        self.border_color = kwargs.get('border_color', preset["border"])
        self.rounded_radius = kwargs.get('rounded_radius', preset["radius"])
        self.border_width = kwargs.get('border_width', 1)
        self.shadow = kwargs.get('shadow', preset.get("shadow", False))
    
    def _get_parent_bg(self, parent):
        """Get parent background with fallback"""
        try:
            return parent.cget('bg')
        except (AttributeError, tk.TclError):
            return "#FFFFFF"
    
    def _render(self):
        """Optimized frame rendering"""
        self.canvas.delete("all")
        
        # Draw shadow if enabled
        if self.shadow:
            self._draw_shadow()
        
        # Draw main frame
        self._draw_frame_shape()
    
    def _draw_shadow(self):
        """Draw subtle shadow effect"""
        shadow_offset = 2
        shadow_color = "#E0E0E0"  # Light gray shadow
        
        if self.rounded_radius > 0:
            points = self._calculate_rounded_points(
                shadow_offset, shadow_offset,
                self.width + shadow_offset, self.height + shadow_offset,
                self.rounded_radius
            )
            self.canvas.create_polygon(points, fill=shadow_color, outline="", smooth=True)
        else:
            self.canvas.create_rectangle(
                shadow_offset, shadow_offset,
                self.width + shadow_offset, self.height + shadow_offset,
                fill=shadow_color, outline=""
            )
    
    def _draw_frame_shape(self):
        """Draw the main frame shape"""
        if self.rounded_radius <= 0:
            # Simple rectangle
            if self.border_width > 0:
                self.canvas.create_rectangle(
                    0, 0, self.width, self.height,
                    fill=self.bg_color,
                    outline=self.border_color,
                    width=self.border_width
                )
            else:
                self.canvas.create_rectangle(
                    0, 0, self.width, self.height,
                    fill=self.bg_color, outline=""
                )
        else:
            # Rounded rectangle
            self._draw_rounded_frame()
    
    def _draw_rounded_frame(self):
        """Draw optimized rounded frame"""
        points = self._calculate_rounded_points(0, 0, self.width, self.height, self.rounded_radius)
        
        # Draw filled shape
        self.canvas.create_polygon(points, fill=self.bg_color, outline="", smooth=True)
        
        # Draw border if needed
        if self.border_width > 0:
            self.canvas.create_polygon(points, fill="", outline=self.border_color, 
                                     width=self.border_width, smooth=True)
    
    def _calculate_rounded_points(self, x1, y1, x2, y2, radius):
        """Calculate points for rounded rectangle efficiently"""
        # Limit radius
        max_radius = min((x2-x1)/2, (y2-y1)/2)
        radius = min(radius, max_radius)
        
        if radius <= 1:
            return [x1, y1, x2, y1, x2, y2, x1, y2]
        
        points = []
        
        # Use adaptive step count for performance
        steps = max(3, min(8, radius // 2))
        
        # Top-left corner
        for i in range(steps):
            angle = math.pi + i * (math.pi/2) / (steps-1)
            x = x1 + radius + radius * math.cos(angle)
            y = y1 + radius + radius * math.sin(angle)
            points.extend([x, y])
        
        # Top-right corner
        for i in range(steps):
            angle = 1.5 * math.pi + i * (math.pi/2) / (steps-1)
            x = x2 - radius + radius * math.cos(angle)
            y = y1 + radius + radius * math.sin(angle)
            points.extend([x, y])
        
        # Bottom-right corner
        for i in range(steps):
            angle = i * (math.pi/2) / (steps-1)
            x = x2 - radius + radius * math.cos(angle)
            y = y2 - radius + radius * math.sin(angle)
            points.extend([x, y])
        
        # Bottom-left corner
        for i in range(steps):
            angle = 0.5 * math.pi + i * (math.pi/2) / (steps-1)
            x = x1 + radius + radius * math.cos(angle)
            y = y2 - radius + radius * math.sin(angle)
            points.extend([x, y])
        
        return points
    
    def configure(self, **kwargs):
        """Configure frame properties"""
        if 'bg_color' in kwargs:
            self.bg_color = kwargs['bg_color']
        if 'border_color' in kwargs:
            self.border_color = kwargs['border_color']
        if 'rounded_radius' in kwargs:
            self.rounded_radius = kwargs['rounded_radius']
        
        self._render()
    
    def place_content(self, widget, relx=0.5, rely=0.5, anchor="center", **kwargs):
        """Place content inside the frame with proper positioning"""
        # Handle padding separately
        padx = kwargs.pop('padx', 0)
        pady = kwargs.pop('pady', 0)
        
        # Use canvas coordinates for precise positioning
        x = relx * self.width + padx
        y = rely * self.height + pady
        
        # Create window in canvas for the widget
        self.canvas.create_window(x, y, window=widget, anchor=anchor, **kwargs)

# Performance test
if __name__ == "__main__":
    def performance_test():
        """Test frame performance and appearance"""
        root = tk.Tk()
        root.title("BTkFrame")
        root.geometry("1000x700")
        root.configure(bg="#FFFFFF")
        
        # Header
        header = tk.Frame(root, bg="#FFFFFF", pady=15)
        header.pack(fill="x")
        
        tk.Label(header, text="BetterTkinter Frame Performance Test", 
                font=(BTkFrame.DEFAULT_FONT, 16, "bold"),
                bg="#FFFFFF", fg="#333333").pack()
        
        # Create scrollable content
        canvas_container = tk.Frame(root, bg="#FFFFFF")
        canvas_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Test different styles
        styles_frame = tk.Frame(canvas_container, bg="#FFFFFF")
        styles_frame.pack(pady=10)
        
        tk.Label(styles_frame, text="Frame Styles:", 
                font=(BTkFrame.DEFAULT_FONT, 14, "bold"),
                bg="#FFFFFF", fg="#333333").pack(anchor="w", pady=(0, 15))
        
        # Create grid of different styled frames
        grid_container = tk.Frame(styles_frame, bg="#FFFFFF")
        grid_container.pack(fill="x")
        
        styles = ["default", "card", "modern", "dark", "light", "primary", "success"]
        
        for i, style in enumerate(styles):
            row = i // 4
            col = i % 4
            
            # Frame container
            frame_container = tk.Frame(grid_container, bg="#FFFFFF")
            frame_container.grid(row=row, column=col, padx=10, pady=10, sticky="w")
            
            # Style label
            tk.Label(frame_container, text=f"{style.title()} Style", 
                    font=(BTkFrame.DEFAULT_FONT, 10, "normal"),
                    bg="#FFFFFF", fg="#666666").pack(anchor="w", pady=(0, 5))
            
            # Create frame
            frame = BTkFrame(frame_container, style=style, width=220, height=120)
            frame.pack()
            
            # Add content to frame
            text_color = "#FFFFFF" if style == "dark" else "#333333"
            content_label = tk.Label(frame, 
                                   text=f"Content in {style} frame\nwith professional styling", 
                                   font=(BTkFrame.DEFAULT_FONT, 9, "normal"),
                                   bg=frame.bg_color, fg=text_color,
                                   justify="center")
            
            # Use the place_content method for proper positioning
            frame.place_content(content_label)
        
        # Size variations
        sizes_frame = tk.Frame(canvas_container, bg="#FFFFFF")
        sizes_frame.pack(pady=20)
        
        tk.Label(sizes_frame, text="Size Variations:", 
                font=(BTkFrame.DEFAULT_FONT, 14, "bold"),
                bg="#FFFFFF", fg="#333333").pack(anchor="w", pady=(0, 15))
        
        size_container = tk.Frame(sizes_frame, bg="#FFFFFF")
        size_container.pack()
        
        sizes = [("Small", 150, 80), ("Medium", 250, 120), ("Large", 350, 160)]
        
        for i, (name, w, h) in enumerate(sizes):
            frame_container = tk.Frame(size_container, bg="#FFFFFF")
            frame_container.grid(row=0, column=i, padx=15, sticky="w")
            
            tk.Label(frame_container, text=f"{name} Frame", 
                    font=(BTkFrame.DEFAULT_FONT, 10, "normal"),
                    bg="#FFFFFF", fg="#666666").pack(anchor="w", pady=(0, 5))
            
            frame = BTkFrame(frame_container, style="card", width=w, height=h)
            frame.pack()
            
            content = tk.Label(frame, text=f"{name}\n{w}×{h}px", 
                             font=(BTkFrame.DEFAULT_FONT, 10, "normal"),
                             bg=frame.bg_color, fg="#333333", justify="center")
            frame.place_content(content)
        
        # Performance test with many frames
        perf_section = tk.Frame(canvas_container, bg="#F8F9FA")
        perf_section.pack(fill="x", pady=20)
        
        tk.Label(perf_section, text="Performance Test (16 Interactive Frames):", 
                font=(BTkFrame.DEFAULT_FONT, 12, "normal"),
                bg="#F8F9FA", fg="#666666").pack(pady=10)
        
        perf_grid = tk.Frame(perf_section, bg="#F8F9FA")
        perf_grid.pack()
        
        for row in range(4):
            for col in range(4):
                frame_num = row * 4 + col + 1
                style = styles[frame_num % len(styles)]
                
                frame = BTkFrame(perf_grid, style=style, width=120, height=80)
                frame.grid(row=row, column=col, padx=5, pady=5)
                
                label = tk.Label(frame, text=f"Frame {frame_num}", 
                               font=(BTkFrame.DEFAULT_FONT, 8, "normal"),
                               bg=frame.bg_color, 
                               fg="#FFFFFF" if style == "dark" else "#333333")
                frame.place_content(label)
        
        root.mainloop()
    
    performance_test()
