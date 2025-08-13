# 📚 BetterTkinter Examples Collection

Complete collection of practical examples demonstrating BetterTkinter components and patterns.

## 🚀 Quick Start Examples

### Basic Window
```python
from bettertkinter import BTk

app = BTk(title="My App", geometry="400x300")
app.mainloop()
```

### Themed Application
```python
from bettertkinter import BTk, BTkButton, BTkLabel, BTkFrame

class ThemedApp(BTk):
    def __init__(self):
        super().__init__(title="Themed App", theme="dark")
        
        container = BTkFrame(self)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        BTkLabel(container, text="Dark Theme Demo", 
                font_size=16).pack(pady=20)
        
        BTkButton(container, text="Primary", 
                 style="primary").pack(pady=5, fill="x")
        BTkButton(container, text="Success", 
                 style="success").pack(pady=5, fill="x")

app = ThemedApp()
app.mainloop()
```

## 📝 Form Examples

### Contact Form
```python
from bettertkinter import (
    BTk, BTkFrame, BTkLabel, BTkEntry, BTkButton, 
    BTkCheckBox, BTkDialog
)

class ContactForm(BTk):
    def __init__(self):
        super().__init__(title="Contact Form", geometry="500x600")
        self.create_form()
    
    def create_form(self):
        # Main container
        container = BTkFrame(self)
        container.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Title
        BTkLabel(container, text="Contact Information", 
                font_size=18).pack(pady=(0, 20))
        
        # Name fields
        name_frame = BTkFrame(container)
        name_frame.pack(fill="x", pady=10)
        
        BTkLabel(name_frame, text="Full Name *").pack(anchor="w")
        self.name_entry = BTkEntry(name_frame, placeholder_text="Enter your full name")
        self.name_entry.pack(fill="x", pady=(5, 0))
        
        # Email field
        email_frame = BTkFrame(container)
        email_frame.pack(fill="x", pady=10)
        
        BTkLabel(email_frame, text="Email Address *").pack(anchor="w")
        self.email_entry = BTkEntry(email_frame, placeholder_text="your.email@example.com")
        self.email_entry.pack(fill="x", pady=(5, 0))
        
        # Phone field
        phone_frame = BTkFrame(container)
        phone_frame.pack(fill="x", pady=10)
        
        BTkLabel(phone_frame, text="Phone Number").pack(anchor="w")
        self.phone_entry = BTkEntry(phone_frame, placeholder_text="+1 (555) 123-4567")
        self.phone_entry.pack(fill="x", pady=(5, 0))
        
        # Message field
        message_frame = BTkFrame(container)
        message_frame.pack(fill="both", expand=True, pady=10)
        
        BTkLabel(message_frame, text="Message *").pack(anchor="w")
        self.message_text = BTkTextEditor(message_frame, height=100)
        self.message_text.pack(fill="both", expand=True, pady=(5, 0))
        
        # Options
        options_frame = BTkFrame(container)
        options_frame.pack(fill="x", pady=10)
        
        self.newsletter_check = BTkCheckBox(options_frame, text="Subscribe to newsletter")
        self.newsletter_check.pack(anchor="w")
        
        self.marketing_check = BTkCheckBox(options_frame, text="Receive marketing emails")
        self.marketing_check.pack(anchor="w")
        
        # Buttons
        button_frame = BTkFrame(container)
        button_frame.pack(fill="x", pady=(20, 0))
        
        BTkButton(button_frame, text="Submit", style="primary",
                 command=self.submit_form).pack(side="right", padx=(10, 0))
        BTkButton(button_frame, text="Clear", style="secondary",
                 command=self.clear_form).pack(side="right")
    
    def validate_form(self):
        """Validate form inputs"""
        errors = []
        
        if not self.name_entry.get().strip():
            errors.append("Name is required")
        
        email = self.email_entry.get().strip()
        if not email:
            errors.append("Email is required")
        elif not BTkEntry.validate_email(email):
            errors.append("Invalid email format")
        
        if not self.message_text.get_text().strip():
            errors.append("Message is required")
        
        return errors
    
    def submit_form(self):
        errors = self.validate_form()
        
        if errors:
            error_msg = "Please fix the following errors:\n\n" + "\n".join(f"• {error}" for error in errors)
            BTkDialog.show_error("Validation Error", error_msg)
            return
        
        # Collect form data
        data = {
            'name': self.name_entry.get(),
            'email': self.email_entry.get(),
            'phone': self.phone_entry.get(),
            'message': self.message_text.get_text(),
            'newsletter': self.newsletter_check.get(),
            'marketing': self.marketing_check.get()
        }
        
        # Simulate form submission
        print("Form submitted:", data)
        BTkDialog.show_success("Success", "Thank you! Your message has been submitted.")
        self.clear_form()
    
    def clear_form(self):
        self.name_entry.clear()
        self.email_entry.clear()
        self.phone_entry.clear()
        self.message_text.set_text("")
        self.newsletter_check.deselect()
        self.marketing_check.deselect()

app = ContactForm()
app.mainloop()
```

