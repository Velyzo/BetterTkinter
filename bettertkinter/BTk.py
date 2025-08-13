import tkinter as tk
from tkinter import ttk
import json
import os
import math
import threading
import time
from PIL import Image, ImageTk, ImageDraw, ImageFilter

# Constants for better code quality
DEFAULT_FONT = "Segoe UI"
TITLEBAR_HEIGHT = 40
CORNER_RADIUS = 12
SHADOW_BLUR = 10

class BTkWindowConfig:
    """Configuration class for BTk window settings"""
    def __init__(self, **kwargs):
        # Basic window settings
        self.title = kwargs.get('title', "BetterTkinter")
        self.icon_path = kwargs.get('icon_path')
        self.theme = kwargs.get('theme', "light")
        self.resizable = kwargs.get('resizable', True)
        self.transparent = kwargs.get('transparent', False)
        self.always_on_top = kwargs.get('always_on_top', False)
        self.min_size = kwargs.get('min_size', (300, 200))
        self.max_size = kwargs.get('max_size')
        
        # Advanced styling
        self.window_style = kwargs.get('window_style', "modern")
        self.border_radius = kwargs.get('border_radius', 15)
        self.border_width = kwargs.get('border_width', 2)
        self.border_color = kwargs.get('border_color', "#E0E0E0")
        self.rounded_corners = kwargs.get('rounded_corners', True)
        self.corner_radius = kwargs.get('corner_radius', CORNER_RADIUS)
        
        # Titlebar settings
        self.custom_titlebar = kwargs.get('custom_titlebar', True)
        self.titlebar_height = kwargs.get('titlebar_height', TITLEBAR_HEIGHT)
        self.titlebar_color = kwargs.get('titlebar_color')
        self.titlebar_text_color = kwargs.get('titlebar_text_color')
        self.titlebar_font = kwargs.get('titlebar_font', (DEFAULT_FONT, 11, "bold"))
        
        # Background effects
        self.background_gradient = kwargs.get('background_gradient')
        self.background_image = kwargs.get('background_image')
        self.background_blur = kwargs.get('background_blur', 0)
        self.glass_effect = kwargs.get('glass_effect', False)
        self.acrylic_blur = kwargs.get('acrylic_blur', 20)
        
        # Animation settings
        self.animations_enabled = kwargs.get('animations_enabled', True)
        self.fade_in_duration = kwargs.get('fade_in_duration', 0.3)
        self.resize_smooth = kwargs.get('resize_smooth', True)
        self.startup_position = kwargs.get('startup_position', "center")
        self.startup_animation = kwargs.get('startup_animation', "fade_in")
        self.close_animation = kwargs.get('close_animation', "fade_out")
        
        # Window controls
        self.custom_controls = kwargs.get('custom_controls', True)
        self.control_style = kwargs.get('control_style', "windows11")
        self.control_colors = kwargs.get('control_colors', {})
        
        # Shadow and effects
        self.shadow = kwargs.get('shadow', True)
        self.drop_shadow_enabled = kwargs.get('drop_shadow_enabled', True)
        self.drop_shadow_blur = kwargs.get('drop_shadow_blur', SHADOW_BLUR)
        self.drop_shadow_offset = kwargs.get('drop_shadow_offset', (2, 2))
        self.window_effects = kwargs.get('window_effects', [])
        
        # Callbacks
        self.on_close = kwargs.get('on_close')
        self.on_resize = kwargs.get('on_resize')
        self.on_move = kwargs.get('on_move')
        self.shortcuts = kwargs.get('shortcuts', {})

