import tkinter as tk
from tkinter import messagebox
import math

class BTkDialog:
    """Modern BetterTkinter dialog component"""
    
    DEFAULT_FONT = "Segoe UI"
    
    def __init__(self, parent=None, title="Dialog", message="", **kwargs):
        self.parent = parent
        self.title = title
        self.message = message
        self.result = None
        
        # Configuration
        self.width = kwargs.get('width', 400)
        self.height = kwargs.get('height', 200)
        self.resizable = kwargs.get('resizable', False)
        
        # Colors
        self.bg_color = kwargs.get('bg_color', "#FFFFFF")
        self.title_bg = kwargs.get('title_bg', "#F8F9FA")
        self.border_color = kwargs.get('border_color', "#E0E0E0")
        self.text_color = kwargs.get('text_color', "#333333")
        self.title_color = kwargs.get('title_color', "#1A1A1A")
        
        # Create dialog
        self.dialog = None
        self.buttons = []
    
    def _create_dialog(self):
        """Create the dialog window"""
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title(self.title)
        self.dialog.geometry(f"{self.width}x{self.height}")
        self.dialog.configure(bg=self.bg_color)
        self.dialog.resizable(self.resizable, self.resizable)
        
        # Make dialog modal
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # Center dialog
        self._center_dialog()
        
        # Create UI elements
        self._create_title_bar()
        self._create_message_area()
        self._create_button_area()
        self._create_buttons()  # Create the actual buttons
    
    def _center_dialog(self):
        """Center dialog on parent or screen"""
        if self.parent:
            parent_x = self.parent.winfo_rootx()
            parent_y = self.parent.winfo_rooty()
            parent_width = self.parent.winfo_width()
            parent_height = self.parent.winfo_height()
            
            x = parent_x + (parent_width - self.width) // 2
            y = parent_y + (parent_height - self.height) // 2
        else:
            x = (self.dialog.winfo_screenwidth() - self.width) // 2
            y = (self.dialog.winfo_screenheight() - self.height) // 2
        
        self.dialog.geometry(f"{self.width}x{self.height}+{x}+{y}")
    
    def _create_title_bar(self):
        """Create title bar"""
        title_frame = tk.Frame(self.dialog, bg=self.title_bg, height=40)
        title_frame.pack(fill="x", pady=(0, 1))
        title_frame.pack_propagate(False)
        
        # Title label
        title_label = tk.Label(title_frame,
                              text=self.title,
                              bg=self.title_bg,
                              fg=self.title_color,
                              font=(self.DEFAULT_FONT, 11, "bold"))
        title_label.pack(side="left", padx=15, pady=10)
    
    def _create_message_area(self):
        """Create message area"""
        message_frame = tk.Frame(self.dialog, bg=self.bg_color)
        message_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Message label
        self.message_label = tk.Label(message_frame,
                                     text=self.message,
                                     bg=self.bg_color,
                                     fg=self.text_color,
                                     font=(self.DEFAULT_FONT, 10, "normal"),
                                     justify="left",
                                     wraplength=self.width - 60)
        self.message_label.pack(anchor="nw", pady=(0, 20))
    
    def _create_button_area(self):
        """Create button area"""
        self.button_frame = tk.Frame(self.dialog, bg=self.bg_color, height=50)
        self.button_frame.pack(fill="x", side="bottom", padx=20, pady=(0, 20))
        self.button_frame.pack_propagate(False)
    
    def add_button(self, text, command=None, style="default", **kwargs):
        """Add button to dialog"""
        # Store button configuration for later creation
        button_config = {
            'text': text,
            'command': command,
            'style': style,
            'kwargs': kwargs
        }
        self.buttons.append(button_config)
        return self  # Return self for method chaining
    
    def _create_buttons(self):
        """Create all stored buttons"""
        if not hasattr(self, 'button_frame') or not self.buttons:
            return
            
        # Button colors by style
        styles = {
            "default": {"bg": "#E9ECEF", "fg": "#333333", "active_bg": "#DEE2E6"},
            "primary": {"bg": "#007BFF", "fg": "#FFFFFF", "active_bg": "#0056B3"},
            "success": {"bg": "#28A745", "fg": "#FFFFFF", "active_bg": "#1E7E34"},
            "warning": {"bg": "#FFC107", "fg": "#212529", "active_bg": "#E0A800"},
            "danger": {"bg": "#DC3545", "fg": "#FFFFFF", "active_bg": "#C82333"}
        }
        
        for i, button_config in enumerate(self.buttons):
            text = button_config['text']
            command = button_config['command']
            style = button_config['style']
            kwargs = button_config['kwargs']
            
            style_config = styles.get(style, styles["default"])
            
            def button_command(result=text, cmd=command):
                self.result = result
                if cmd:
                    try:
                        cmd()
                    except Exception:
                        pass  # Ignore command errors
                self.close()
            
            btn = tk.Button(self.button_frame,
                          text=text,
                          command=button_command,
                          bg=style_config["bg"],
                          fg=style_config["fg"],
                          activebackground=style_config["active_bg"],
                          activeforeground=style_config["fg"],
                          font=(self.DEFAULT_FONT, 9, "normal"),
                          relief="flat",
                          bd=0,
                          padx=20,
                          pady=6,
                          cursor="hand2",
                          **kwargs)
            
            btn.pack(side="right", padx=(5, 0))
    
    def close(self):
        """Close dialog"""
        if self.dialog:
            self.dialog.destroy()
    
    def show(self):
        """Show dialog and wait for result"""
        self._create_dialog()
        
        # Wait for dialog to close
        self.dialog.wait_window()
        
        return self.result

    @staticmethod
    def show_info(title="Information", message="", parent=None):
        """Show information dialog"""
        dialog = BTkDialog(parent, title, message,
                          bg_color="#E8F4FD",
                          title_bg="#D1ECFF")
        dialog.add_button("OK", style="primary")
        return dialog.show()
    
    @staticmethod
    def show_warning(title="Warning", message="", parent=None):
        """Show warning dialog"""
        dialog = BTkDialog(parent, title, message,
                          bg_color="#FFF3CD",
                          title_bg="#FFEAA7")
        dialog.add_button("OK", style="warning")
        return dialog.show()
    
    @staticmethod
    def show_error(title="Error", message="", parent=None):
        """Show error dialog"""
        dialog = BTkDialog(parent, title, message,
                          bg_color="#F8D7DA",
                          title_bg="#F5C6CB")
        dialog.add_button("OK", style="danger")
        return dialog.show()
    
    @staticmethod
    def show_success(title="Success", message="", parent=None):
        """Show success dialog"""
        dialog = BTkDialog(parent, title, message,
                          bg_color="#D4F8E8", 
                          title_bg="#C3F7DB")
        dialog.add_button("OK", style="success")
        return dialog.show()
    
    @staticmethod
    def ask_yes_no(title="Question", message="", parent=None):
        """Show yes/no question dialog"""
        dialog = BTkDialog(parent, title, message,
                          bg_color="#FFF8DC",
                          title_bg="#FFE4B5")
        dialog.add_button("Yes", style="success")
        dialog.add_button("No", style="secondary")
        return dialog.show()

# Compatibility aliases
class BTkMessageBox:
    """Message box dialogs for compatibility"""
    
    @staticmethod
    def showinfo(title="Information", message="", parent=None):
        """Show information message box"""
        return BTkDialog.show_info(title, message, parent)
    
    @staticmethod
    def showwarning(title="Warning", message="", parent=None):
        """Show warning message box"""
        return BTkDialog.show_warning(title, message, parent)
    
    @staticmethod
    def showerror(title="Error", message="", parent=None):
        """Show error message box"""
        return BTkDialog.show_error(title, message, parent)
    
    @staticmethod
    def showsuccess(title="Success", message="", parent=None):
        """Show success message box"""
        return BTkDialog.show_success(title, message, parent)
    
    @staticmethod
    def askyesno(title="Question", message="", parent=None):
        """Show yes/no question box"""
        return BTkDialog.ask_yes_no(title, message, parent)
    
    @staticmethod
    def askokcancel(title="Confirm", message="", parent=None):
        """Show OK/Cancel dialog"""
        dialog = BTkDialog(parent, title, message)
        dialog.add_button("Cancel", style="secondary")
        dialog.add_button("OK", style="primary")
        result = dialog.show()
        return result == "OK"