### Settings Panel
```python
from bettertkinter import (
    BTk, BTkFrame, BTkLabel, BTkButton, BTkCheckBox,
    BTkSlider, BTkComboBox, BTkColorPicker
)
import json

class SettingsPanel(BTk):
    def __init__(self):
        super().__init__(title="Application Settings", geometry="600x700")
        self.settings = self.load_settings()
        self.create_settings_panel()
    
    def load_settings(self):
        """Load settings from file or return defaults"""
        try:
            with open("app_settings.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'theme': 'light',
                'notifications': True,
                'auto_save': True,
                'font_size': 12,
                'accent_color': '#0078D4',
                'language': 'English',
                'startup_behavior': 'restore_session'
            }
    
    def save_settings(self):
        """Save settings to file"""
        try:
            with open("app_settings.json", "w") as f:
                json.dump(self.settings, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving settings: {e}")
            return False
    
    def create_settings_panel(self):
        # Main scrollable container
        main_container = BTkFrame(self)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        BTkLabel(main_container, text="Application Settings", 
                font_size=18).pack(pady=(0, 20))
        
        # Appearance Section
        appearance_section = BTkFrame(main_container)
        appearance_section.pack(fill="x", pady=(0, 20))
        
        BTkLabel(appearance_section, text="Appearance", 
                font_size=14, text_color="#2E8B57").pack(anchor="w", pady=(5, 10))
        
        # Theme selection
        theme_frame = BTkFrame(appearance_section)
        theme_frame.pack(fill="x", pady=5)
        BTkLabel(theme_frame, text="Theme:").pack(side="left")
        
        self.theme_combo = BTkComboBox(
            theme_frame, 
            values=["light", "dark", "auto"],
            state="readonly"
        )
        self.theme_combo.set(self.settings['theme'])
        self.theme_combo.pack(side="right")
        
        # Font size
        font_frame = BTkFrame(appearance_section)
        font_frame.pack(fill="x", pady=5)
        BTkLabel(font_frame, text="Font Size:").pack(side="left")
        
        self.font_slider = BTkSlider(font_frame, from_=8, to=24)
        self.font_slider.set(self.settings['font_size'])
        self.font_slider.pack(side="right", fill="x", expand=True, padx=(20, 0))
        
        # Accent color
        color_frame = BTkFrame(appearance_section)
        color_frame.pack(fill="x", pady=5)
        BTkLabel(color_frame, text="Accent Color:").pack(anchor="w")
        
        self.color_picker = BTkColorPicker(
            color_frame,
            initial_color=self.settings['accent_color'],
            width=200,
            height=100,
            show_alpha=False
        )
        self.color_picker.pack(pady=5)
        
        # Behavior Section
        behavior_section = BTkFrame(main_container)
        behavior_section.pack(fill="x", pady=(0, 20))
        
        BTkLabel(behavior_section, text="Behavior", 
                font_size=14, text_color="#2E8B57").pack(anchor="w", pady=(5, 10))
        
        # Checkboxes for boolean settings
        self.notifications_check = BTkCheckBox(
            behavior_section, 
            text="Enable notifications"
        )
        self.notifications_check.pack(anchor="w", pady=2)
        if self.settings['notifications']:
            self.notifications_check.select()
        
        self.autosave_check = BTkCheckBox(
            behavior_section,
            text="Auto-save documents"
        )
        self.autosave_check.pack(anchor="w", pady=2)
        if self.settings['auto_save']:
            self.autosave_check.select()
        
        # Startup behavior
        startup_frame = BTkFrame(behavior_section)
        startup_frame.pack(fill="x", pady=10)
        BTkLabel(startup_frame, text="On Startup:").pack(side="left")
        
        self.startup_combo = BTkComboBox(
            startup_frame,
            values=["restore_session", "show_welcome", "blank_document"],
            state="readonly"
        )
        self.startup_combo.set(self.settings['startup_behavior'])
        self.startup_combo.pack(side="right")
        
        # Language Section
        language_section = BTkFrame(main_container)
        language_section.pack(fill="x", pady=(0, 20))
        
        BTkLabel(language_section, text="Language & Region", 
                font_size=14, text_color="#2E8B57").pack(anchor="w", pady=(5, 10))
        
        lang_frame = BTkFrame(language_section)
        lang_frame.pack(fill="x", pady=5)
        BTkLabel(lang_frame, text="Language:").pack(side="left")
        
        self.language_combo = BTkComboBox(
            lang_frame,
            values=["English", "Spanish", "French", "German", "Chinese", "Japanese"],
            state="readonly"
        )
        self.language_combo.set(self.settings['language'])
        self.language_combo.pack(side="right")
        
        # Action Buttons
        button_frame = BTkFrame(main_container)
        button_frame.pack(fill="x", pady=(20, 0))
        
        BTkButton(button_frame, text="Apply", style="primary",
                 command=self.apply_settings).pack(side="right", padx=(10, 0))
        BTkButton(button_frame, text="Reset to Defaults", style="warning",
                 command=self.reset_defaults).pack(side="right", padx=(10, 0))
        BTkButton(button_frame, text="Cancel", style="secondary",
                 command=self.cancel_changes).pack(side="right")
    
    def apply_settings(self):
        """Apply current settings"""
        # Update settings dictionary
        self.settings.update({
            'theme': self.theme_combo.get(),
            'font_size': int(self.font_slider.get()),
            'accent_color': self.color_picker.get_color("hex"),
            'notifications': self.notifications_check.get(),
            'auto_save': self.autosave_check.get(),
            'startup_behavior': self.startup_combo.get(),
            'language': self.language_combo.get()
        })
        
        # Apply theme changes immediately
        if self.settings['theme'] != self.current_theme:
            self.configure_theme(self.settings['theme'])
        
        # Save to file
        if self.save_settings():
            BTkDialog.show_success("Settings Applied", "Your settings have been saved successfully!")
        else:
            BTkDialog.show_error("Error", "Failed to save settings.")
    
    def reset_defaults(self):
        """Reset all settings to default values"""
        result = BTkDialog.ask_yes_no("Reset Settings", 
                                     "Are you sure you want to reset all settings to default values?")
        
        if result == "Yes":
            # Reset to defaults
            defaults = {
                'theme': 'light',
                'notifications': True,
                'auto_save': True,
                'font_size': 12,
                'accent_color': '#0078D4',
                'language': 'English',
                'startup_behavior': 'restore_session'
            }
            
            # Update UI
            self.theme_combo.set(defaults['theme'])
            self.font_slider.set(defaults['font_size'])
            self.color_picker.set_color(defaults['accent_color'])
            self.notifications_check.select() if defaults['notifications'] else self.notifications_check.deselect()
            self.autosave_check.select() if defaults['auto_save'] else self.autosave_check.deselect()
            self.startup_combo.set(defaults['startup_behavior'])
            self.language_combo.set(defaults['language'])
            
            self.settings = defaults
    
    def cancel_changes(self):
        """Close without saving changes"""
        self.destroy()

app = SettingsPanel()
app.mainloop()
```

