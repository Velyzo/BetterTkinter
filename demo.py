import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import logging
import sys
import traceback
import threading
import time
from datetime import datetime
import os

# Configure comprehensive logging
def setup_logging():
    """Setup extreme logging configuration"""
    log_formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(filename)s:%(lineno)d | %(funcName)s() | %(message)s'
    )
    
    # File handler
    log_file = os.path.join(os.path.dirname(__file__), 'btk_demo.log')
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.INFO)
    
    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # Component-specific loggers
    loggers = [
        'BTkDemo', 'BTkDemo.UI', 'BTkDemo.Navigation', 'BTkDemo.Components',
        'BTkDemo.Events', 'BTkDemo.SystemTray', 'BTkDemo.ErrorHandler'
    ]
    
    for logger_name in loggers:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
    
    logging.info("=" * 80)
    logging.info("BetterTkinter Demo - Logging System Initialized")
    logging.info(f"Log file: {log_file}")
    logging.info("=" * 80)

# Setup logging first
setup_logging()

# Import BetterTkinter components with error handling
def safe_import_components():
    """Safely import all BetterTkinter components with detailed error logging"""
    logger = logging.getLogger('BTkDemo.Components')
    components = {}
    errors = []
    
    component_imports = {
        'BTk': 'bettertkinter.BTk',
        'BTkButton': 'bettertkinter.BTkButton',
        'BTkFrame': 'bettertkinter.BTkFrame', 
        'BTkLabel': 'bettertkinter.BTkLabel',
        'BTkEntry': 'bettertkinter.BTkEntry',
        'BTkCheckBox': 'bettertkinter.BTkCheckBox',
        'BTkProgressBar': 'bettertkinter.BTkProgressBar',
        'BTkNavBar': 'bettertkinter.BTkNavBar',
        'BTkColorPicker': 'bettertkinter.BTkColorPicker',
        'BTkDialog': 'bettertkinter.BTkDialog',
        'BTkSystemTray': 'bettertkinter.BTkSystemTray',
        'BTkSlider': 'bettertkinter.BTkSlider',
    }
    
    for component_name, import_path in component_imports.items():
        try:
            logger.debug(f"Importing {component_name} from {import_path}")
            module_path, class_name = import_path.rsplit('.', 1)
            module = __import__(module_path, fromlist=[class_name])
            component_class = getattr(module, class_name)
            components[component_name] = component_class
            logger.info(f"✅ Successfully imported {component_name}")
        except ImportError as e:
            error_msg = f"❌ ImportError for {component_name}: {e}"
            logger.error(error_msg)
            errors.append(error_msg)
        except AttributeError as e:
            error_msg = f"❌ AttributeError for {component_name}: {e}"
            logger.error(error_msg)
            errors.append(error_msg)
        except Exception as e:
            error_msg = f"❌ Unexpected error importing {component_name}: {e}"
            logger.exception(error_msg)
            errors.append(error_msg)
    
    logger.info(f"Import complete: {len(components)} successful, {len(errors)} errors")
    return components, errors

# Import components
COMPONENTS, IMPORT_ERRORS = safe_import_components()

class ErrorHandler:
    """Centralized error handling and logging"""
    
    def __init__(self):
        self.logger = logging.getLogger('BTkDemo.ErrorHandler')
        self.error_count = 0
        self.errors = []
    
    def handle_error(self, error, context="Unknown", show_dialog=False):
        """Handle an error with logging and optional user notification"""
        self.error_count += 1
        error_id = f"ERR-{self.error_count:04d}"
        
        error_info = {
            'id': error_id,
            'timestamp': datetime.now().isoformat(),
            'context': context,
            'error': str(error),
            'type': type(error).__name__,
            'traceback': traceback.format_exc()
        }
        
        self.errors.append(error_info)
        
        # Log the error
        self.logger.error(f"[{error_id}] Error in {context}: {error}")
        self.logger.debug(f"[{error_id}] Traceback:\n{error_info['traceback']}")
        
        # Show dialog if requested
        if show_dialog:
            try:
                messagebox.showerror(
                    f"Error {error_id}",
                    f"An error occurred in {context}:\n\n{error}\n\nCheck logs for details."
                )
            except Exception as dialog_error:
                self.logger.error(f"Failed to show error dialog: {dialog_error}")
        
        return error_id
    
    def get_error_summary(self):
        """Get a summary of all errors"""
        return f"Total Errors: {self.error_count}"