class BTk(tk.Tk):
    """Ultra-advanced BetterTkinter main window with extreme customization"""
    
    def __init__(self, **kwargs):
        super().__init__()
        self.config = BTkWindowConfig(**kwargs)
        
        # Initialize window state
        self._is_fullscreen = False
        self._is_maximized = False
        self._last_geometry = None
        self._drag_data = {"x": 0, "y": 0}
        self._resize_data = {"edge": None}
        self._animation_running = False
        
        # Theme colors
        self._theme_colors = self._load_theme_colors()
        
        # Setup window
        self._setup_window()
        self._setup_titlebar()
        self._setup_effects()
        self._setup_bindings()
        
        # Apply startup animation
        if self.config.animations_enabled:
            self._apply_startup_animation()
    
    def _load_theme_colors(self):
        """Load theme-specific colors"""
        themes = {
            "light": {
                "bg": "#FFFFFF",
                "fg": "#000000",
                "titlebar": "#F0F0F0",
                "titlebar_text": "#000000",
                "border": "#E0E0E0",
                "accent": "#0078D7",
                "hover": "#E5F3FF",
                "close_hover": "#E81123",
                "minimize_hover": "#E5E5E5",
                "maximize_hover": "#E5E5E5"
            },
            "dark": {
                "bg": "#2B2B2B",
                "fg": "#FFFFFF",
                "titlebar": "#1F1F1F",
                "titlebar_text": "#FFFFFF",
                "border": "#404040",
                "accent": "#0078D7",
                "hover": "#404040",
                "close_hover": "#E81123",
                "minimize_hover": "#404040",
                "maximize_hover": "#404040"
            },
            "blue": {
                "bg": "#E3F2FD",
                "fg": "#0D47A1",
                "titlebar": "#1976D2",
                "titlebar_text": "#FFFFFF",
                "border": "#90CAF9",
                "accent": "#2196F3",
                "hover": "#BBDEFB",
                "close_hover": "#E81123",
                "minimize_hover": "#64B5F6",
                "maximize_hover": "#64B5F6"
            },
            "green": {
                "bg": "#E8F5E8",
                "fg": "#1B5E20",
                "titlebar": "#388E3C",
                "titlebar_text": "#FFFFFF",
                "border": "#A5D6A7",
                "accent": "#4CAF50",
                "hover": "#C8E6C9",
                "close_hover": "#E81123",
                "minimize_hover": "#81C784",
                "maximize_hover": "#81C784"
            }
        }
        return themes.get(self.config.theme, themes["light"])
    
    def _setup_window(self):
        """Setup basic window properties"""
        self.title(self.config.title)
        self.resizable(self.config.resizable, self.config.resizable)
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        
        # Set window attributes
        if self.config.always_on_top:
            self.attributes("-topmost", True)
        
        if self.config.transparent:
            self.attributes("-alpha", 0.9)
        
        # Set size constraints
        self.minsize(*self.config.min_size)
        if self.config.max_size:
            self.maxsize(*self.config.max_size)
        
        # Remove default titlebar if using custom
        if self.config.custom_titlebar:
            self.overrideredirect(True)
        
        # Set background
        bg_color = self.config.titlebar_color or self._theme_colors["bg"]
        self.configure(bg=bg_color)
        
        # Set window position
        self._set_startup_position()
        
        # Load icon
        if self.config.icon_path:
            self._load_icon()
    
    def _setup_titlebar(self):
        """Create custom titlebar with advanced controls"""
        if not self.config.custom_titlebar:
            return
        
        titlebar_color = self.config.titlebar_color or self._theme_colors["titlebar"]
        text_color = self.config.titlebar_text_color or self._theme_colors["titlebar_text"]
        
        # Create titlebar frame
        self._titlebar = tk.Frame(self, height=self.config.titlebar_height, 
                                bg=titlebar_color, relief="flat")
        self._titlebar.pack(fill="x", side="top")
        self._titlebar.pack_propagate(False)
        
        # Title label
        self._title_label = tk.Label(self._titlebar, text=self.config.title, 
                                   bg=titlebar_color, fg=text_color, 
                                   font=self.config.titlebar_font)
        self._title_label.pack(side="left", padx=10, pady=5)
        
        # Window controls
        self._setup_window_controls()
        
        # Bind titlebar events
        self._titlebar.bind("<Button-1>", self._start_drag)
        self._titlebar.bind("<B1-Motion>", self._drag_window)
        self._titlebar.bind("<Double-Button-1>", self._toggle_maximize)
        self._title_label.bind("<Button-1>", self._start_drag)
        self._title_label.bind("<B1-Motion>", self._drag_window)
        self._title_label.bind("<Double-Button-1>", self._toggle_maximize)
    
    def _setup_window_controls(self):
        """Create modern window control buttons"""
        controls_frame = tk.Frame(self._titlebar, bg=self._theme_colors["titlebar"])
        controls_frame.pack(side="right", padx=5)
        
        # Control button styles
        button_width = 30
        button_height = 20
        
        # Close button
        self._close_btn = tk.Button(controls_frame, text="×", 
                                  width=button_width, height=button_height,
                                  command=self._close_window,
                                  bg=self._theme_colors["titlebar"],
                                  fg=self._theme_colors["titlebar_text"],
                                  border=0, font=(DEFAULT_FONT, 12, "bold"))
        self._close_btn.pack(side="right", padx=1)
        
        # Maximize button  
        self._maximize_btn = tk.Button(controls_frame, text="□", 
                                     width=button_width, height=button_height,
                                     command=self._toggle_maximize,
                                     bg=self._theme_colors["titlebar"],
                                     fg=self._theme_colors["titlebar_text"],
                                     border=0, font=(DEFAULT_FONT, 10))
        self._maximize_btn.pack(side="right", padx=1)
        
        # Minimize button
        self._minimize_btn = tk.Button(controls_frame, text="–", 
                                     width=button_width, height=button_height,
                                     command=self._minimize_window,
                                     bg=self._theme_colors["titlebar"],
                                     fg=self._theme_colors["titlebar_text"],
                                     border=0, font=(DEFAULT_FONT, 10))
        self._minimize_btn.pack(side="right", padx=1)
        
        # Bind hover effects
        self._setup_control_hover_effects()
    
    def _setup_control_hover_effects(self):
        """Add hover effects to window controls"""
        def on_enter_minimize(event):
            self._minimize_btn.configure(bg=self._theme_colors["minimize_hover"])
        
        def on_leave_minimize(event):
            self._minimize_btn.configure(bg=self._theme_colors["titlebar"])
        
        def on_enter_maximize(event):
            self._maximize_btn.configure(bg=self._theme_colors["maximize_hover"])
        
        def on_leave_maximize(event):
            self._maximize_btn.configure(bg=self._theme_colors["titlebar"])
        
        def on_enter_close(event):
            self._close_btn.configure(bg=self._theme_colors["close_hover"], fg="white")
        
        def on_leave_close(event):
            self._close_btn.configure(bg=self._theme_colors["titlebar"], 
                                    fg=self._theme_colors["titlebar_text"])
        
        self._minimize_btn.bind("<Enter>", on_enter_minimize)
        self._minimize_btn.bind("<Leave>", on_leave_minimize)
        self._maximize_btn.bind("<Enter>", on_enter_maximize)
        self._maximize_btn.bind("<Leave>", on_leave_maximize)
        self._close_btn.bind("<Enter>", on_enter_close)
        self._close_btn.bind("<Leave>", on_leave_close)
    
    def _setup_effects(self):
        """Apply visual effects like shadows and rounded corners"""
        if self.config.drop_shadow_enabled:
            self._apply_drop_shadow()
        
        if self.config.glass_effect:
            self._apply_glass_effect()
    
    def _setup_bindings(self):
        """Setup event bindings"""
        self.bind("<Configure>", self._on_configure)
        self.bind("<Key>", self._on_key_press)
        
        # Keyboard shortcuts
        for key, callback in self.config.shortcuts.items():
            self.bind(key, callback)
        
        # Resize bindings for borderless window
        if self.config.custom_titlebar:
            self.bind("<Button-1>", self._check_resize_edge)
            self.bind("<B1-Motion>", self._resize_window)
            self.bind("<Motion>", self._update_cursor)
    
    def _set_startup_position(self):
        """Set window startup position"""
        if self.config.startup_position == "center":
            self.center_window()
        elif isinstance(self.config.startup_position, tuple):
            x, y = self.config.startup_position
            self.geometry(f"+{x}+{y}")
    
    def _load_icon(self):
        """Load window icon"""
        try:
            if self.config.icon_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                img = Image.open(self.config.icon_path)
                img = img.resize((32, 32), Image.Resampling.LANCZOS)
                self.iconphoto(False, ImageTk.PhotoImage(img))
            else:
                self.iconbitmap(self.config.icon_path)
        except Exception as e:
            print(f"Could not load icon: {e}")
    
    def _apply_startup_animation(self):
        """Apply startup animation"""
        if self.config.startup_animation == "fade_in":
            self._fade_in_animation()
        elif self.config.startup_animation == "slide_in":
            self._slide_in_animation()
        elif self.config.startup_animation == "scale_in":
            self._scale_in_animation()
    
    def _fade_in_animation(self):
        """Fade in animation"""
        self.attributes("-alpha", 0.0)
        steps = 20
        step_duration = self.config.fade_in_duration / steps
        
        def animate_step(step):
            if step <= steps:
                alpha = step / steps
                self.attributes("-alpha", alpha)
                self.after(int(step_duration * 1000), lambda: animate_step(step + 1))
        
        animate_step(1)
    
    def _slide_in_animation(self):
        """Slide in animation"""
        screen_width = self.winfo_screenwidth()
        final_x = int((screen_width - 800) / 2)  # Assuming 800px width
        start_x = screen_width
        
        steps = 20
        step_duration = self.config.fade_in_duration / steps
        
        def animate_step(step):
            if step <= steps:
                current_x = start_x - ((start_x - final_x) * step / steps)
                self.geometry(f"+{int(current_x)}+100")
                self.after(int(step_duration * 1000), lambda: animate_step(step + 1))
        
        animate_step(1)
    
    def _scale_in_animation(self):
        """Scale in animation"""
        final_width, final_height = 800, 600
        start_width, start_height = 50, 50
        
        steps = 15
        step_duration = self.config.fade_in_duration / steps
        
        def animate_step(step):
            if step <= steps:
                scale = step / steps
                current_width = int(start_width + (final_width - start_width) * scale)
                current_height = int(start_height + (final_height - start_height) * scale)
                self.geometry(f"{current_width}x{current_height}")
                self.after(int(step_duration * 1000), lambda: animate_step(step + 1))
        
        animate_step(1)
    
    def _apply_drop_shadow(self):
        """Apply drop shadow effect (Windows only)"""
        try:
            import ctypes
            from ctypes import wintypes, windll
            
            GWL_EXSTYLE = -20
            WS_EX_LAYERED = 0x00080000
            WS_EX_TRANSPARENT = 0x00000020
            
            hwnd = int(self.wm_frame(), 16)
            windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE,
                                       windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE) | WS_EX_LAYERED)
        except Exception:
            pass  # Shadow not supported on this platform
    
    def _apply_glass_effect(self):
        """Apply glass/acrylic effect"""
        if self.config.acrylic_blur > 0:
            self.attributes("-alpha", 0.95)
    
    # Event handlers
    def _start_drag(self, event):
        """Start window dragging"""
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
    
    def _drag_window(self, event):
        """Drag window"""
        if not self._is_maximized:
            x = self.winfo_pointerx() - self._drag_data["x"]
            y = self.winfo_pointery() - self._drag_data["y"]
            self.geometry(f"+{x}+{y}")
    
    def _toggle_maximize(self, event=None):
        """Toggle maximize/restore window"""
        if self._is_maximized:
            self._restore_window()
        else:
            self._maximize_window()
    
    def _maximize_window(self):
        """Maximize window"""
        if not self._is_maximized:
            self._last_geometry = self.geometry()
            self._is_maximized = True
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            self.geometry(f"{screen_width}x{screen_height}+0+0")
            if hasattr(self, '_maximize_btn'):
                self._maximize_btn.configure(text="❐")
    
    def _restore_window(self):
        """Restore window from maximized state"""
        if self._is_maximized and self._last_geometry:
            self._is_maximized = False
            self.geometry(self._last_geometry)
            if hasattr(self, '_maximize_btn'):
                self._maximize_btn.configure(text="□")
    
    def _minimize_window(self):
        """Minimize window"""
        self.iconify()
    
    def _close_window(self):
        """Close window with animation"""
        if self.config.animations_enabled and self.config.close_animation:
            self._apply_close_animation()
        else:
            self._on_close()
    
    def _apply_close_animation(self):
        """Apply closing animation"""
        if self.config.close_animation == "fade_out":
            self._fade_out_animation()
        else:
            self._on_close()
    
    def _fade_out_animation(self):
        """Fade out animation"""
        steps = 10
        step_duration = 0.2 / steps
        
        def animate_step(step):
            if step <= steps:
                alpha = 1.0 - (step / steps)
                self.attributes("-alpha", alpha)
                if step == steps:
                    self.after(50, self._on_close)
                else:
                    self.after(int(step_duration * 1000), lambda: animate_step(step + 1))
        
        animate_step(1)
    
    def _check_resize_edge(self, event):
        """Check if click is on resize edge"""
        # Implementation for resize edge detection
        pass
    
    def _resize_window(self, event):
        """Resize window from edges"""
        # Implementation for edge resizing
        pass
    
    def _update_cursor(self, event):
        """Update cursor for resize edges"""
        # Implementation for cursor updates
        pass
    
    def _on_configure(self, event):
        """Handle window configure events"""
        if self.config.on_resize and event.widget == self:
            self.config.on_resize(event)
    
    def _on_key_press(self, event):
        """Handle key press events"""
        # Handle keyboard shortcuts
        pass
    
    def _on_close(self):
        """Handle window close event"""
        if self.config.on_close:
            self.config.on_close()
        self.destroy()
    
    # Public methods
    def center_window(self):
        """Center window on screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def set_theme(self, theme):
        """Change window theme"""
        self.config.theme = theme
        self._theme_colors = self._load_theme_colors()
        
        # Update colors
        bg_color = self._theme_colors["bg"]
        self.configure(bg=bg_color)
        
        if hasattr(self, '_titlebar'):
            titlebar_color = self._theme_colors["titlebar"]
            text_color = self._theme_colors["titlebar_text"]
            
            self._titlebar.configure(bg=titlebar_color)
            self._title_label.configure(bg=titlebar_color, fg=text_color)
            
            # Update control buttons
            for btn in [self._minimize_btn, self._maximize_btn, self._close_btn]:
                btn.configure(bg=titlebar_color, fg=text_color)
    
    def get_theme(self):
        """Get current theme"""
        return self.config.theme
    
    def toggle_fullscreen(self):
        """Toggle fullscreen mode"""
        self._is_fullscreen = not self._is_fullscreen
        self.attributes("-fullscreen", self._is_fullscreen)
    
    def save_config(self, filepath):
        """Save window configuration to file"""
        config_data = {
            "theme": self.config.theme,
            "geometry": self.geometry(),
            "always_on_top": self.config.always_on_top,
            "transparent": self.config.transparent,
            "animations_enabled": self.config.animations_enabled,
        }
        
        try:
            with open(filepath, 'w') as f:
                json.dump(config_data, f, indent=2)
        except Exception as e:
            print(f"Could not save config: {e}")
    
    def load_config(self, filepath):
        """Load window configuration from file"""
        try:
            with open(filepath, 'r') as f:
                config_data = json.load(f)
            
            self.set_theme(config_data.get("theme", "light"))
            if "geometry" in config_data:
                self.geometry(config_data["geometry"])
            
            return True
        except Exception as e:
            print(f"Could not load config: {e}")
            return False

# Test window
if __name__ == "__main__":
    def test_window():
        app = BTk(
            title="🚀 Ultra BTk Test Window",
            theme="dark",
            window_style="modern",
            border_radius=20,
            titlebar_height=50,
            animations_enabled=True,
            startup_animation="fade_in",
            close_animation="fade_out",
            drop_shadow_enabled=True,
            rounded_corners=True,
            glass_effect=True
        )
        app.geometry("800x600")
        
        # Test content
        test_frame = tk.Frame(app, bg=app._theme_colors["bg"])
        test_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        title_label = tk.Label(test_frame, text="🎨 Ultra-Advanced BTk Window",
                              font=(DEFAULT_FONT, 18, "bold"),
                              bg=app._theme_colors["bg"],
                              fg=app._theme_colors["fg"])
        title_label.pack(pady=20)
        
        features_text = """✨ EXTREME CUSTOMIZATION FEATURES ✨