## 📊 Dashboard Examples

### Analytics Dashboard
```python
from bettertkinter import (
    BTk, BTkFrame, BTkLabel, BTkButton, BTkProgressBar,
    BTkCanvas, BTkNavBar
)
import random
import threading
import time

class AnalyticsDashboard(BTk):
    def __init__(self):
        super().__init__(title="Analytics Dashboard", geometry="1000x700")
        self.data = {
            'users': 1234,
            'revenue': 45678,
            'conversions': 89,
            'bounce_rate': 23.5
        }
        
        self.create_dashboard()
        self.start_data_updates()
    
    def create_dashboard(self):
        # Navigation bar
        nav_items = ["Overview", "Users", "Revenue", "Reports", "Settings"]
        self.navbar = BTkNavBar(self, items=nav_items, orientation="horizontal")
        self.navbar.pack(fill="x", padx=10, pady=(10, 0))
        self.navbar.set_active(0)  # Set "Overview" as active
        
        # Main content area
        content_frame = BTkFrame(self)
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Top metrics row
        metrics_frame = BTkFrame(content_frame)
        metrics_frame.pack(fill="x", pady=(0, 20))
        
        self.create_metric_cards(metrics_frame)
        
        # Charts row
        charts_frame = BTkFrame(content_frame)
        charts_frame.pack(fill="both", expand=True)
        
        # Left chart
        left_chart_frame = BTkFrame(charts_frame)
        left_chart_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        BTkLabel(left_chart_frame, text="Revenue Trend", 
                font_size=14).pack(pady=10)
        
        self.revenue_canvas = BTkCanvas(left_chart_frame, height=200)
        self.revenue_canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Right chart
        right_chart_frame = BTkFrame(charts_frame)
        right_chart_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        BTkLabel(right_chart_frame, text="User Activity", 
                font_size=14).pack(pady=10)
        
        self.activity_canvas = BTkCanvas(right_chart_frame, height=200)
        self.activity_canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Initial chart drawing
        self.draw_revenue_chart()
        self.draw_activity_chart()
    
    def create_metric_cards(self, parent):
        """Create metric cards for key statistics"""
        metrics = [
            ("Total Users", self.data['users'], "#2E8B57", "👥"),
            ("Revenue", f"${self.data['revenue']:,}", "#FF6B35", "💰"),
            ("Conversions", f"{self.data['conversions']}%", "#4169E1", "🎯"),
            ("Bounce Rate", f"{self.data['bounce_rate']}%", "#DC143C", "📊")
        ]
        
        self.metric_widgets = {}
        
        for title, value, color, icon in metrics:
            card_frame = BTkFrame(parent, corner_radius=10)
            card_frame.pack(side="left", fill="both", expand=True, padx=5)
            
            # Icon and title
            header_frame = BTkFrame(card_frame)
            header_frame.pack(fill="x", padx=15, pady=(15, 5))
            
            BTkLabel(header_frame, text=icon, font_size=20).pack(side="left")
            BTkLabel(header_frame, text=title, font_size=12, 
                    text_color="#666666").pack(side="left", padx=(10, 0))
            
            # Value
            value_label = BTkLabel(card_frame, text=str(value), 
                                  font_size=24, text_color=color)
            value_label.pack(pady=(0, 15))
            
            # Store reference for updates
            self.metric_widgets[title] = value_label
            
            # Progress indicator (for demonstration)
            progress = BTkProgressBar(card_frame, width=150, height=4)
            progress.pack(pady=(0, 15))
            progress.set_value(random.randint(60, 95))
    
    def draw_revenue_chart(self):
        """Draw a simple revenue trend chart"""
        self.revenue_canvas.delete("all")
        
        width = self.revenue_canvas.winfo_width() or 300
        height = self.revenue_canvas.winfo_height() or 150
        
        # Generate sample data
        points = []
        for i in range(10):
            x = (i / 9) * (width - 40) + 20
            y = height - 20 - (random.random() * (height - 40))
            points.extend([x, y])
        
        # Draw line chart
        if len(points) >= 4:
            self.revenue_canvas.create_line(
                points, 
                fill="#2E8B57", 
                width=3, 
                smooth=True
            )
            
            # Draw points
            for i in range(0, len(points), 2):
                x, y = points[i], points[i+1]
                self.revenue_canvas.create_oval(
                    x-4, y-4, x+4, y+4,
                    fill="#2E8B57",
                    outline="white",
                    width=2
                )
        
        # Axes
        self.revenue_canvas.create_line(20, height-20, width-20, height-20, 
                                       fill="#CCCCCC", width=1)  # X-axis
        self.revenue_canvas.create_line(20, 20, 20, height-20, 
                                       fill="#CCCCCC", width=1)  # Y-axis
    
    def draw_activity_chart(self):
        """Draw a simple bar chart for user activity"""
        self.activity_canvas.delete("all")
        
        width = self.activity_canvas.winfo_width() or 300
        height = self.activity_canvas.winfo_height() or 150
        
        # Sample data for days of week
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        values = [random.randint(50, 100) for _ in days]
        
        bar_width = (width - 40) // len(days) - 10
        max_value = max(values)
        
        # Draw bars
        for i, (day, value) in enumerate(zip(days, values)):
            x = 30 + i * (bar_width + 10)
            bar_height = (value / max_value) * (height - 60)
            y = height - 30 - bar_height
            
            # Bar
            self.activity_canvas.create_rectangle(
                x, y, x + bar_width, height - 30,
                fill="#4169E1",
                outline=""
            )
            
            # Label
            self.activity_canvas.create_text(
                x + bar_width // 2, height - 15,
                text=day,
                fill="#666666",
                font=("Arial", 8)
            )
            
            # Value
            self.activity_canvas.create_text(
                x + bar_width // 2, y - 10,
                text=str(value),
                fill="#333333",
                font=("Arial", 8)
            )
    
    def update_data(self):
        """Simulate real-time data updates"""
        # Update metrics with small random changes
        self.data['users'] += random.randint(-5, 15)
        self.data['revenue'] += random.randint(-100, 500)
        self.data['conversions'] += random.uniform(-0.5, 1.0)
        self.data['bounce_rate'] += random.uniform(-0.3, 0.3)
        
        # Ensure values stay reasonable
        self.data['users'] = max(1000, self.data['users'])
        self.data['revenue'] = max(40000, self.data['revenue'])
        self.data['conversions'] = max(75, min(95, self.data['conversions']))
        self.data['bounce_rate'] = max(15, min(35, self.data['bounce_rate']))
        
        # Update UI in main thread
        self.after(0, self.refresh_display)
    
    def refresh_display(self):
        """Refresh the display with updated data"""
        # Update metric cards
        metrics_map = {
            "Total Users": self.data['users'],
            "Revenue": f"${self.data['revenue']:,}",
            "Conversions": f"{self.data['conversions']:.1f}%",
            "Bounce Rate": f"{self.data['bounce_rate']:.1f}%"
        }
        
        for title, value in metrics_map.items():
            if title in self.metric_widgets:
                self.metric_widgets[title].configure(text=str(value))
        
        # Redraw charts
        self.draw_revenue_chart()
        self.draw_activity_chart()
    
    def start_data_updates(self):
        """Start background data updates"""
        def update_loop():
            while True:
                time.sleep(5)  # Update every 5 seconds
                if self.winfo_exists():
                    self.update_data()
                else:
                    break
        
        thread = threading.Thread(target=update_loop, daemon=True)
        thread.start()

app = AnalyticsDashboard()
app.mainloop()
```