class LogDisplay:
    """Real-time log display widget"""
    
    def __init__(self, parent):
        self.logger = logging.getLogger('BTkDemo.LogDisplay')
        self.parent = parent
        self.setup_ui()
        self.setup_log_handler()
    
    def setup_ui(self):
        """Setup the log display UI"""
        try:
            self.frame = tk.Frame(self.parent, relief='sunken', bd=1)
            self.frame.pack(fill='both', expand=True, padx=5, pady=5)
            
            # Title
            title = tk.Label(self.frame, text="📋 Real-time Logs", 
                           font=('Segoe UI', 10, 'bold'), fg='#333')
            title.pack(anchor='w', padx=5, pady=(5, 0))
            
            # Log text area with scrollbar
            self.log_text = scrolledtext.ScrolledText(
                self.frame, 
                height=10,
                font=('Consolas', 8),
                bg='#1e1e1e',
                fg='#ffffff',
                insertbackground='white',
                selectbackground='#264f78',
                wrap=tk.WORD
            )
            self.log_text.pack(fill='both', expand=True, padx=5, pady=5)
            
            # Control buttons
            btn_frame = tk.Frame(self.frame)
            btn_frame.pack(fill='x', padx=5, pady=(0, 5))
            
            tk.Button(btn_frame, text="Clear", command=self.clear_logs,
                     font=('Segoe UI', 8)).pack(side='left', padx=(0, 5))
            
            tk.Button(btn_frame, text="Save Logs", command=self.save_logs,
                     font=('Segoe UI', 8)).pack(side='left')
            
            self.logger.info("Log display UI initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to setup log display UI: {e}")
            raise
    
    def setup_log_handler(self):
        """Setup custom log handler to display logs in real-time"""
        try:
            class TextHandler(logging.Handler):
                def __init__(self, text_widget, logger_ref):
                    super().__init__()
                    self.text_widget = text_widget
                    self.logger_ref = logger_ref
                
                def emit(self, record):
                    try:
                        msg = self.format(record)
                        
                        # Color coding based on log level
                        color = {
                            'DEBUG': '#888888',
                            'INFO': '#ffffff', 
                            'WARNING': '#ffaa00',
                            'ERROR': '#ff4444',
                            'CRITICAL': '#ff0000'
                        }.get(record.levelname, '#ffffff')
                        
                        # Thread-safe GUI update
                        def update_gui():
                            try:
                                self.text_widget.configure(state='normal')
                                self.text_widget.insert('end', msg + '\n')
                                self.text_widget.configure(state='disabled')
                                self.text_widget.see('end')
                            except tk.TclError:
                                pass  # Widget destroyed
                        
                        if self.text_widget.winfo_exists():
                            self.text_widget.after_idle(update_gui)
                            
                    except Exception as e:
                        # Avoid recursive logging errors
                        print(f"Log handler error: {e}")
            
            # Create and add the handler
            self.text_handler = TextHandler(self.log_text, self.logger)
            formatter = logging.Formatter('%(asctime)s | %(levelname)8s | %(name)s | %(message)s',
                                        datefmt='%H:%M:%S')
            self.text_handler.setFormatter(formatter)
            self.text_handler.setLevel(logging.INFO)
            
            # Add to root logger
            logging.getLogger().addHandler(self.text_handler)
            
            self.logger.info("Real-time log handler initialized")
            
        except Exception as e:
            self.logger.error(f"Failed to setup log handler: {e}")
    
    def clear_logs(self):
        """Clear the log display"""
        try:
            self.log_text.configure(state='normal')
            self.log_text.delete(1.0, 'end')
            self.log_text.configure(state='disabled')
            self.logger.info("Log display cleared")
        except Exception as e:
            self.logger.error(f"Failed to clear logs: {e}")
    
    def save_logs(self):
        """Save logs to file"""
        try:
            from tkinter import filedialog
            filename = filedialog.asksaveasfilename(
                defaultextension='.log',
                filetypes=[('Log files', '*.log'), ('Text files', '*.txt'), ('All files', '*.*')]
            )
            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    content = self.log_text.get(1.0, 'end')
                    f.write(content)
                self.logger.info(f"Logs saved to {filename}")
                messagebox.showinfo("Success", f"Logs saved to {filename}")
        except Exception as e:
            self.logger.error(f"Failed to save logs: {e}")
            messagebox.showerror("Error", f"Failed to save logs: {e}")

