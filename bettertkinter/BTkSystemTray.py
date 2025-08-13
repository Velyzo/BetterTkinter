import tkinter as tk
import sys
import os
import logging
from tkinter import messagebox

# Windows-specific imports
try:
    import pystray
    from pystray import MenuItem as item
    from PIL import Image, ImageDraw
    PYSTRAY_AVAILABLE = True
except ImportError:
    PYSTRAY_AVAILABLE = False
    logging.warning("pystray not available - system tray functionality disabled")

class BTkSystemTray:
    """Windows system tray icon component for BetterTkinter applications"""
    
    def __init__(self, app_name="BetterTkinter App", **kwargs):
        """
        Initialize system tray icon
        
        Args:
            app_name (str): Name of the application
            icon_path (str, optional): Path to custom icon file
            on_quit (callable, optional): Callback when quit is selected
            on_show (callable, optional): Callback when show is selected
            menu_items (list, optional): Additional menu items
        """
        self.logger = logging.getLogger(f"BTkSystemTray.{app_name}")
        self.logger.info(f"Initializing system tray for {app_name}")
        
        if not PYSTRAY_AVAILABLE:
            self.logger.error("pystray module not available - cannot create system tray")
            raise ImportError("pystray module required for system tray functionality")
        
        if sys.platform != 'win32':
            self.logger.warning(f"System tray optimized for Windows, current platform: {sys.platform}")
        
        self.app_name = app_name
        self.icon_path = kwargs.get('icon_path', None)
        self.on_quit = kwargs.get('on_quit', self._default_quit)
        self.on_show = kwargs.get('on_show', self._default_show)
        self.on_hide = kwargs.get('on_hide', self._default_hide)
        self.root_window = kwargs.get('root_window', None)
        self.custom_menu_items = kwargs.get('menu_items', [])
        
        # State
        self.icon = None
        self.is_visible = True
        self.is_running = False
        
        # Create icon
        try:
            self._create_icon()
            self.logger.info("System tray icon created successfully")
        except Exception as e:
            self.logger.error(f"Failed to create system tray icon: {e}")
            raise
    
    def _create_icon(self):
        """Create the system tray icon"""
        try:
            # Load or create icon image
            if self.icon_path and os.path.exists(self.icon_path):
                self.logger.info(f"Loading custom icon from {self.icon_path}")
                image = Image.open(self.icon_path)
            else:
                self.logger.info("Creating default icon")
                image = self._create_default_icon()
            
            # Resize to standard tray icon size
            image = image.resize((64, 64), Image.Resampling.LANCZOS)
            
            # Create menu
            menu = self._create_menu()
            
            # Create pystray icon
            self.icon = pystray.Icon(
                name=self.app_name,
                icon=image,
                title=self.app_name,
                menu=menu
            )
            
            self.logger.info("System tray icon configured successfully")
            
        except Exception as e:
            self.logger.error(f"Error creating system tray icon: {e}")
            raise
    
    def _create_default_icon(self):
        """Create a default icon if no custom icon provided"""
        self.logger.debug("Creating default BTk system tray icon")
        
        # Create a simple icon with BTk branding
        width, height = 64, 64
        image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Draw background circle
        margin = 4
        draw.ellipse([margin, margin, width-margin, height-margin], 
                    fill='#007BFF', outline='#0056B3', width=2)
        
        # Draw "BTk" text
        try:
            # Try to use a better font if available
            from PIL import ImageFont
            try:
                font = ImageFont.truetype("arial.ttf", 16)
            except (OSError, IOError):
                font = ImageFont.load_default()
        except ImportError:
            font = None
        
        text = "BTk"
        if font:
            # Calculate text position for centering
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (width - text_width) // 2
            y = (height - text_height) // 2
            draw.text((x, y), text, fill='white', font=font)
        else:
            # Fallback without font
            draw.text((20, 25), text, fill='white')
        
        self.logger.debug("Default icon created successfully")
        return image
    
    def _create_menu(self):
        """Create the context menu for the system tray"""
        self.logger.debug("Creating system tray menu")
        
        menu_items = []
        
        # Show/Hide option
        if self.root_window:
            menu_items.extend([
                item('Show', self._show_window, default=True),
                item('Hide', self._hide_window),
                pystray.Menu.SEPARATOR,
            ])
        
        # Custom menu items
        for menu_item in self.custom_menu_items:
            if isinstance(menu_item, dict):
                menu_items.append(
                    item(menu_item.get('text', 'Item'), 
                        menu_item.get('command', lambda: None),
                        enabled=menu_item.get('enabled', True))
                )
            elif menu_item == 'SEPARATOR':
                menu_items.append(pystray.Menu.SEPARATOR)
        
        # Standard items
        if self.custom_menu_items:
            menu_items.append(pystray.Menu.SEPARATOR)
        
        menu_items.extend([
            item('About', self._show_about),
            item('Quit', self._quit_application)
        ])
        
        self.logger.debug(f"Created menu with {len(menu_items)} items")
        return pystray.Menu(*menu_items)
    
    def _show_window(self, icon=None, item=None):
        """Show the main window"""
        try:
            if self.root_window:
                self.logger.info("Showing main window from system tray")
                self.root_window.deiconify()
                self.root_window.lift()
                self.root_window.focus_force()
                self.is_visible = True
            
            if self.on_show:
                self.on_show()
                
        except Exception as e:
            self.logger.error(f"Error showing window: {e}")
    
    def _hide_window(self, icon=None, item=None):
        """Hide the main window"""
        try:
            if self.root_window:
                self.logger.info("Hiding main window to system tray")
                self.root_window.withdraw()
                self.is_visible = False
            
            if self.on_hide:
                self.on_hide()
                
        except Exception as e:
            self.logger.error(f"Error hiding window: {e}")
    
    def _show_about(self, icon=None, item=None):
        """Show about dialog"""
        try:
            self.logger.info("Showing about dialog")
            messagebox.showinfo("About", 
                f"{self.app_name}\nBetterTkinter System Tray Component\nWindows System Tray Integration")
        except Exception as e:
            self.logger.error(f"Error showing about dialog: {e}")
    
    def _quit_application(self, icon=None, item=None):
        """Quit the application"""
        try:
            self.logger.info("Quitting application from system tray")
            self.stop()
            if self.on_quit:
                self.on_quit()
        except Exception as e:
            self.logger.error(f"Error quitting application: {e}")
    
    def _default_show(self):
        """Default show callback"""
        self.logger.debug("Default show callback triggered")
    
    def _default_hide(self):
        """Default hide callback"""
        self.logger.debug("Default hide callback triggered")
    
    def _default_quit(self):
        """Default quit callback"""
        self.logger.info("Default quit callback - exiting application")
        if self.root_window:
            self.root_window.quit()
        sys.exit(0)
    
    def run(self):
        """Start the system tray icon (blocking)"""
        if not self.icon:
            self.logger.error("Cannot run - icon not created")
            raise RuntimeError("System tray icon not properly initialized")
        
        try:
            self.logger.info("Starting system tray icon")
            self.is_running = True
            self.icon.run()
        except Exception as e:
            self.logger.error(f"Error running system tray: {e}")
            raise
    
    def run_detached(self):
        """Start the system tray icon in a separate thread (non-blocking)"""
        if not self.icon:
            self.logger.error("Cannot run detached - icon not created")
            raise RuntimeError("System tray icon not properly initialized")
        
        try:
            import threading
            self.logger.info("Starting system tray icon in separate thread")
            self.is_running = True
            
            def run_icon():
                try:
                    self.icon.run_detached()
                except Exception as e:
                    self.logger.error(f"Error in detached system tray thread: {e}")
            
            thread = threading.Thread(target=run_icon, daemon=True)
            thread.start()
            self.logger.info("System tray thread started successfully")
            
        except Exception as e:
            self.logger.error(f"Error starting detached system tray: {e}")
            raise
    
    def stop(self):
        """Stop the system tray icon"""
        if self.icon and self.is_running:
            try:
                self.logger.info("Stopping system tray icon")
                self.icon.stop()
                self.is_running = False
                self.logger.info("System tray icon stopped successfully")
            except Exception as e:
                self.logger.error(f"Error stopping system tray: {e}")
    
    def update_tooltip(self, tooltip):
        """Update the tooltip text"""
        if self.icon:
            try:
                self.icon.title = tooltip
                self.logger.debug(f"Updated tooltip to: {tooltip}")
            except Exception as e:
                self.logger.error(f"Error updating tooltip: {e}")
    
    def update_menu(self, menu_items):
        """Update the context menu"""
        try:
            self.custom_menu_items = menu_items
            menu = self._create_menu()
            if self.icon:
                self.icon.menu = menu
                self.logger.info("System tray menu updated successfully")
        except Exception as e:
            self.logger.error(f"Error updating menu: {e}")
    
    def show_notification(self, title, message):
        """Show a system notification (Windows only)"""
        try:
            if self.icon and sys.platform == 'win32':
                self.icon.notify(message, title)
                self.logger.info(f"Notification sent: {title} - {message}")
            else:
                self.logger.warning("Notifications not supported on this platform")
        except Exception as e:
            self.logger.error(f"Error showing notification: {e}")
    
    @property
    def visible(self):
        """Check if the system tray icon is visible"""
        return self.icon and self.is_running
    
    def __del__(self):
        """Cleanup when object is destroyed"""
        try:
            self.stop()
        except Exception:
            pass