## 🎮 Interactive Examples

### Color Picker Application
```python
from bettertkinter import (
    BTk, BTkFrame, BTkLabel, BTkButton, 
    BTkColorPicker, BTkEntry, BTkCanvas
)

class ColorPickerApp(BTk):
    def __init__(self):
        super().__init__(title="Color Picker Studio", geometry="800x600")
        self.selected_colors = []
        self.create_ui()
    
    def create_ui(self):
        # Main container
        container = BTkFrame(self)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        BTkLabel(container, text="Color Picker Studio", 
                font_size=20).pack(pady=(0, 20))
        
        # Top section - color picker and preview
        top_frame = BTkFrame(container)
        top_frame.pack(fill="x", pady=(0, 20))
        
        # Color picker
        picker_frame = BTkFrame(top_frame)
        picker_frame.pack(side="left", padx=(0, 20))
        
        BTkLabel(picker_frame, text="Select Color", font_size=14).pack(pady=(0, 10))
        
        self.color_picker = BTkColorPicker(
            picker_frame,
            initial_color="#FF6B35",
            width=300,
            height=250,
            show_alpha=True
        )
        self.color_picker.pack()
        self.color_picker.bind_color_change(self.on_color_change)
        
        # Color info panel
        info_frame = BTkFrame(top_frame)
        info_frame.pack(side="right", fill="both", expand=True)
        
        BTkLabel(info_frame, text="Color Information", font_size=14).pack(pady=(0, 10))
        
        # Color preview
        self.preview_canvas = BTkCanvas(info_frame, width=150, height=150)
        self.preview_canvas.pack(pady=(0, 15))
        
        # Color values
        self.hex_label = BTkLabel(info_frame, text="HEX: #FF6B35", font_size=12)
        self.hex_label.pack(anchor="w", pady=2)
        
        self.rgb_label = BTkLabel(info_frame, text="RGB: (255, 107, 53)", font_size=12)
        self.rgb_label.pack(anchor="w", pady=2)
        
        self.hsv_label = BTkLabel(info_frame, text="HSV: (14°, 79%, 100%)", font_size=12)
        self.hsv_label.pack(anchor="w", pady=2)
        
        # Add to palette button
        BTkButton(info_frame, text="Add to Palette", style="primary",
                 command=self.add_to_palette).pack(pady=15, fill="x")
        
        # Color palette section
        palette_frame = BTkFrame(container)
        palette_frame.pack(fill="both", expand=True)
        
        BTkLabel(palette_frame, text="Color Palette", font_size=14).pack(anchor="w", pady=(0, 10))
        
        # Palette display
        self.palette_canvas = BTkCanvas(palette_frame, height=100)
        self.palette_canvas.pack(fill="x", pady=(0, 10))
        
        # Palette controls
        palette_controls = BTkFrame(palette_frame)
        palette_controls.pack(fill="x")
        
        BTkButton(palette_controls, text="Clear Palette", style="warning",
                 command=self.clear_palette).pack(side="left")
        BTkButton(palette_controls, text="Export Palette", style="secondary",
                 command=self.export_palette).pack(side="left", padx=(10, 0))
        BTkButton(palette_controls, text="Random Colors", style="secondary",
                 command=self.generate_random_palette).pack(side="left", padx=(10, 0))
        
        # Initialize display
        self.update_preview()
        self.update_palette_display()
    
    def on_color_change(self, color):
        """Handle color picker changes"""
        self.update_preview()
        self.update_color_info()
    
    def update_preview(self):
        """Update the color preview"""
        self.preview_canvas.delete("all")
        
        color = self.color_picker.get_color("hex")
        
        # Main color rectangle
        self.preview_canvas.create_rectangle(
            10, 10, 140, 140,
            fill=color,
            outline="#CCCCCC",
            width=1
        )
        
        # Add some pattern for better visualization
        for i in range(0, 130, 20):
            for j in range(0, 130, 20):
                if (i + j) % 40 == 0:
                    self.preview_canvas.create_rectangle(
                        10 + i, 10 + j, 10 + i + 10, 10 + j + 10,
                        fill="white",
                        stipple="gray50",
                        outline=""
                    )
    
    def update_color_info(self):
        """Update color information display"""
        hex_color = self.color_picker.get_color("hex")
        rgb_color = self.color_picker.get_color("rgb")
        hsv_color = self.color_picker.get_color("hsv")
        
        self.hex_label.configure(text=f"HEX: {hex_color}")
        self.rgb_label.configure(text=f"RGB: {rgb_color}")
        self.hsv_label.configure(text=f"HSV: ({hsv_color[0]:.0f}°, {hsv_color[1]:.0f}%, {hsv_color[2]:.0f}%)")
    
    def add_to_palette(self):
        """Add current color to palette"""
        current_color = self.color_picker.get_color("hex")
        if current_color not in self.selected_colors:
            self.selected_colors.append(current_color)
            self.update_palette_display()
            print(f"Added {current_color} to palette")
    
    def update_palette_display(self):
        """Update the palette display"""
        self.palette_canvas.delete("all")
        
        if not self.selected_colors:
            self.palette_canvas.create_text(
                400, 50, text="No colors in palette",
                fill="#999999", font=("Arial", 12)
            )
            return
        
        canvas_width = self.palette_canvas.winfo_width() or 600
        color_width = min(60, canvas_width // max(1, len(self.selected_colors)))
        
        for i, color in enumerate(self.selected_colors):
            x = i * color_width + 10
            
            # Color swatch
            self.palette_canvas.create_rectangle(
                x, 20, x + color_width - 5, 80,
                fill=color,
                outline="#CCCCCC",
                width=1,
                tags=f"color_{i}"
            )
            
            # Color label
            self.palette_canvas.create_text(
                x + (color_width - 5) // 2, 90,
                text=color,
                fill="#333333",
                font=("Arial", 8)
            )
            
            # Click handler
            self.palette_canvas.tag_bind(f"color_{i}", "<Button-1>", 
                                       lambda e, c=color: self.select_palette_color(c))
    
    def select_palette_color(self, color):
        """Select a color from the palette"""
        self.color_picker.set_color(color, "hex")
    
    def clear_palette(self):
        """Clear the color palette"""
        result = BTkDialog.ask_yes_no("Clear Palette", "Are you sure you want to clear the palette?")
        if result == "Yes":
            self.selected_colors.clear()
            self.update_palette_display()
    
    def export_palette(self):
        """Export palette to different formats"""
        if not self.selected_colors:
            BTkDialog.show_warning("Empty Palette", "No colors to export!")
            return
        
        # Create export dialog
        export_text = "Color Palette Export:\n\n"
        
        # Add different formats
        export_text += "HEX Colors:\n"
        for color in self.selected_colors:
            export_text += f"{color}\n"
        
        export_text += "\nRGB Colors:\n"
        for color in self.selected_colors:
            rgb = self.color_picker.hex_to_rgb(color)
            export_text += f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})\n"
        
        export_text += "\nCSS Variables:\n"
        for i, color in enumerate(self.selected_colors):
            export_text += f"--color-{i+1}: {color};\n"
        
        # Show export dialog
        BTkDialog.show_info("Exported Palette", export_text)
    
    def generate_random_palette(self):
        """Generate a random color palette"""
        import random
        
        self.selected_colors.clear()
        
        # Generate 6 random colors
        for _ in range(6):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            hex_color = f"#{r:02X}{g:02X}{b:02X}"
            self.selected_colors.append(hex_color)
        
        self.update_palette_display()

app = ColorPickerApp()
app.mainloop()
```