class ComponentTab:
    """Individual component demonstration tab"""
    
    def __init__(self, parent, component_name, component_class, error_handler):
        self.logger = logging.getLogger(f'BTkDemo.Tab.{component_name}')
        self.parent = parent
        self.component_name = component_name
        self.component_class = component_class
        self.error_handler = error_handler
        self.components = []
        
        self.logger.info(f"Initializing tab for {component_name}")
        self.setup_tab()
    
    def setup_tab(self):
        """Setup the component demonstration tab"""
        try:
            # Main container with padding
            self.main_frame = tk.Frame(self.parent, bg='#f8f9fa')
            
            # Header section
            header_frame = tk.Frame(self.main_frame, bg='#ffffff', relief='raised', bd=1)
            header_frame.pack(fill='x', padx=10, pady=(10, 5))
            
            # Component title and description
            title_label = tk.Label(header_frame, 
                                 text=f"🔧 {self.component_name}",
                                 font=('Segoe UI', 16, 'bold'),
                                 bg='#ffffff', fg='#333333')
            title_label.pack(pady=10)
            
            desc_text = self.get_component_description()
            desc_label = tk.Label(header_frame,
                                text=desc_text,
                                font=('Segoe UI', 10),
                                bg='#ffffff', fg='#666666',
                                wraplength=600)
            desc_label.pack(pady=(0, 10))
            
            # Demo section
            demo_frame = tk.Frame(self.main_frame, bg='#ffffff', relief='raised', bd=1)
            demo_frame.pack(fill='both', expand=True, padx=10, pady=5)
            
            demo_title = tk.Label(demo_frame,
                                text="Live Demo",
                                font=('Segoe UI', 12, 'bold'),
                                bg='#ffffff', fg='#333333')
            demo_title.pack(pady=(10, 5))
            
            # Component-specific demo area
            self.demo_area = tk.Frame(demo_frame, bg='#f8f9fa', relief='sunken', bd=1)
            self.demo_area.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Create component demonstrations
            self.create_component_demo()
            
            self.logger.info(f"Tab setup complete for {self.component_name}")
            
        except Exception as e:
            error_id = self.error_handler.handle_error(e, f"Tab setup for {self.component_name}")
            self.logger.error(f"Failed to setup tab: {error_id}")
    
    def get_component_description(self):
        """Get description text for the component"""
        descriptions = {
            'BTkButton': "Modern button component with multiple styles, hover effects, and customizable appearance. Supports primary, secondary, success, warning, and danger variants.",
            'BTkFrame': "Enhanced frame container with modern styling, rounded corners, and flexible content positioning. Perfect for organizing UI elements.",
            'BTkLabel': "Advanced label component with auto-sizing, multiple font weights, and specialized variants like titles and clickable labels.",
            'BTkEntry': "Modern input field with placeholder text, focus indicators, and validation support. Features rounded borders and smooth animations.",
            'BTkCheckBox': "Canvas-based checkbox with smooth animations, custom styling, and hover effects. Supports variable binding and custom commands.",
            'BTkProgressBar': "Animated progress bar with percentage display, gradient effects, and smooth value transitions. Ideal for showing task progress.",
            'BTkNavBar': "Flexible navigation component with multiple position styles (top, left, bottom). Features tab switching and content management.",
            'BTkColorPicker': "Full-featured HSV color picker with interactive color wheel, brightness slider, and real-time preview. Perfect for color selection.",
            'BTkDialog': "Modern dialog system with predefined types (info, warning, error, success) and custom input dialogs. Supports modal and non-modal modes.",
            'BTkSystemTray': "Windows system tray integration with custom icons, context menus, and notification support. Enables background app operation."
        }
        
        return descriptions.get(self.component_name, f"Demonstration of {self.component_name} component functionality.")
    
    def create_component_demo(self):
        """Create component-specific demonstration"""
        try:
            self.logger.info(f"Creating demo for {self.component_name}")
            
            if self.component_name == 'BTkButton':
                self.demo_buttons()
            elif self.component_name == 'BTkFrame':
                self.demo_frames()
            elif self.component_name == 'BTkLabel':
                self.demo_labels()
            elif self.component_name == 'BTkEntry':
                self.demo_entries()
            elif self.component_name == 'BTkCheckBox':
                self.demo_checkboxes()
            elif self.component_name == 'BTkProgressBar':
                self.demo_progress_bars()
            elif self.component_name == 'BTkNavBar':
                self.demo_navbar()
            elif self.component_name == 'BTkColorPicker':
                self.demo_color_picker()
            elif self.component_name == 'BTkDialog':
                self.demo_dialogs()
            elif self.component_name == 'BTkSystemTray':
                self.demo_system_tray()
            elif self.component_name == 'BTkSlider':
                self.demo_sliders()
            else:
                self.demo_generic()
                
            self.logger.info(f"Demo created successfully for {self.component_name}")
            
        except Exception as e:
            error_id = self.error_handler.handle_error(e, f"Demo creation for {self.component_name}")
            self.logger.error(f"Failed to create demo: {error_id}")
    
    def safe_create_component(self, component_class, parent, **kwargs):
        """Safely create a component with error handling"""
        try:
            component = component_class(parent, **kwargs)
            self.components.append(component)
            self.logger.debug(f"Created {component_class.__name__} successfully")
            return component
        except Exception as e:
            error_id = self.error_handler.handle_error(e, f"Creating {component_class.__name__}")
            self.logger.error(f"Failed to create component: {error_id}")
            
            # Create fallback label
            fallback = tk.Label(parent, 
                              text=f"❌ Error creating {component_class.__name__}\nSee logs for details",
                              fg='red', font=('Segoe UI', 10))
            return fallback
    
    def demo_buttons(self):
        """Demonstrate BTkButton component"""
        try:
            # Button styles demonstration
            styles_frame = tk.LabelFrame(self.demo_area, text="Button Styles", 
                                       font=('Segoe UI', 10, 'bold'))
            styles_frame.pack(fill='x', padx=10, pady=5)
            
            button_frame = tk.Frame(styles_frame)
            button_frame.pack(pady=10)
            
            styles = ['default', 'primary', 'success', 'warning', 'danger']
            for i, style in enumerate(styles):
                try:
                    btn = self.safe_create_component(
                        self.component_class, button_frame,
                        text=style.title(),
                        style=style,
                        command=lambda s=style: self.logger.info(f"Button clicked: {s}")
                    )
                    btn.grid(row=0, column=i, padx=5, pady=5)
                except Exception as e:
                    self.error_handler.handle_error(e, f"Creating {style} button")
            
            # Interactive demo
            interactive_frame = tk.LabelFrame(self.demo_area, text="Interactive Features",
                                            font=('Segoe UI', 10, 'bold'))
            interactive_frame.pack(fill='x', padx=10, pady=5)
            
            # Custom styled button
            try:
                custom_btn = self.safe_create_component(
                    self.component_class, interactive_frame,
                    text="Custom Style Button",
                    width=200, height=40,
                    command=lambda: self.show_button_info()
                )
                custom_btn.pack(pady=10)
            except Exception as e:
                self.error_handler.handle_error(e, "Creating custom button")
                
        except Exception as e:
            self.error_handler.handle_error(e, "Button demo setup")
    
    def demo_frames(self):
        """Demonstrate BTkFrame component"""
        try:
            # Different frame styles
            for i, style in enumerate(['default', 'card', 'raised']):
                try:
                    frame = self.safe_create_component(
                        self.component_class, self.demo_area,
                        style=style, width=200, height=100
                    )
                    frame.grid(row=0, column=i, padx=10, pady=10, sticky='nsew')
                    
                    # Add content to frame
                    label = tk.Label(frame, text=f"{style.title()} Frame",
                                   font=('Segoe UI', 10, 'bold'))
                    if hasattr(frame, 'place_content'):
                        frame.place_content(label, relx=0.5, rely=0.5, anchor='center')
                    else:
                        label.pack(expand=True)
                        
                except Exception as e:
                    self.error_handler.handle_error(e, f"Creating {style} frame")
            
            # Configure grid weights
            for i in range(3):
                self.demo_area.grid_columnconfigure(i, weight=1)
                
        except Exception as e:
            self.error_handler.handle_error(e, "Frame demo setup")
    
    def demo_labels(self):
        """Demonstrate BTkLabel component"""
        try:
            label_frame = tk.Frame(self.demo_area)
            label_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Different label styles
            label_configs = [
                {'text': 'Title Label', 'font_size': 16, 'font_weight': 'bold'},
                {'text': 'Subtitle Label', 'font_size': 12, 'font_weight': 'bold'},
                {'text': 'Regular Label', 'font_size': 10},
                {'text': 'Caption Label', 'font_size': 8, 'text_color': '#666666'},
            ]
            
            for config in label_configs:
                try:
                    label = self.safe_create_component(
                        self.component_class, label_frame, **config
                    )
                    label.pack(pady=5, anchor='w')
                except Exception as e:
                    self.error_handler.handle_error(e, f"Creating label with config {config}")
                    
        except Exception as e:
            self.error_handler.handle_error(e, "Label demo setup")
    
    def demo_entries(self):
        """Demonstrate BTkEntry component"""
        try:
            entry_frame = tk.Frame(self.demo_area)
            entry_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Different entry configurations
            entries = [
                {'placeholder_text': 'Enter your name...', 'width': 200},
                {'placeholder_text': 'Email address', 'width': 250},
                {'placeholder_text': 'Password', 'width': 180, 'show': '*'},
            ]
            
            for entry_config in entries:
                try:
                    label = tk.Label(entry_frame, 
                                   text=entry_config['placeholder_text'].replace('...', ':'),
                                   font=('Segoe UI', 9))
                    label.pack(anchor='w', pady=(10, 2))
                    
                    entry = self.safe_create_component(
                        self.component_class, entry_frame, **entry_config
                    )
                    entry.pack(anchor='w', pady=(0, 5))
                    
                except Exception as e:
                    self.error_handler.handle_error(e, f"Creating entry with config {entry_config}")
                    
        except Exception as e:
            self.error_handler.handle_error(e, "Entry demo setup")
    
    def demo_checkboxes(self):
        """Demonstrate BTkCheckBox component"""
        try:
            checkbox_frame = tk.Frame(self.demo_area)
            checkbox_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Different checkbox options
            options = [
                'Enable notifications',
                'Auto-save documents',
                'Show tooltips',
                'Dark mode theme'
            ]
            
            for option in options:
                try:
                    var = tk.BooleanVar()
                    checkbox = self.safe_create_component(
                        self.component_class, checkbox_frame,
                        text=option,
                        variable=var,
                        command=lambda opt=option, v=var: self.logger.info(f"Checkbox '{opt}': {v.get()}")
                    )
                    checkbox.pack(anchor='w', pady=5)
                    
                except Exception as e:
                    self.error_handler.handle_error(e, f"Creating checkbox for {option}")
                    
        except Exception as e:
            self.error_handler.handle_error(e, "Checkbox demo setup")
    
    def demo_progress_bars(self):
        """Demonstrate BTkProgressBar component"""
        try:
            progress_frame = tk.Frame(self.demo_area)
            progress_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Create progress bars with different values
            values = [25, 50, 75, 100]
            progress_bars = []
            
            for value in values:
                try:
                    label = tk.Label(progress_frame, text=f"Progress: {value}%",
                                   font=('Segoe UI', 9))
                    label.pack(anchor='w', pady=(10, 2))
                    
                    progress = self.safe_create_component(
                        self.component_class, progress_frame,
                        value=value, width=300
                    )
                    progress.pack(anchor='w', pady=(0, 5))
                    progress_bars.append(progress)
                    
                except Exception as e:
                    self.error_handler.handle_error(e, f"Creating progress bar with value {value}")
            
            # Animation demo
            def animate_progress():
                try:
                    for progress in progress_bars:
                        if hasattr(progress, 'set_value'):
                            import random
                            new_value = random.randint(10, 100)
                            progress.set_value(new_value)
                            self.logger.debug(f"Animated progress bar to {new_value}%")
                except Exception as e:
                    self.error_handler.handle_error(e, "Progress bar animation")
            
            animate_btn = tk.Button(progress_frame, text="Animate Progress Bars",
                                  command=animate_progress, font=('Segoe UI', 9))
            animate_btn.pack(pady=10)
            
        except Exception as e:
            self.error_handler.handle_error(e, "Progress bar demo setup")
    
    def demo_navbar(self):
        """Demonstrate BTkNavBar component"""
        try:
            nav_frame = tk.Frame(self.demo_area)
            nav_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Position demonstration
            positions = ['top', 'left', 'bottom']
            
            for i, position in enumerate(positions):
                try:
                    label = tk.Label(nav_frame, text=f"Position: {position.title()}",
                                   font=('Segoe UI', 10, 'bold'))
                    label.grid(row=i*2, column=0, sticky='w', pady=(10, 2))
                    
                    nav = self.safe_create_component(
                        self.component_class, nav_frame,
                        position=position,
                        width=300, height=60
                    )
                    nav.grid(row=i*2+1, column=0, sticky='w', pady=(0, 10))
                    
                except Exception as e:
                    self.error_handler.handle_error(e, f"Creating navbar with position {position}")
                    
        except Exception as e:
            self.error_handler.handle_error(e, "NavBar demo setup")
    
    def demo_color_picker(self):
        """Demonstrate BTkColorPicker component"""
        try:
            picker_frame = tk.Frame(self.demo_area)
            picker_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Color picker with callback
            def on_color_selected(color):
                self.logger.info(f"Color selected: {color}")
                result_label.configure(text=f"Selected Color: {color}", bg=color)
            
            try:
                color_picker = self.safe_create_component(
                    self.component_class, picker_frame,
                    command=on_color_selected
                )
                color_picker.pack(pady=10)
                
                # Result display
                result_label = tk.Label(picker_frame, 
                                      text="Select a color above",
                                      font=('Segoe UI', 10),
                                      relief='raised', bd=2)
                result_label.pack(pady=10, padx=20, fill='x')
                
            except Exception as e:
                self.error_handler.handle_error(e, "Creating color picker")
                
        except Exception as e:
            self.error_handler.handle_error(e, "Color picker demo setup")
    
    def demo_dialogs(self):
        """Demonstrate BTkDialog component"""
        try:
            dialog_frame = tk.Frame(self.demo_area)
            dialog_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Dialog types
            dialog_types = [
                ('Info Dialog', 'info'),
                ('Warning Dialog', 'warning'), 
                ('Error Dialog', 'error'),
                ('Success Dialog', 'success')
            ]
            
            def show_dialog(dialog_type):
                try:
                    if hasattr(self.component_class, 'show_info') and dialog_type == 'info':
                        self.component_class.show_info("Information", "This is an info dialog!")
                    elif hasattr(self.component_class, 'show_warning') and dialog_type == 'warning':
                        self.component_class.show_warning("Warning", "This is a warning dialog!")
                    elif hasattr(self.component_class, 'show_error') and dialog_type == 'error':
                        self.component_class.show_error("Error", "This is an error dialog!")
                    elif hasattr(self.component_class, 'show_success') and dialog_type == 'success':
                        self.component_class.show_success("Success", "This is a success dialog!")
                    else:
                        # Fallback to creating instance
                        dialog = self.component_class(dialog_frame, 
                                                    title=f"{dialog_type.title()} Dialog",
                                                    message=f"This is a {dialog_type} dialog!")
                        dialog.show()
                    
                    self.logger.info(f"Showed {dialog_type} dialog")
                except Exception as e:
                    self.error_handler.handle_error(e, f"Showing {dialog_type} dialog")
            
            for dialog_name, dialog_type in dialog_types:
                try:
                    btn = tk.Button(dialog_frame, text=dialog_name,
                                  command=lambda dt=dialog_type: show_dialog(dt),
                                  font=('Segoe UI', 9), width=15)
                    btn.pack(pady=5)
                except Exception as e:
                    self.error_handler.handle_error(e, f"Creating dialog button for {dialog_name}")
                    
        except Exception as e:
            self.error_handler.handle_error(e, "Dialog demo setup")
    
    def demo_system_tray(self):
        """Demonstrate BTkSystemTray component"""
        try:
            tray_frame = tk.Frame(self.demo_area)
            tray_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            info_label = tk.Label(tray_frame,
                                text="System Tray Component (Windows Only)\n\nThis component provides system tray integration with:\n• Custom icons and tooltips\n• Context menus\n• Show/hide application\n• System notifications",
                                font=('Segoe UI', 10),
                                justify='left')
            info_label.pack(pady=20)
            
            def test_system_tray():
                try:
                    # Test if system tray is available
                    import sys
                    if sys.platform != 'win32':
                        messagebox.showinfo("Info", "System tray is optimized for Windows")
                        return
                    
                    self.logger.info("Testing system tray functionality")
                    
                    # Try to show a notification through the system tray
                    if hasattr(self, 'parent') and hasattr(self.parent, 'system_tray'):
                        self.parent.system_tray.show_notification("BTk Demo", "System tray test notification!")
                        messagebox.showinfo("System Tray", "System tray is working!\n\nCheck your system tray for the notification and BTk icon.")
                    else:
                        messagebox.showinfo("System Tray", "System tray component is available but not currently active in this demo.")
                    
                except Exception as e:
                    self.error_handler.handle_error(e, "Testing system tray")
            
            test_btn = tk.Button(tray_frame, text="Test System Tray",
                               command=test_system_tray,
                               font=('Segoe UI', 9))
            test_btn.pack(pady=10)
            
        except Exception as e:
            self.error_handler.handle_error(e, "System tray demo setup")
    
    def demo_sliders(self):
        """Demonstrate BTkSlider component"""
        try:
            slider_frame = tk.Frame(self.demo_area)
            slider_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            info_label = tk.Label(slider_frame,
                                text="BTkSlider - Modern Slider Component\n\nInteractive sliders with customizable appearance",
                                font=('Segoe UI', 10, 'bold'))
            info_label.pack(pady=10)
            
            # Horizontal slider demo
            h_frame = tk.LabelFrame(slider_frame, text="Horizontal Slider", font=('Segoe UI', 9))
            h_frame.pack(fill='x', pady=10, padx=20)
            
            value_var = tk.StringVar(value="50")
            def on_slider_change(value):
                value_var.set(f"{int(value)}")
            
            h_slider = self.safe_create_component(
                self.component_class, h_frame,
                from_=0, to=100,
                width=300, height=20,
                command=on_slider_change
            )
            h_slider.pack(pady=10)
            
            # Set initial value
            if hasattr(h_slider, 'set_value'):
                h_slider.set_value(50)
            elif hasattr(h_slider, 'set'):
                h_slider.set(50)
            
            value_label = tk.Label(h_frame, textvariable=value_var, font=('Segoe UI', 10))
            value_label.pack()
            
            # Vertical slider demo  
            v_frame = tk.LabelFrame(slider_frame, text="Vertical Slider", font=('Segoe UI', 9))
            v_frame.pack(fill='x', pady=10, padx=20)
            
            v_container = tk.Frame(v_frame)
            v_container.pack()
            
            v_value_var = tk.StringVar(value="25")
            def on_v_slider_change(value):
                v_value_var.set(f"{int(value)}")
            
            v_slider = self.safe_create_component(
                self.component_class, v_container,
                from_=0, to=100,
                orientation="vertical",
                width=20, height=200,
                command=on_v_slider_change
            )
            v_slider.pack(side='left', padx=20)
            
            # Set initial value
            if hasattr(v_slider, 'set_value'):
                v_slider.set_value(25)
            elif hasattr(v_slider, 'set'):
                v_slider.set(25)
            
            v_value_label = tk.Label(v_container, textvariable=v_value_var, font=('Segoe UI', 10))
            v_value_label.pack(side='left', padx=10)
            
        except Exception as e:
            self.error_handler.handle_error(e, "Slider demo setup")
    
    def demo_generic(self):
        """Generic demo for unknown components"""
        try:
            generic_frame = tk.Frame(self.demo_area)
            generic_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            info_label = tk.Label(generic_frame,
                                text=f"Demo for {self.component_name}\n\nThis component is available but doesn't have a specific demo yet.",
                                font=('Segoe UI', 10))
            info_label.pack(expand=True)
            
            # Try to create a basic instance
            try:
                component = self.safe_create_component(
                    self.component_class, generic_frame
                )
                component.pack(pady=20)
            except Exception as e:
                self.error_handler.handle_error(e, f"Creating generic {self.component_name}")
                
        except Exception as e:
            self.error_handler.handle_error(e, f"Generic demo setup for {self.component_name}")
    
    def show_button_info(self):
        """Show information about button interaction"""
        try:
            messagebox.showinfo("Button Clicked", 
                              "Custom style button was clicked!\nCheck the logs for detailed information.")
            self.logger.info("Custom button interaction completed successfully")
        except Exception as e:
            self.error_handler.handle_error(e, "Showing button info")

