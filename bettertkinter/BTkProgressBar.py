import tkinter as tk
import math

class BTkProgressBar(tk.Canvas):
    """Modern BetterTkinter progress bar component"""
    
    # Constants
    DEFAULT_FONT = "Segoe UI"
    DEFAULT_WIDTH = 300
    DEFAULT_HEIGHT = 20
    
    def __init__(self, parent, **kwargs):
        # Configuration
        self.width = kwargs.get('width', self.DEFAULT_WIDTH)
        self.height = kwargs.get('height', self.DEFAULT_HEIGHT)
        self.minimum = kwargs.get('minimum', 0)
        self.maximum = kwargs.get('maximum', 100)
        self.value = kwargs.get('value', 0)
        self.show_percentage = kwargs.get('show_percentage', True)
        self.show_text = kwargs.get('show_text', True)
        
        # Colors
        self.bg_color = kwargs.get('bg_color', "#E9ECEF")
        self.progress_color = kwargs.get('progress_color', "#007BFF")
        self.text_color = kwargs.get('text_color', "#333333")
        self.border_color = kwargs.get('border_color', "#CED4DA")
        self.fg_color = kwargs.get('fg_color', "#007BFF")  # Alias for progress_color
        
        # Styling
        self.border_radius = kwargs.get('border_radius', 10)
        self.gradient = kwargs.get('gradient', False)
        self.animated = kwargs.get('animated', True)
        
        # Animation
        self.animate_enabled = kwargs.get('animate', True)
        self.animation_speed = kwargs.get('animation_speed', 10)  # ms
        
        # Initialize canvas
        super().__init__(parent,
                        width=self.width,
                        height=self.height,
                        bg=self._get_parent_bg(parent),
                        highlightthickness=0,
                        bd=0)
        
        # Animation state
        self._current_visual_value = self.value
        self._target_value = self.value
        self._animation_id = None
        self.animation_offset = 0  # For gradient animation
        
        # Render initial state
        self._render()
    
    def _get_parent_bg(self, parent):
        """Get parent background color"""
        try:
            return parent.cget("bg")
        except (AttributeError, tk.TclError):
            return "#FFFFFF"
    
    def _render(self):
        """Render progress bar"""
        self.delete("all")
        
        # Draw background
        self._draw_background()
        
        # Draw progress
        self._draw_progress()
        
        # Draw text if enabled
        if self.show_text or self.show_percentage:
            self._draw_text()
    
    def _draw_background(self):
        """Draw progress bar background"""
        # Simple rounded rectangle for background
        self.create_rectangle(0, 0, self.width, self.height,
                            fill=self.bg_color, outline=self.border_color, width=1)
    
    def _draw_progress(self):
        """Draw progress fill"""
        if self.value <= self.minimum:
            return
        
        # Calculate progress width
        progress_range = self.maximum - self.minimum
        if progress_range <= 0:
            return
        
        progress_ratio = (self.value - self.minimum) / progress_range
        progress_width = max(0, min(self.width - 2, (self.width - 2) * progress_ratio))
        
        if progress_width > 0:
            # Draw progress fill
            self.create_rectangle(1, 1, progress_width + 1, self.height - 1,
                                fill=self.progress_color, outline="", width=0)
    
    def _draw_text(self):
        """Draw progress text if enabled"""
        if not (self.show_percentage or self.show_text):
            return
            
        # Calculate percentage
        progress_range = self.maximum - self.minimum
        if progress_range <= 0:
            percentage = 0
        else:
            percentage = ((self.value - self.minimum) / progress_range) * 100
        
        # Draw percentage text
        if self.show_percentage:
            text = f"{percentage:.0f}%"
        else:
            text = str(self.value)
            
        x = self.width // 2
        y = self.height // 2
        
        self.create_text(x, y, text=text, font=(self.DEFAULT_FONT, 9, "normal"),
                        fill=self.text_color, anchor="center")
    
    def set_value(self, value):
        """Set progress bar value"""
        self.value = max(self.minimum, min(self.maximum, value))
        self._target_value = self.value
        
        if self.animate_enabled:
            self._animate_to_value()
        else:
            self._current_visual_value = self.value
            self._render()
    
    def _animate_to_value(self):
        """Animate progress bar to target value"""
        if abs(self._current_visual_value - self._target_value) < 0.5:
            self._current_visual_value = self._target_value
            self._render()
            return
        
        # Calculate animation step
        diff = self._target_value - self._current_visual_value
        step = diff * 0.1  # 10% of remaining distance
        
        self._current_visual_value += step
        self._render()
        
        # Schedule next animation frame
        self._animation_id = self.after(self.animation_speed, self._animate_to_value)
    
    def get_value(self):
        """Get current progress bar value"""
        return self.value
    
    def configure(self, **kwargs):
        """Configure progress bar properties"""
        if 'value' in kwargs:
            self.set_value(kwargs['value'])
            del kwargs['value']
        
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        
        self._render()