## 🗃️ Data Management Examples

### Todo List Manager
```python
from bettertkinter import (
    BTk, BTkFrame, BTkLabel, BTkButton, BTkEntry,
    BTkCheckBox, BTkDialog, BTkTextEditor
)
import json
from datetime import datetime

class TodoManager(BTk):
    def __init__(self):
        super().__init__(title="Todo List Manager", geometry="700x800")
        self.todos = self.load_todos()
        self.create_ui()
        self.refresh_todo_list()
    
    def load_todos(self):
        """Load todos from file"""
        try:
            with open("todos.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_todos(self):
        """Save todos to file"""
        try:
            with open("todos.json", "w") as f:
                json.dump(self.todos, f, indent=2)
        except Exception as e:
            print(f"Error saving todos: {e}")
    
    def create_ui(self):
        # Header
        header_frame = BTkFrame(self)
        header_frame.pack(fill="x", padx=20, pady=(20, 0))
        
        BTkLabel(header_frame, text="📝 Todo List Manager", 
                font_size=20).pack(pady=10)
        
        # Stats
        self.stats_frame = BTkFrame(header_frame)
        self.stats_frame.pack(fill="x", pady=(0, 10))
        
        self.total_label = BTkLabel(self.stats_frame, text="Total: 0", font_size=12)
        self.total_label.pack(side="left")
        
        self.completed_label = BTkLabel(self.stats_frame, text="Completed: 0", font_size=12)
        self.completed_label.pack(side="left", padx=(20, 0))
        
        self.pending_label = BTkLabel(self.stats_frame, text="Pending: 0", font_size=12)
        self.pending_label.pack(side="left", padx=(20, 0))
        
        # Add todo section
        add_frame = BTkFrame(self)
        add_frame.pack(fill="x", padx=20, pady=10)
        
        BTkLabel(add_frame, text="Add New Todo:", font_size=14).pack(anchor="w", pady=(5, 5))
        
        input_frame = BTkFrame(add_frame)
        input_frame.pack(fill="x", pady=(0, 10))
        
        self.todo_entry = BTkEntry(input_frame, placeholder_text="Enter todo item...")
        self.todo_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        BTkButton(input_frame, text="Add Todo", style="primary",
                 command=self.add_todo).pack(side="right")
        
        # Priority and category
        options_frame = BTkFrame(add_frame)
        options_frame.pack(fill="x")
        
        BTkLabel(options_frame, text="Priority:").pack(side="left")
        self.priority_combo = BTkComboBox(options_frame, 
                                         values=["Low", "Medium", "High"],
                                         state="readonly", width=100)
        self.priority_combo.set("Medium")
        self.priority_combo.pack(side="left", padx=(5, 15))
        
        BTkLabel(options_frame, text="Category:").pack(side="left")
        self.category_entry = BTkEntry(options_frame, placeholder_text="Category", width=120)
        self.category_entry.pack(side="left", padx=(5, 0))
        
        # Filter section
        filter_frame = BTkFrame(self)
        filter_frame.pack(fill="x", padx=20, pady=(0, 10))
        
        BTkLabel(filter_frame, text="Filter:", font_size=12).pack(side="left")
        
        self.show_all_btn = BTkButton(filter_frame, text="All", style="secondary",
                                     command=lambda: self.filter_todos("all"))
        self.show_all_btn.pack(side="left", padx=(10, 5))
        
        self.show_pending_btn = BTkButton(filter_frame, text="Pending", style="secondary",
                                         command=lambda: self.filter_todos("pending"))
        self.show_pending_btn.pack(side="left", padx=5)
        
        self.show_completed_btn = BTkButton(filter_frame, text="Completed", style="secondary",
                                           command=lambda: self.filter_todos("completed"))
        self.show_completed_btn.pack(side="left", padx=5)
        
        # Todo list
        list_frame = BTkFrame(self)
        list_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        BTkLabel(list_frame, text="Todo Items:", font_size=14).pack(anchor="w", pady=(5, 10))
        
        # Scrollable todo container
        self.todo_container = BTkFrame(list_frame)
        self.todo_container.pack(fill="both", expand=True)
        
        # Bind Enter key to add todo
        self.todo_entry.bind("<Return>", lambda e: self.add_todo())
        
        self.current_filter = "all"
    
    def add_todo(self):
        """Add a new todo item"""
        text = self.todo_entry.get().strip()
        if not text:
            BTkDialog.show_warning("Empty Todo", "Please enter a todo item!")
            return
        
        todo = {
            'id': len(self.todos) + 1,
            'text': text,
            'completed': False,
            'priority': self.priority_combo.get(),
            'category': self.category_entry.get().strip() or "General",
            'created': datetime.now().isoformat(),
            'completed_date': None
        }
        
        self.todos.append(todo)
        self.todo_entry.clear()
        self.category_entry.clear()
        self.save_todos()
        self.refresh_todo_list()
    
    def toggle_todo(self, todo_id):
        """Toggle completion status of a todo"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = not todo['completed']
                todo['completed_date'] = datetime.now().isoformat() if todo['completed'] else None
                break
        
        self.save_todos()
        self.refresh_todo_list()
    
    def delete_todo(self, todo_id):
        """Delete a todo item"""
        result = BTkDialog.ask_yes_no("Delete Todo", "Are you sure you want to delete this todo?")
        if result == "Yes":
            self.todos = [todo for todo in self.todos if todo['id'] != todo_id]
            self.save_todos()
            self.refresh_todo_list()
    
    def edit_todo(self, todo_id):
        """Edit a todo item"""
        todo = next((t for t in self.todos if t['id'] == todo_id), None)
        if not todo:
            return
        
        # Create edit dialog
        from bettertkinter.dialogs import InputDialog
        new_text = InputDialog.get_input(
            self, 
            title="Edit Todo",
            prompt="Edit todo text:",
            default=todo['text']
        )
        
        if new_text and new_text != todo['text']:
            todo['text'] = new_text
            self.save_todos()
            self.refresh_todo_list()
    
    def filter_todos(self, filter_type):
        """Filter todos by type"""
        self.current_filter = filter_type
        self.refresh_todo_list()
        
        # Update button styles
        buttons = [self.show_all_btn, self.show_pending_btn, self.show_completed_btn]
        for btn in buttons:
            btn.configure(style="secondary")
        
        if filter_type == "all":
            self.show_all_btn.configure(style="primary")
        elif filter_type == "pending":
            self.show_pending_btn.configure(style="primary")
        elif filter_type == "completed":
            self.show_completed_btn.configure(style="primary")
    
    def refresh_todo_list(self):
        """Refresh the todo list display"""
        # Clear current items
        for widget in self.todo_container.winfo_children():
            widget.destroy()
        
        # Filter todos
        if self.current_filter == "pending":
            filtered_todos = [t for t in self.todos if not t['completed']]
        elif self.current_filter == "completed":
            filtered_todos = [t for t in self.todos if t['completed']]
        else:
            filtered_todos = self.todos
        
        # Sort by priority and creation date
        priority_order = {"High": 0, "Medium": 1, "Low": 2}
        filtered_todos.sort(key=lambda x: (x['completed'], priority_order.get(x['priority'], 1), x['created']))
        
        # Display todos
        if not filtered_todos:
            no_items_label = BTkLabel(self.todo_container, 
                                    text="No todos to display", 
                                    font_size=14, text_color="#999999")
            no_items_label.pack(pady=50)
        else:
            for todo in filtered_todos:
                self.create_todo_item(todo)
        
        # Update stats
        self.update_stats()
    
    def create_todo_item(self, todo):
        """Create a todo item widget"""
        item_frame = BTkFrame(self.todo_container, corner_radius=8)
        item_frame.pack(fill="x", pady=5, padx=5)
        
        # Left section - checkbox and text
        left_frame = BTkFrame(item_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=15, pady=10)
        
        # Checkbox
        check_var = BTkCheckBox(left_frame, text="", 
                               command=lambda: self.toggle_todo(todo['id']))
        check_var.pack(side="left", padx=(0, 10))
        if todo['completed']:
            check_var.select()
        
        # Todo text and details
        text_frame = BTkFrame(left_frame)
        text_frame.pack(side="left", fill="both", expand=True)
        
        # Main text
        text_style = {"font_size": 14}
        if todo['completed']:
            text_style["text_color"] = "#999999"
        
        todo_label = BTkLabel(text_frame, text=todo['text'], **text_style)
        todo_label.pack(anchor="w")
        
        # Details
        details = f"Priority: {todo['priority']} | Category: {todo['category']}"
        if todo['completed'] and todo['completed_date']:
            completed_date = datetime.fromisoformat(todo['completed_date']).strftime("%Y-%m-%d %H:%M")
            details += f" | Completed: {completed_date}"
        
        details_label = BTkLabel(text_frame, text=details, 
                               font_size=10, text_color="#666666")
        details_label.pack(anchor="w")
        
        # Right section - action buttons
        right_frame = BTkFrame(item_frame)
        right_frame.pack(side="right", padx=15, pady=10)
        
        BTkButton(right_frame, text="Edit", style="secondary", width=60,
                 command=lambda: self.edit_todo(todo['id'])).pack(side="top", pady=2)
        BTkButton(right_frame, text="Delete", style="danger", width=60,
                 command=lambda: self.delete_todo(todo['id'])).pack(side="top", pady=2)
    
    def update_stats(self):
        """Update todo statistics"""
        total = len(self.todos)
        completed = sum(1 for todo in self.todos if todo['completed'])
        pending = total - completed
        
        self.total_label.configure(text=f"Total: {total}")
        self.completed_label.configure(text=f"Completed: {completed}")
        self.pending_label.configure(text=f"Pending: {pending}")

app = TodoManager()
app.mainloop()
```