class BTkUltimateDemo:
    """Main application class with extreme error handling and logging"""
    
    def __init__(self):
        self.logger = logging.getLogger('BTkDemo')
        self.error_handler = ErrorHandler()
        self.system_tray = None
        self.tabs = {}
        self.current_tab = None
        
        self.logger.info("Initializing BetterTkinter Demo")
        
        try:
            self.setup_main_window()
            self.setup_navigation()
            self.setup_component_tabs()
            self.setup_log_display()
            self.setup_system_tray()
            self.logger.info("Demo initialization completed successfully")
            
        except Exception as e:
            error_id = self.error_handler.handle_error(e, "Demo initialization", show_dialog=True)
            self.logger.critical(f"Failed to initialize demo: {error_id}")
            sys.exit(1)
    
    def setup_main_window(self):
        """Setup the main application window"""
        try:
            self.logger.info("Setting up main window")
            
            self.root = tk.Tk()
            self.root.title("BetterTkinter Demo - Complete Component Showcase")
            self.root.geometry("1200x800")
            self.root.minsize(800, 600)
            
            # Window icon (if available)
            try:
                icon_path = os.path.join(os.path.dirname(__file__), 'btk_logo.png')
                if os.path.exists(icon_path):
                    # Try to set window icon
                    try:
                        from PIL import Image, ImageTk
                        img = Image.open(icon_path)
                        img = img.resize((32, 32), Image.Resampling.LANCZOS)
                        photo = ImageTk.PhotoImage(img)
                        self.root.iconphoto(False, photo)
                        self.logo_image = photo  # Keep reference
                        self.logger.info(f"Window icon set successfully from {icon_path}")
                    except ImportError:
                        # Fallback for systems without PIL
                        try:
                            self.root.iconbitmap(icon_path)
                            self.logger.info("Window icon set using iconbitmap")
                        except tk.TclError:
                            self.logger.warning("Could not set window icon")
                    except Exception as e:
                        self.logger.warning(f"Could not load icon: {e}")
                else:
                    self.logger.warning(f"Icon file not found: {icon_path}")
            except Exception as e:
                self.logger.warning(f"Error setting window icon: {e}")
            
            # Configure styles
            self.root.configure(bg='#f0f0f0')
            
            # Handle window close
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            
            # Main container with padding
            self.main_container = tk.Frame(self.root, bg='#f0f0f0')
            self.main_container.pack(fill='both', expand=True, padx=5, pady=5)
            
            self.logger.info("Main window setup completed")
            
        except Exception as e:
            self.error_handler.handle_error(e, "Main window setup")
            raise
    
    def setup_navigation(self):
        """Setup the navigation bar"""
        try:
            self.logger.info("Setting up navigation system")
            
            # Top navigation frame
            self.nav_frame = tk.Frame(self.main_container, bg='#ffffff', relief='raised', bd=1)
            self.nav_frame.pack(fill='x', pady=(0, 5))
            
            # Title and logo
            title_frame = tk.Frame(self.nav_frame, bg='#ffffff')
            title_frame.pack(fill='x', padx=10, pady=10)
            
            # Try to load and display logo
            try:
                logo_path = os.path.join(os.path.dirname(__file__), 'btk_logo.png')
                if os.path.exists(logo_path):
                    try:
                        from PIL import Image, ImageTk
                        logo_img = Image.open(logo_path)
                        logo_img = logo_img.resize((32, 32), Image.Resampling.LANCZOS)
                        self.logo_photo = ImageTk.PhotoImage(logo_img)
                        
                        logo_label = tk.Label(title_frame, image=self.logo_photo, bg='#ffffff')
                        logo_label.pack(side='left', padx=(0, 10))
                        self.logger.info("BTk logo loaded and displayed successfully")
                    except ImportError:
                        self.logger.warning("PIL not available - logo not displayed")
                    except Exception as e:
                        self.logger.error(f"Error loading logo: {e}")
                else:
                    self.logger.warning(f"Logo file not found: {logo_path}")
            except Exception as e:
                self.logger.error(f"Error setting up logo: {e}")
            
            # Main title
            title_label = tk.Label(title_frame,
                                 text="🚀 BetterTkinter Demo",
                                 font=('Segoe UI', 18, 'bold'),
                                 bg='#ffffff', fg='#333333')
            title_label.pack(side='left')
            
            # Status info
            status_text = f"Components: {len(COMPONENTS)} | Errors: {len(IMPORT_ERRORS)}"
            status_label = tk.Label(title_frame,
                                  text=status_text,
                                  font=('Segoe UI', 9),
                                  bg='#ffffff', fg='#666666')
            status_label.pack(side='right')
            
            # Navigation tabs frame
            self.tabs_frame = tk.Frame(self.nav_frame, bg='#ffffff')
            self.tabs_frame.pack(fill='x', padx=10, pady=(0, 10))
            
            # Content area
            self.content_frame = tk.Frame(self.main_container, bg='#f8f9fa', relief='sunken', bd=1)
            self.content_frame.pack(fill='both', expand=True)
            
            self.logger.info("Navigation setup completed")
            
        except Exception as e:
            self.error_handler.handle_error(e, "Navigation setup")
            raise
    
    def setup_component_tabs(self):
        """Setup individual component tabs"""
        try:
            self.logger.info("Setting up component tabs")
            
            self.tab_buttons = {}
            self.tab_contents = {}
            
            # Add log tab first
            self.create_log_tab()
            
            # Create tabs for each available component
            col = 1  # Start after log tab
            row = 0
            max_cols = 6
            
            for component_name, component_class in COMPONENTS.items():
                try:
                    # Create tab button
                    tab_btn = tk.Button(self.tabs_frame,
                                      text=component_name.replace('BTk', ''),
                                      font=('Segoe UI', 9),
                                      relief='raised',
                                      bd=1,
                                      padx=10,
                                      pady=5,
                                      command=lambda name=component_name: self.show_tab(name))
                    
                    tab_btn.grid(row=row, column=col, padx=2, pady=2, sticky='ew')
                    self.tab_buttons[component_name] = tab_btn
                    
                    # Create tab content
                    tab_content = ComponentTab(self.content_frame, component_name, component_class, self.error_handler)
                    self.tab_contents[component_name] = tab_content
                    
                    col += 1
                    if col >= max_cols:
                        col = 0
                        row += 1
                    
                    self.logger.debug(f"Created tab for {component_name}")
                    
                except Exception as e:
                    self.error_handler.handle_error(e, f"Creating tab for {component_name}")
            
            # Configure grid weights
            for i in range(max_cols):
                self.tabs_frame.grid_columnconfigure(i, weight=1)
            
            # Show first component tab by default
            if COMPONENTS:
                first_component = list(COMPONENTS.keys())[0]
                self.show_tab(first_component)
            else:
                self.show_tab('logs')
            
            self.logger.info(f"Component tabs setup completed - {len(self.tab_contents)} tabs created")
            
        except Exception as e:
            self.error_handler.handle_error(e, "Component tabs setup")
            raise
    
    def create_log_tab(self):
        """Create the logs tab"""
        try:
            # Log tab button
            log_btn = tk.Button(self.tabs_frame,
                              text="📋 Logs",
                              font=('Segoe UI', 9, 'bold'),
                              relief='raised',
                              bd=1,
                              padx=10,
                              pady=5,
                              fg='#007BFF',
                              command=lambda: self.show_tab('logs'))
            
            log_btn.grid(row=0, column=0, padx=2, pady=2, sticky='ew')
            self.tab_buttons['logs'] = log_btn
            
            # Log content frame
            log_content_frame = tk.Frame(self.content_frame, bg='#f8f9fa')
            
            # Setup log display
            self.log_display = LogDisplay(log_content_frame)
            self.tab_contents['logs'] = type('LogTab', (), {'main_frame': log_content_frame})()
            
            self.logger.info("Log tab created successfully")
            
        except Exception as e:
            self.error_handler.handle_error(e, "Creating log tab")
    
    def setup_log_display(self):
        """Setup the integrated log display"""
        try:
            # Bottom panel for logs (collapsible)
            self.log_panel = tk.Frame(self.main_container, bg='#ffffff', relief='raised', bd=1, height=200)
            self.log_panel.pack(fill='x', pady=(5, 0))
            self.log_panel.pack_propagate(False)
            
            # Log panel header
            log_header = tk.Frame(self.log_panel, bg='#ffffff')
            log_header.pack(fill='x')
            
            log_title = tk.Label(log_header, text="📊 Live System Logs",
                                font=('Segoe UI', 10, 'bold'),
                                bg='#ffffff', fg='#333333')
            log_title.pack(side='left', padx=10, pady=5)
            
            # Collapse/expand button
            self.log_collapsed = False
            self.toggle_btn = tk.Button(log_header, text="▼", font=('Segoe UI', 8),
                                      command=self.toggle_log_panel,
                                      relief='flat', bd=0, bg='#ffffff')
            self.toggle_btn.pack(side='right', padx=10, pady=5)
            
            # Mini log display
            self.mini_log = LogDisplay(self.log_panel)
            
            self.logger.info("Integrated log display setup completed")
            
        except Exception as e:
            self.error_handler.handle_error(e, "Log display setup")
    
    def setup_system_tray(self):
        """Setup system tray integration"""
        try:
            if 'BTkSystemTray' in COMPONENTS and sys.platform == 'win32':
                self.logger.info("Setting up system tray integration")
                
                def on_show():
                    self.root.deiconify()
                    self.root.lift()
                    
                def on_hide():
                    self.root.withdraw()
                    
                def on_quit():
                    self.on_closing()
                
                custom_menu = [
                    {'text': 'Show Demo', 'command': on_show},
                    {'text': 'Hide Demo', 'command': on_hide},
                    'SEPARATOR',
                    {'text': 'View Logs', 'command': lambda: self.show_tab('logs')},
                ]
                
                self.system_tray = COMPONENTS['BTkSystemTray'](
                    app_name="BTk Demo",
                    root_window=self.root,
                    on_show=on_show,
                    on_hide=on_hide,
                    on_quit=on_quit,
                    menu_items=custom_menu
                )
                
                # Start system tray in separate thread
                self.system_tray.run_detached()
                
                self.logger.info("System tray integration completed")
            else:
                self.logger.info("System tray not available or not on Windows")
                
        except Exception as e:
            self.error_handler.handle_error(e, "System tray setup")
    
    def show_tab(self, tab_name):
        """Show a specific tab"""
        try:
            self.logger.info(f"Switching to tab: {tab_name}")
            
            # Hide current tab
            if self.current_tab and self.current_tab in self.tab_contents:
                self.tab_contents[self.current_tab].main_frame.pack_forget()
                # Reset button style
                if self.current_tab in self.tab_buttons:
                    self.tab_buttons[self.current_tab].configure(relief='raised', bg='SystemButtonFace')
            
            # Show new tab
            if tab_name in self.tab_contents:
                self.tab_contents[tab_name].main_frame.pack(fill='both', expand=True)
                self.current_tab = tab_name
                
                # Highlight button
                if tab_name in self.tab_buttons:
                    self.tab_buttons[tab_name].configure(relief='sunken', bg='#e3f2fd')
                
                self.logger.info(f"Successfully switched to tab: {tab_name}")
            else:
                self.logger.error(f"Tab not found: {tab_name}")
                
        except Exception as e:
            self.error_handler.handle_error(e, f"Showing tab {tab_name}")
    
    def toggle_log_panel(self):
        """Toggle the log panel visibility"""
        try:
            if self.log_collapsed:
                self.log_panel.configure(height=200)
                self.toggle_btn.configure(text="▼")
                self.log_collapsed = False
                self.logger.debug("Log panel expanded")
            else:
                self.log_panel.configure(height=30)
                self.toggle_btn.configure(text="▲")
                self.log_collapsed = True
                self.logger.debug("Log panel collapsed")
                
        except Exception as e:
            self.error_handler.handle_error(e, "Toggling log panel")
    
    def on_closing(self):
        """Handle application closing"""
        try:
            self.logger.info("Application closing initiated")
            
            # Stop system tray
            if self.system_tray:
                self.system_tray.stop()
            
            # Save final log summary
            self.logger.info("=" * 80)
            self.logger.info("DEMO SESSION SUMMARY")
            self.logger.info(f"Total Errors: {self.error_handler.error_count}")
            self.logger.info(f"Components Loaded: {len(COMPONENTS)}")
            self.logger.info(f"Import Errors: {len(IMPORT_ERRORS)}")
            self.logger.info("Demo session ended successfully")
            self.logger.info("=" * 80)
            
            # Cleanup
            self.root.quit()
            self.root.destroy()
            
        except Exception as e:
            self.logger.error(f"Error during application closing: {e}")
            sys.exit(1)
    
    def run(self):
        """Run the demo application"""
        try:
            self.logger.info("Starting demo application main loop")
            
            # Show startup notification
            if self.system_tray:
                self.root.after(2000, lambda: self.system_tray.show_notification(
                    "BTk Demo", "Demo started successfully! Check system tray."))
            
            # Start main loop
            self.root.mainloop()
            
        except KeyboardInterrupt:
            self.logger.info("Demo interrupted by user (Ctrl+C)")
            self.on_closing()
        except Exception as e:
            error_id = self.error_handler.handle_error(e, "Main application loop", show_dialog=True)
            self.logger.critical(f"Critical error in main loop: {error_id}")
            sys.exit(1)

def main():
    """Main entry point with comprehensive error handling"""
    try:
        print("🚀 Starting BetterTkinter Demo...")
        print("=" * 60)
        
        # Show import status
        print(f"✅ Successfully imported: {len(COMPONENTS)} components")
        if IMPORT_ERRORS:
            print(f"❌ Import errors: {len(IMPORT_ERRORS)}")
            for error in IMPORT_ERRORS[:3]:  # Show first 3 errors
                print(f"   • {error}")
            if len(IMPORT_ERRORS) > 3:
                print(f"   ... and {len(IMPORT_ERRORS) - 3} more errors")
        
        print("=" * 60)
        
        # Check Python version
        if sys.version_info < (3, 6):
            print("⚠️ Warning: Python 3.6+ recommended")
        
        # Create and run demo
        demo = BTkUltimateDemo()
        demo.run()
        
    except Exception as e:
        print(f"💥 CRITICAL ERROR: {e}")
        print("Full traceback:")
        traceback.print_exc()
        
        # Try to show error dialog
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Critical Error", 
                               f"Failed to start BTk Demo:\n\n{e}\n\nCheck console for details.")
            root.destroy()
        except:
            pass
        
        sys.exit(1)

if __name__ == "__main__":
    main()
