import tkinter as tk
import sys
import os

# Add the parent directory to the path so we can import bettertkinter
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from BTk import BTk
    from BTkButton import BTkButton
    from BTkFrame import BTkFrame
    from BTkLabel import BTkLabel
    from BTkEntry import BTkEntry
    from BTkDialog import BTkDialog
    from BTkTooltip import BTkTooltip
    from BTkTheme import BTkTheme
    from BTkNavBar import BTkNavBar
    from BTkSlider import BTkSlider
    from BTkProgressBar import BTkProgressBar
    from BTkCheckBox import BTkCheckBox
    from BTkSwitch import BTkSwitch
except ImportError:
    # If direct imports fail, try relative imports
    from .BTk import BTk
    from .BTkButton import BTkButton
    from .BTkFrame import BTkFrame
    from .BTkLabel import BTkLabel
    from .BTkEntry import BTkEntry
    from .BTkDialog import BTkDialog
    from .BTkTooltip import BTkTooltip
    from .BTkTheme import BTkTheme
    from .BTkNavBar import BTkNavBar
    from .BTkSlider import BTkSlider
    from .BTkProgressBar import BTkProgressBar
    from .BTkCheckBox import BTkCheckBox
    from .BTkSwitch import BTkSwitch

class DemoApp(BTk):
    def __init__(self):
        super().__init__(title="BetterTkinter Demo - Ultimate UI Showcase", 
                        theme="light", resizable=True, custom_titlebar=False)
        self.geometry("1000x700")
        self.configure(bg="#F5F5F5")
        
        # Create main container with scrollable area
        self.create_demo_interface()
        
    def create_demo_interface(self):
        # Title
        title = BTkLabel(self, text="🎨 BetterTkinter Ultimate Demo", 
                        font=("Segoe UI", 24, "bold"), fg="#0078D7")
        title.pack(pady=20)
        
        # Create tabbed interface using frames
        self.create_navigation()
        self.create_widget_showcase()
        
    def create_navigation(self):
        # Navigation bar
        nav_items = [
            {"text": "🏠 Home", "icon": None},
            {"text": "🎛️ Controls", "icon": None},
            {"text": "📊 Progress", "icon": None},
            {"text": "🎨 Themes", "icon": None},
            {"text": "ℹ️ About", "icon": None}
        ]
        
        nav_options = {
            "position": "top",
            "bg": "#0078D7",
            "fg": "white",
            "active_bg": "#106EBE",
            "active_fg": "#FFD700",
            "border": True,
            "border_color": "#005A9E",
            "border_width": 2,
            "callback": self.on_nav_click,
            "font": ("Segoe UI", 12, "bold"),
            "height": 50,
            "style": "modern",
            "spacing": 20
        }
        
        self.navbar = BTkNavBar(self, items=nav_items, **nav_options)
        
    def create_widget_showcase(self):
        # Main content frame
        self.content_frame = BTkFrame(self, radius=25, width=950, height=550, 
                                    color="#FFFFFF", border=True, 
                                    border_color="#0078D7", border_thick=2)
        self.content_frame.pack(pady=20, padx=25)
        
        # Create sections
        self.create_button_section()
        self.create_input_section()
        self.create_progress_section()
        self.create_theme_section()
        
    def create_button_section(self):
        # Button showcase
        btn_frame = tk.Frame(self.content_frame, bg="#FFFFFF")
        btn_frame.pack(pady=20, padx=30, fill="x")
        
        tk.Label(btn_frame, text="🔘 Advanced Buttons", font=("Segoe UI", 16, "bold"), 
                bg="#FFFFFF", fg="#333").pack(anchor="w")
        
        btn_container = tk.Frame(btn_frame, bg="#FFFFFF")
        btn_container.pack(pady=10, fill="x")
        
        # Various button styles
        styles = [
            {"text": "Primary", "bg_color": "#0078D7", "hover_color": "#106EBE", "shadow": True},
            {"text": "Success", "bg_color": "#28A745", "hover_color": "#218838", "border_width": 2},
            {"text": "Warning", "bg_color": "#FFC107", "fg_color": "#000", "hover_color": "#E0A800"},
            {"text": "Danger", "bg_color": "#DC3545", "hover_color": "#C82333", "rounded_radius": 30}
        ]
        
        for i, style in enumerate(styles):
            btn = BTkButton(btn_container, command=lambda s=style: self.show_button_demo(s),
                          width=140, height=45, font=("Segoe UI", 11, "bold"), **style)
            btn.pack(side="left", padx=10)
            
    def create_input_section(self):
        # Input controls section
        input_frame = tk.Frame(self.content_frame, bg="#FFFFFF")
        input_frame.pack(pady=20, padx=30, fill="x")
        
        tk.Label(input_frame, text="📝 Input Controls", font=("Segoe UI", 16, "bold"), 
                bg="#FFFFFF", fg="#333").pack(anchor="w")
        
        controls_container = tk.Frame(input_frame, bg="#FFFFFF")
        controls_container.pack(pady=10, fill="x")
        
        # Left column
        left_col = tk.Frame(controls_container, bg="#FFFFFF")
        left_col.pack(side="left", fill="both", expand=True, padx=(0, 20))
        
        # Checkbox
        self.checkbox_var = tk.BooleanVar(value=True)
        checkbox = BTkCheckBox(left_col, text="Enable notifications", 
                             variable=self.checkbox_var, command=self.on_checkbox)
        checkbox.pack(anchor="w", pady=5)
        
        # Switch
        self.switch_var = tk.BooleanVar()
        switch_container = tk.Frame(left_col, bg="#FFFFFF")
        switch_container.pack(anchor="w", pady=10)
        tk.Label(switch_container, text="Dark mode:", bg="#FFFFFF", fg="#333").pack(side="left")
        switch = BTkSwitch(switch_container, variable=self.switch_var, 
                         command=self.on_switch_toggle)
        switch.pack(side="left", padx=(10, 0))
        
        # Right column  
        right_col = tk.Frame(controls_container, bg="#FFFFFF")
        right_col.pack(side="right", fill="both", expand=True)
        
        # Slider
        tk.Label(right_col, text="Volume:", bg="#FFFFFF", fg="#333").pack(anchor="w")
        self.slider = BTkSlider(right_col, from_=0, to=100, command=self.on_slider_change,
                              width=200, height=25, bg_color="#E0E0E0", fg_color="#0078D7")
        self.slider.pack(anchor="w", pady=5)
        self.slider.set(75)
        
        self.slider_label = tk.Label(right_col, text="75%", bg="#FFFFFF", fg="#666")
        self.slider_label.pack(anchor="w")
        
    def create_progress_section(self):
        # Progress indicators
        progress_frame = tk.Frame(self.content_frame, bg="#FFFFFF")
        progress_frame.pack(pady=20, padx=30, fill="x")
        
        tk.Label(progress_frame, text="📊 Progress Indicators", font=("Segoe UI", 16, "bold"), 
                bg="#FFFFFF", fg="#333").pack(anchor="w")
        
        progress_container = tk.Frame(progress_frame, bg="#FFFFFF")
        progress_container.pack(pady=10, fill="x")
        
        # Regular progress bar
        tk.Label(progress_container, text="Loading progress:", bg="#FFFFFF", fg="#333").pack(anchor="w")
        self.progress1 = BTkProgressBar(progress_container, width=300, height=20, 
                                      bg_color="#E0E0E0", fg_color="#0078D7", animated=False)
        self.progress1.pack(anchor="w", pady=5)
        
        # Animated progress bar  
        tk.Label(progress_container, text="Animated progress:", bg="#FFFFFF", fg="#333").pack(anchor="w", pady=(10, 0))
        self.progress2 = BTkProgressBar(progress_container, width=300, height=20,
                                      bg_color="#E0E0E0", fg_color="#28A745", 
                                      animated=True, gradient=True)
        self.progress2.pack(anchor="w", pady=5)
        
        # Progress controls
        btn_container = tk.Frame(progress_container, bg="#FFFFFF")
        btn_container.pack(anchor="w", pady=10)
        
        BTkButton(btn_container, text="Start Demo", command=self.start_progress_demo,
                 width=100, height=35, bg_color="#28A745").pack(side="left", padx=(0, 10))
        BTkButton(btn_container, text="Reset", command=self.reset_progress,
                 width=80, height=35, bg_color="#6C757D").pack(side="left")
        
    def create_theme_section(self):
        # Theme switcher
        theme_frame = tk.Frame(self.content_frame, bg="#FFFFFF")  
        theme_frame.pack(pady=20, padx=30, fill="x")
        
        tk.Label(theme_frame, text="🎨 Theme Options", font=("Segoe UI", 16, "bold"), 
                bg="#FFFFFF", fg="#333").pack(anchor="w")
        
        theme_container = tk.Frame(theme_frame, bg="#FFFFFF")
        theme_container.pack(pady=10, fill="x")
        
        themes = ["Light", "Dark", "Blue", "Green", "Purple"]
        for theme in themes:
            color_map = {
                "Light": "#F8F9FA", "Dark": "#343A40", "Blue": "#007BFF", 
                "Green": "#28A745", "Purple": "#6F42C1"
            }
            BTkButton(theme_container, text=theme, width=80, height=35,
                     bg_color=color_map[theme], 
                     fg_color="white" if theme != "Light" else "black",
                     command=lambda t=theme: self.change_theme(t)).pack(side="left", padx=5)
        
    def on_nav_click(self, idx, item):
        BTkDialog.info("Navigation", f"Selected: {item['text']}")
        
    def show_button_demo(self, style):
        BTkDialog.info("Button Demo", f"Clicked {style['text']} button!")
        
    def on_checkbox(self):
        status = "enabled" if self.checkbox_var.get() else "disabled"
        BTkDialog.info("Checkbox", f"Notifications {status}")
        
    def on_switch_toggle(self):
        if self.switch_var.get():
            self.configure(bg="#2C2C2C")
            BTkDialog.info("Theme", "Dark mode activated!")
        else:
            self.configure(bg="#F5F5F5") 
            BTkDialog.info("Theme", "Light mode activated!")
            
    def on_slider_change(self, value):
        self.slider_label.config(text=f"{int(value)}%")
        
    def start_progress_demo(self):
        """Animate progress bars"""
        self.animate_progress(0)
        
    def animate_progress(self, value):
        if value <= 100:
            self.progress1.set(value)
            self.progress2.set(value)
            self.after(50, lambda: self.animate_progress(value + 2))
            
    def reset_progress(self):
        self.progress1.set(0)
        self.progress2.set(0)
        
    def change_theme(self, theme):
        BTkDialog.info("Theme", f"Switched to {theme} theme!")

def main():
    """Entry point for console script"""
    app = DemoApp()
    app.mainloop()

if __name__ == "__main__":
    main()