## 🎨 Creative Examples

### Drawing Application
```python
from bettertkinter import (
    BTk, BTkFrame, BTkLabel, BTkButton, BTkCanvas,
    BTkSlider, BTkColorPicker, BTkComboBox
)

class DrawingApp(BTk):
    def __init__(self):
        super().__init__(title="Drawing Studio", geometry="1000x700")
        
        self.drawing_mode = "pen"
        self.brush_size = 5
        self.current_color = "#000000"
        self.shapes = []
        
        self.create_ui()
        self.setup_canvas_events()
    
    def create_ui(self):
        # Tool panel on the left
        tools_frame = BTkFrame(self, width=250)
        tools_frame.pack(side="left", fill="y", padx=(10, 5), pady=10)
        tools_frame.pack_propagate(False)
        
        BTkLabel(tools_frame, text="🎨 Drawing Tools", font_size=16).pack(pady=15)
        
        # Drawing tools
        BTkLabel(tools_frame, text="Tool:", font_size=12).pack(anchor="w", padx=10, pady=(10, 5))
        
        tools_buttons_frame = BTkFrame(tools_frame)
        tools_buttons_frame.pack(fill="x", padx=10, pady=(0, 15))
        
        self.pen_btn = BTkButton(tools_buttons_frame, text="✏️ Pen", style="primary",
                                command=lambda: self.set_tool("pen"))
        self.pen_btn.pack(fill="x", pady=2)
        
        self.eraser_btn = BTkButton(tools_buttons_frame, text="🧹 Eraser", style="secondary",
                                   command=lambda: self.set_tool("eraser"))
        self.eraser_btn.pack(fill="x", pady=2)
        
        self.line_btn = BTkButton(tools_buttons_frame, text="📏 Line", style="secondary",
                                 command=lambda: self.set_tool("line"))
        self.line_btn.pack(fill="x", pady=2)
        
        self.rectangle_btn = BTkButton(tools_buttons_frame, text="⬜ Rectangle", style="secondary",
                                      command=lambda: self.set_tool("rectangle"))
        self.rectangle_btn.pack(fill="x", pady=2)
        
        self.circle_btn = BTkButton(tools_buttons_frame, text="⭕ Circle", style="secondary",
                                   command=lambda: self.set_tool("circle"))
        self.circle_btn.pack(fill="x", pady=2)
        
        # Brush size
        BTkLabel(tools_frame, text="Brush Size:", font_size=12).pack(anchor="w", padx=10, pady=(10, 5))
        
        self.size_slider = BTkSlider(tools_frame, from_=1, to=50, command=self.on_size_change)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(fill="x", padx=10, pady=(0, 15))
        
        self.size_label = BTkLabel(tools_frame, text=f"Size: {self.brush_size}px", font_size=10)
        self.size_label.pack(padx=10)
        
        # Color picker
        BTkLabel(tools_frame, text="Color:", font_size=12).pack(anchor="w", padx=10, pady=(15, 5))
        
        self.color_picker = BTkColorPicker(
            tools_frame,
            initial_color=self.current_color,
            width=200,
            height=150,
            show_alpha=False
        )
        self.color_picker.pack(padx=10, pady=(0, 15))
        self.color_picker.bind_color_change(self.on_color_change)
        
        # Action buttons
        actions_frame = BTkFrame(tools_frame)
        actions_frame.pack(fill="x", padx=10, pady=15)
        
        BTkButton(actions_frame, text="🗑️ Clear Canvas", style="warning",
                 command=self.clear_canvas).pack(fill="x", pady=2)
        BTkButton(actions_frame, text="↶ Undo", style="secondary",
                 command=self.undo).pack(fill="x", pady=2)
        BTkButton(actions_frame, text="💾 Save", style="success",
                 command=self.save_drawing).pack(fill="x", pady=2)
        
        # Canvas area
        canvas_frame = BTkFrame(self)
        canvas_frame.pack(side="right", fill="both", expand=True, padx=(5, 10), pady=10)
        
        # Canvas with white background
        self.canvas = BTkCanvas(canvas_frame, bg="white", cursor="crosshair")
        self.canvas.pack(fill="both", expand=True)
        
        # Drawing state variables
        self.last_x = None
        self.last_y = None
        self.current_shape = None
        self.shape_start_x = None
        self.shape_start_y = None
    
    def setup_canvas_events(self):
        """Setup canvas mouse events"""
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Motion>", self.on_motion)
    
    def set_tool(self, tool):
        """Set the current drawing tool"""
        self.drawing_mode = tool
        
        # Update button styles
        buttons = [self.pen_btn, self.eraser_btn, self.line_btn, 
                  self.rectangle_btn, self.circle_btn]
        for btn in buttons:
            btn.configure(style="secondary")
        
        # Highlight active tool
        if tool == "pen":
            self.pen_btn.configure(style="primary")
            self.canvas.configure(cursor="pencil")
        elif tool == "eraser":
            self.eraser_btn.configure(style="primary")
            self.canvas.configure(cursor="dotbox")
        elif tool == "line":
            self.line_btn.configure(style="primary")
            self.canvas.configure(cursor="crosshair")
        elif tool == "rectangle":
            self.rectangle_btn.configure(style="primary")
            self.canvas.configure(cursor="crosshair")
        elif tool == "circle":
            self.circle_btn.configure(style="primary")
            self.canvas.configure(cursor="crosshair")
    
    def on_size_change(self, value):
        """Handle brush size change"""
        self.brush_size = int(value)
        self.size_label.configure(text=f"Size: {self.brush_size}px")
    
    def on_color_change(self, color):
        """Handle color change"""
        self.current_color = color
    
    def on_click(self, event):
        """Handle mouse click"""
        self.last_x = event.x
        self.last_y = event.y
        
        if self.drawing_mode in ["line", "rectangle", "circle"]:
            self.shape_start_x = event.x
            self.shape_start_y = event.y
        elif self.drawing_mode == "pen":
            # Start drawing
            pass
        elif self.drawing_mode == "eraser":
            # Start erasing
            self.erase_at_point(event.x, event.y)
    
    def on_drag(self, event):
        """Handle mouse drag"""
        if self.drawing_mode == "pen":
            if self.last_x and self.last_y:
                # Draw line from last position to current
                line_id = self.canvas.create_line(
                    self.last_x, self.last_y, event.x, event.y,
                    width=self.brush_size,
                    fill=self.current_color,
                    capstyle="round",
                    smooth=True
                )
                self.shapes.append(("line", line_id))
            
            self.last_x = event.x
            self.last_y = event.y
            
        elif self.drawing_mode == "eraser":
            self.erase_at_point(event.x, event.y)
            
        elif self.drawing_mode in ["line", "rectangle", "circle"]:
            # Update preview shape
            if self.current_shape:
                self.canvas.delete(self.current_shape)
            
            if self.drawing_mode == "line":
                self.current_shape = self.canvas.create_line(
                    self.shape_start_x, self.shape_start_y, event.x, event.y,
                    width=self.brush_size,
                    fill=self.current_color,
                    capstyle="round"
                )
            elif self.drawing_mode == "rectangle":
                self.current_shape = self.canvas.create_rectangle(
                    self.shape_start_x, self.shape_start_y, event.x, event.y,
                    outline=self.current_color,
                    width=self.brush_size
                )
            elif self.drawing_mode == "circle":
                # Calculate radius for circle
                radius = ((event.x - self.shape_start_x) ** 2 + 
                         (event.y - self.shape_start_y) ** 2) ** 0.5
                self.current_shape = self.canvas.create_oval(
                    self.shape_start_x - radius, self.shape_start_y - radius,
                    self.shape_start_x + radius, self.shape_start_y + radius,
                    outline=self.current_color,
                    width=self.brush_size
                )
    
    def on_release(self, event):
        """Handle mouse release"""
        if self.drawing_mode in ["line", "rectangle", "circle"] and self.current_shape:
            # Finalize shape
            self.shapes.append((self.drawing_mode, self.current_shape))
            self.current_shape = None
        
        self.last_x = None
        self.last_y = None
    
    def on_motion(self, event):
        """Handle mouse motion (for cursor updates)"""
        pass
    
    def erase_at_point(self, x, y):
        """Erase drawing at specified point"""
        # Find items near the cursor
        items = self.canvas.find_overlapping(
            x - self.brush_size, y - self.brush_size,
            x + self.brush_size, y + self.brush_size
        )
        
        for item in items:
            # Remove from shapes list and delete
            self.shapes = [(shape_type, shape_id) for shape_type, shape_id in self.shapes 
                          if shape_id != item]
            self.canvas.delete(item)
    
    def clear_canvas(self):
        """Clear the entire canvas"""
        result = BTkDialog.ask_yes_no("Clear Canvas", 
                                     "Are you sure you want to clear the entire canvas?")
        if result == "Yes":
            self.canvas.delete("all")
            self.shapes.clear()
    
    def undo(self):
        """Undo the last drawing action"""
        if self.shapes:
            shape_type, shape_id = self.shapes.pop()
            self.canvas.delete(shape_id)
    
    def save_drawing(self):
        """Save the drawing"""
        try:
            # This would require PIL/Pillow for actual image saving
            BTkDialog.show_info("Save Drawing", 
                               "Save functionality would require PIL/Pillow integration.\n\n" +
                               f"Current drawing has {len(self.shapes)} shapes.")
        except Exception as e:
            BTkDialog.show_error("Save Error", f"Failed to save drawing: {str(e)}")

app = DrawingApp()
app.mainloop()
```

