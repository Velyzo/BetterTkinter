import tkinter as tk
import math

class BTkEntry(tk.Canvas):
    """Modern BetterTkinter entry component"""
    
    # Constants
    DEFAULT_FONT = "Segoe UI"
    DEFAULT_WIDTH = 200
    DEFAULT_HEIGHT = 32
    
    def __init__(self, parent, **kwargs):
        # Configuration
        self.width = kwargs.get('width', self.DEFAULT_WIDTH)
        self.height = kwargs.get('height', self.DEFAULT_HEIGHT)
        self.placeholder_text = kwargs.get('placeholder_text', "")
        self.show_char = kwargs.get('show', None)  # For password fields
        self.command = kwargs.get('command', None)  # Called on Enter key
        self.validate_command = kwargs.get('validate_command', None)
        
        # Colors
        self.bg_color = kwargs.get('bg_color', "#FFFFFF")
        self.border_color = kwargs.get('border_color', "#CED4DA")
        self.focus_border_color = kwargs.get('focus_border_color', "#007BFF")
        self.text_color = kwargs.get('text_color', "#333333")
        self.placeholder_color = kwargs.get('placeholder_color', "#6C757D")
        self.selection_bg = kwargs.get('selection_bg', "#007BFF")
        
        # Initialize canvas
        super().__init__(parent,
                        width=self.width,
                        height=self.height,
                        bg=self._get_parent_bg(parent),
                        highlightthickness=0,
                        bd=0)
        
        # State
        self._focused = False
        self._text_var = tk.StringVar()
        self._text_var.trace_add("write", self._on_text_change)
        
        # Initialize with default value
        if 'textvariable' in kwargs:
            self._text_var = kwargs['textvariable']
        elif 'text' in kwargs:
            self._text_var.set(kwargs['text'])
        
        # Create entry widget
        self._create_entry()
        
        # Render and bind events
        self._render()
        self._bind_events()
    
    def _get_parent_bg(self, parent):
        """Get parent background color"""
        try:
            return parent.cget("bg")
        except (AttributeError, tk.TclError):
            return "#FFFFFF"
    
    def _create_entry(self):
        """Create the internal Entry widget"""
        # Calculate entry position and size
        border_width = 2
        padding = 8
        
        entry_x = border_width + padding
        entry_y = border_width + padding
        entry_width = self.width - 2 * (border_width + padding)
        entry_height = self.height - 2 * (border_width + padding)
        
        # Create entry widget
        self.entry = tk.Entry(self,
                             textvariable=self._text_var,
                             font=(self.DEFAULT_FONT, 10, "normal"),
                             fg=self.text_color,
                             bg=self.bg_color,
                             relief="flat",
                             bd=0,
                             highlightthickness=0,
                             insertbackground=self.text_color,
                             selectbackground=self.selection_bg,
                             selectforeground="#FFFFFF")
        
        # Set password character if specified
        if self.show_char:
            self.entry.config(show=self.show_char)
        
        # Position entry widget
        self.create_window(entry_x, entry_y,
                          window=self.entry,
                          anchor="nw",
                          width=entry_width,
                          height=entry_height)
    
    def _render(self):
        """Render entry border and placeholder"""
        self.delete("border")
        
        # Determine border color
        border_color = self.focus_border_color if self._focused else self.border_color
        
        # Draw rounded border
        self._draw_rounded_border(border_color)
        
        # Handle placeholder text
        self._update_placeholder()
    
    def _draw_rounded_border(self, color):
        """Draw rounded border"""
        # Simple rounded rectangle simulation
        border_width = 2
        radius = 4
        
        # Main rectangle
        self.create_rectangle(1, 1, self.width-1, self.height-1,
                            outline=color,
                            width=border_width,
                            fill="",
                            tags="border")
        
        # Corner arcs for rounded appearance
        self.create_arc(1, 1, radius*2, radius*2,
                       outline=color, width=border_width,
                       start=90, extent=90, style="arc", tags="border")
        
        self.create_arc(self.width-radius*2-1, 1, self.width-1, radius*2,
                       outline=color, width=border_width,
                       start=0, extent=90, style="arc", tags="border")
        
        self.create_arc(1, self.height-radius*2-1, radius*2, self.height-1,
                       outline=color, width=border_width,
                       start=180, extent=90, style="arc", tags="border")
        
        self.create_arc(self.width-radius*2-1, self.height-radius*2-1,
                       self.width-1, self.height-1,
                       outline=color, width=border_width,
                       start=270, extent=90, style="arc", tags="border")
    
    def _update_placeholder(self):
        """Update placeholder text display"""
        self.delete("placeholder")
        
        current_text = self._text_var.get()
        
        if not current_text and self.placeholder_text and not self._focused:
            # Show placeholder
            self.create_text(12, self.height // 2,
                           text=self.placeholder_text,
                           fill=self.placeholder_color,
                           font=(self.DEFAULT_FONT, 10, "normal"),
                           anchor="w",
                           tags="placeholder")
    
    def _bind_events(self):
        """Bind events"""
        self.entry.bind("<FocusIn>", self._on_focus_in)
        self.entry.bind("<FocusOut>", self._on_focus_out)
        self.entry.bind("<Return>", self._on_return)
        self.entry.bind("<KeyRelease>", self._on_key_release)
        
        # Canvas events
        self.bind("<Button-1>", self._on_canvas_click)
    
    def _on_focus_in(self, event=None):
        """Handle focus in"""
        self._focused = True
        self._render()
    
    def _on_focus_out(self, event=None):
        """Handle focus out"""
        self._focused = False
        self._render()
    
    def _on_return(self, event=None):
        """Handle Return key"""
        if self.command:
            try:
                self.command()
            except Exception as e:
                print(f"Entry command error: {e}")
    
    def _on_key_release(self, event=None):
        """Handle key release for validation"""
        if self.validate_command:
            try:
                self.validate_command(self._text_var.get())
            except Exception as e:
                print(f"Entry validation error: {e}")
    
    def _on_canvas_click(self, event=None):
        """Handle canvas click to focus entry"""
        self.entry.focus_set()
    
    def _on_text_change(self, *args):
        """Handle text variable change"""
        self._update_placeholder()
    
    # Public methods
    def get(self):
        """Get entry text"""
        return self._text_var.get()
    
    def set(self, value):
        """Set entry text"""
        self._text_var.set(str(value))
    
    def clear(self):
        """Clear entry text"""
        self._text_var.set("")
    
    def focus(self):
        """Set focus to entry"""
        self.entry.focus_set()
    
    def configure(self, **kwargs):
        """Configure entry properties"""
        if 'text' in kwargs:
            self.set(kwargs['text'])
        if 'state' in kwargs:
            self.entry.config(state=kwargs['state'])
        if 'bg_color' in kwargs:
            self.bg_color = kwargs['bg_color']
            self.entry.config(bg=self.bg_color)
        if 'text_color' in kwargs:
            self.text_color = kwargs['text_color']
            self.entry.config(fg=self.text_color)
        
        self._render()
    
    def bind_var(self, variable):
        """Bind to a StringVar"""
        self._text_var = variable
        self.entry.config(textvariable=self._text_var)
        self._text_var.trace_add("write", self._on_text_change)