# Example usage and testing
if __name__ == "__main__":
    import logging
    
    # Setup logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create a simple test window
    root = tk.Tk()
    root.title("BTkSystemTray Test")
    root.geometry("400x300")
    
    label = tk.Label(root, text="System Tray Test\nCheck your system tray!", 
                    font=("Segoe UI", 12))
    label.pack(expand=True)
    
    def on_quit():
        print("Custom quit callback triggered")
        root.quit()
    
    def on_show():
        print("Custom show callback triggered")
    
    def on_hide():
        print("Custom hide callback triggered")
    
    # Custom menu items
    custom_menu = [
        {'text': 'Custom Action', 'command': lambda: print("Custom action executed!")},
        'SEPARATOR',
        {'text': 'Settings', 'command': lambda: print("Settings opened!")},
    ]
    
    try:
        # Create system tray
        tray = BTkSystemTray(
            app_name="BTk System Tray Test",
            root_window=root,
            on_quit=on_quit,
            on_show=on_show,
            on_hide=on_hide,
            menu_items=custom_menu
        )
        
        # Start system tray in separate thread
        tray.run_detached()
        
        # Show notification
        root.after(1000, lambda: tray.show_notification("BTk System Tray", "System tray is now active!"))
        
        # Handle window close button to minimize instead of quit
        def on_closing():
            tray._hide_window()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Start tkinter main loop
        root.mainloop()
        
        # Cleanup
        tray.stop()
        
    except ImportError as e:
        print(f"System tray not available: {e}")
        print("To enable system tray functionality, install: pip install pystray pillow")
        root.mainloop()
    except Exception as e:
        print(f"Error: {e}")
        root.mainloop()