# Performance test
if __name__ == "__main__":
    def performance_test():
        """Test progress bar functionality"""
        root = tk.Tk()
        root.title("BTkProgressBar Test")
        root.geometry("600x400")
        root.configure(bg="#FFFFFF")
        
        # Header
        header = tk.Frame(root, bg="#FFFFFF", pady=15)
        header.pack(fill="x")
        
        tk.Label(header, text="BetterTkinter ProgressBar Test", 
                font=(BTkProgressBar.DEFAULT_FONT, 16, "bold"),
                bg="#FFFFFF", fg="#333333").pack()
        
        # Progress bars with different configurations
        progress_frame = tk.Frame(root, bg="#FFFFFF", pady=20)
        progress_frame.pack(fill="both", expand=True)
        
        # Test progress bars
        progress_bars = []
        
        for i, (label, config) in enumerate([
            ("Default Progress (50%)", {'value': 50}),
            ("Custom Colors (75%)", {'value': 75, 'progress_color': '#28A745', 'bg_color': '#F8F9FA'}),
            ("Large Progress (25%)", {'value': 25, 'width': 400, 'height': 30}),
            ("No Text (90%)", {'value': 90, 'show_percentage': False, 'show_text': False}),
        ]):
            # Label
            tk.Label(progress_frame, text=label, 
                    font=(BTkProgressBar.DEFAULT_FONT, 10),
                    bg="#FFFFFF", fg="#333333").pack(anchor="w", padx=20, pady=(10, 5))
            
            # Progress bar
            progress = BTkProgressBar(progress_frame, **config)
            progress.pack(padx=20, pady=(0, 10))
            progress_bars.append(progress)
        
        # Animation controls
        control_frame = tk.Frame(root, bg="#FFFFFF")
        control_frame.pack(fill="x", padx=20, pady=20)
        
        def animate_random():
            """Animate progress bars to random values"""
            import random
            for progress in progress_bars:
                progress.set_value(random.randint(0, 100))
        
        def reset_progress():
            """Reset all progress bars"""
            for progress in progress_bars:
                progress.set_value(0)
        
        def fill_progress():
            """Fill all progress bars"""
            for progress in progress_bars:
                progress.set_value(100)
        
        tk.Button(control_frame, text="Animate Random", command=animate_random,
                 font=(BTkProgressBar.DEFAULT_FONT, 10)).pack(side="left", padx=(0, 10))
        
        tk.Button(control_frame, text="Reset", command=reset_progress,
                 font=(BTkProgressBar.DEFAULT_FONT, 10)).pack(side="left", padx=(0, 10))
        
        tk.Button(control_frame, text="Fill", command=fill_progress,
                 font=(BTkProgressBar.DEFAULT_FONT, 10)).pack(side="left")
        
        root.mainloop()
    
    performance_test()
