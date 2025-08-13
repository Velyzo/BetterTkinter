import tkinter as tk
import math

class BTkLabel(tk.Canvas):
    """Modern BetterTkinter label component"""
    
    # Constants
    DEFAULT_FONT = "Segoe UI"
    DEFAULT_WIDTH = 200
    DEFAULT_HEIGHT = 32
    
    def __init__(self, parent, text="Label", **kwargs):
        # Store parent reference
        self.parent = parent
        
        # Configuration
        self.text = kwargs.get('text', text)
        self.width = kwargs.get('width', None)  # Auto-size if None
        self.height = kwargs.get('height', self.DEFAULT_HEIGHT)
        self.auto_width = self.width is None
        
        # Font configuration
        self.font_family = kwargs.get('font_family', self.DEFAULT_FONT)
        self.font_size = kwargs.get('font_size', 10)
        self.font_weight = kwargs.get('font_weight', "normal")
        self.font_tuple = (self.font_family, self.font_size, self.font_weight)
        
        # Colors
        self.bg_color = kwargs.get('bg_color', None)  # Transparent by default
        self.text_color = kwargs.get('text_color', "#333333")
        self.border_color = kwargs.get('border_color', None)
        
        # Alignment
        self.text_anchor = kwargs.get('anchor', "center")  # "w", "center", "e"
        self.justify = kwargs.get('justify', "center")  # "left", "center", "right"
        
        # Calculate dimensions if auto-width
        if self.auto_width:
            self.width = self._calculate_text_width() + 20
        
        # Get parent background if no bg_color specified
        if self.bg_color is None:
            self.bg_color = self._get_parent_bg(parent)
        
        # Initialize canvas
        super().__init__(parent,
                        width=self.width,
                        height=self.height,
                        bg=self.bg_color,
                        highlightthickness=0,
                        bd=0)
        
        # State
        self._hover_enabled = kwargs.get('hover_enabled', False)
        self._hover_color = kwargs.get('hover_color', "#F8F9FA")
        self._hovered = False
        self._clickable = kwargs.get('clickable', False)
        self._command = kwargs.get('command', None)
        
        # Render and bind events
        self._render()
        if self._hover_enabled or self._clickable:
            self._bind_events()
    
    def _get_parent_bg(self, parent):
        """Get parent background color"""
        try:
            return parent.cget("bg")
        except (AttributeError, tk.TclError):
            return "#FFFFFF"
    
    def _calculate_text_width(self):
        """Calculate text width for auto-sizing"""
        # Create temporary label to measure text
        temp = tk.Label(self.parent, text=self.text, font=self.font_tuple)
        temp.update_idletasks()
        width = temp.winfo_reqwidth()
        temp.destroy()
        return max(width, 50)  # Minimum width
    
    def _render(self):
        """Render label"""
        self.delete("all")
        
        # Draw background if hovered
        if self._hovered and self._hover_enabled:
            self._draw_background()
        
        # Draw border if specified
        if self.border_color:
            self._draw_border()
        
        # Draw text
        self._draw_text()
    
    def _draw_background(self):
        """Draw background for hover effect"""
        radius = 4
        
        # Simple rounded rectangle
        self.create_rectangle(2, 2, self.width-2, self.height-2,
                            fill=self._hover_color,
                            outline="",
                            tags="background")
    
    def _draw_border(self):
        """Draw border around label"""
        self.create_rectangle(1, 1, self.width-1, self.height-1,
                            outline=self.border_color,
                            width=1,
                            fill="",
                            tags="border")
    
    def _draw_text(self):
        """Draw text content"""
        # Calculate text position based on anchor
        if self.text_anchor == "w":
            x = 10
            anchor = "w"
        elif self.text_anchor == "e":
            x = self.width - 10
            anchor = "e"
        else:  # center
            x = self.width // 2
            anchor = "center"
        
        y = self.height // 2
        
        # Handle multiline text
        lines = self.text.split('\n')
        
        if len(lines) == 1:
            # Single line
            self.create_text(x, y,
                           text=self.text,
                           fill=self.text_color,
                           font=self.font_tuple,
                           anchor=anchor,
                           tags="text")
        else:
            # Multiple lines
            line_height = self.font_size + 4
            total_height = len(lines) * line_height
            start_y = (self.height - total_height) // 2 + line_height // 2
            
            for i, line in enumerate(lines):
                line_y = start_y + (i * line_height)
                self.create_text(x, line_y,
                               text=line,
                               fill=self.text_color,
                               font=self.font_tuple,
                               anchor=anchor,
                               tags="text")
    
    def _bind_events(self):
        """Bind mouse events"""
        if self._hover_enabled:
            self.bind("<Enter>", self._on_enter)
            self.bind("<Leave>", self._on_leave)
        
        if self._clickable:
            self.bind("<Button-1>", self._on_click)
            self.config(cursor="hand2")
    
    def _on_enter(self, event=None):
        """Handle mouse enter"""
        if self._hover_enabled:
            self._hovered = True
            self._render()
    
    def _on_leave(self, event=None):
        """Handle mouse leave"""
        if self._hover_enabled:
            self._hovered = False
            self._render()
    
    def _on_click(self, event=None):
        """Handle click event"""
        if self._clickable and self._command:
            try:
                self._command()
            except Exception as e:
                print(f"Label command error: {e}")
    
    # Public methods
    def configure(self, **kwargs):
        """Configure label properties"""
        redraw_needed = False
        
        if 'text' in kwargs:
            self.text = kwargs['text']
            if self.auto_width:
                new_width = self._calculate_text_width() + 20
                if new_width != self.width:
                    self.width = new_width
                    self.config(width=self.width)
            redraw_needed = True
        
        if 'text_color' in kwargs:
            self.text_color = kwargs['text_color']
            redraw_needed = True
        
        if 'bg_color' in kwargs:
            self.bg_color = kwargs['bg_color']
            self.config(bg=self.bg_color)
            redraw_needed = True
        
        if 'font_size' in kwargs:
            self.font_size = kwargs['font_size']
            self.font_tuple = (self.font_family, self.font_size, self.font_weight)
            if self.auto_width:
                new_width = self._calculate_text_width() + 20
                if new_width != self.width:
                    self.width = new_width
                    self.config(width=self.width)
            redraw_needed = True
        
        if 'font_weight' in kwargs:
            self.font_weight = kwargs['font_weight']
            self.font_tuple = (self.font_family, self.font_size, self.font_weight)
            redraw_needed = True
        
        if redraw_needed:
            self._render()
    
    def set_text(self, text):
        """Set label text"""
        self.configure(text=text)
    
    def get_text(self):
        """Get label text"""
        return self.text