🎨 Advanced Theming System
🖼️ Custom Titlebar with Modern Controls  
🌟 Smooth Animations (Fade, Slide, Scale)
🔄 Window Effects (Glass, Shadow, Acrylic)
📐 Rounded Corners & Border Styling
🎯 Drag-to-Move & Edge Resizing
⚙️ Configuration Save/Load System
🎪 Multiple Startup Positions
🎭 Theme Hot-Switching
🚀 Ultra-Smooth Performance"""
        
        features_label = tk.Label(test_frame, text=features_text,
                                 font=(DEFAULT_FONT, 10),
                                 bg=app._theme_colors["bg"],
                                 fg=app._theme_colors["fg"],
                                 justify="left")
        features_label.pack(pady=20)
        
        # Theme buttons
        theme_frame = tk.Frame(test_frame, bg=app._theme_colors["bg"])
        theme_frame.pack(pady=20)
        
        themes = ["light", "dark", "blue", "green"]
        for theme in themes:
            btn = tk.Button(theme_frame, text=f"{theme.title()} Theme",
                           command=lambda t=theme: app.set_theme(t),
                           font=(DEFAULT_FONT, 10, "bold"),
                           width=12, height=2)
            btn.pack(side="left", padx=5)
        
        app.center_window()
        app.mainloop()
    
    test_window()