## 📋 Additional Resources

### Example Files Structure
```
examples/
├── basic/
│   ├── hello_world.py
│   ├── themed_window.py
│   └── simple_form.py
├── intermediate/
│   ├── calculator.py
│   ├── text_editor.py
│   └── image_viewer.py
├── advanced/
│   ├── dashboard.py
│   ├── drawing_app.py
│   └── database_manager.py
├── games/
│   ├── tic_tac_toe.py
│   ├── snake_game.py
│   └── puzzle_game.py
└── utilities/
    ├── file_organizer.py
    ├── system_monitor.py
    └── password_generator.py
```

### Running Examples

1. **Install BetterTkinter:**
   ```bash
   pip install bettertkinter
   ```

2. **Run any example:**
   ```bash
   python examples/basic/hello_world.py
   ```

3. **Modify and experiment:**
   - Copy example code
   - Modify colors, styles, layouts
   - Add new features
   - Combine multiple examples

### Learning Path

1. **Start with Basic Examples** - Learn component usage
2. **Progress to Forms** - Understand user input and validation
3. **Explore Dashboards** - Learn data visualization
4. **Try Interactive Apps** - Master event handling
5. **Build Creative Tools** - Combine multiple components
6. **Create Your Own Projects** - Apply learned concepts

---

**Ready to build amazing applications with BetterTkinter!** 🚀

For more information, see:
- [Installation Guide](../guides/installation.md)
- [Quick Start Guide](../guides/quickstart.md)
- [Component Documentation](../components/)
- [API Reference](../api/)
