import tkinter as tk
import os

class BTk(tk.Tk):
    """Modern BetterTkinter main window with professional styling"""
    
    # Constants
    DEFAULT_FONT = "Segoe UI"
    LOGO_FILENAME = "btk_logo.png"
    
    def __init__(self, title="BetterTkinter Application", **kwargs):
        super().__init__()
        
        # Configuration
        self.title(title)
        self.configure(bg="#FFFFFF")
        
        # Set default geometry
        width = kwargs.get('width', 800)
        height = kwargs.get('height', 600)
        self.geometry(f"{width}x{height}")
        
        # Center window on screen
        self.center_window()
        
        # Set application icon
        self.set_icon()
        
        # Configure window properties
        self.configure_window(**kwargs)
    
    def center_window(self):
        """Center the window on screen"""
        self.update_idletasks()
        
        # Get window size
        width = self.winfo_width()
        height = self.winfo_height()
        
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate position
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        # Set position
        self.geometry(f"{width}x{height}+{x}+{y}")
    
    def set_icon(self):
        """Set the application icon"""
        try:
            # Look for btk_logo.png in current directory or parent
            icon_paths = [
                self.LOGO_FILENAME,
                os.path.join("..", self.LOGO_FILENAME),
                os.path.join(os.path.dirname(__file__), "..", self.LOGO_FILENAME)
            ]
            
            for icon_path in icon_paths:
                if os.path.exists(icon_path):
                    try:
                        self.iconphoto(True, tk.PhotoImage(file=icon_path))
                        return
                    except tk.TclError:
                        continue
            
            # If no PNG found, create a simple icon
            self.create_simple_icon()
            
        except Exception:
            # Silent fallback - use default icon
            pass
    
    def create_simple_icon(self):
        """Create a simple icon programmatically"""
        try:
            # Create a simple 32x32 icon
            icon_data = '''
            R0lGODlhIAAgAPAAAAAAAAAAACH5BAAAAAAALAAAAAAgACAAAAJQhI+py+0Po5y02ouz3rz7D4biSJbmiabqyrbuC8fyTNf2jef6zvf+DwwKh8Si8YhMKpfMpvMJjUqn1Kr1is1qt9yu9wsOi8fksvmMTqvX7HYLADs=
            '''
            photo = tk.PhotoImage(data=icon_data)
            self.iconphoto(True, photo)
        except Exception:
            pass
    
    def configure_window(self, **kwargs):
        """Configure additional window properties"""
        # Resizable
        if 'resizable' in kwargs:
            resizable = kwargs['resizable']
            if isinstance(resizable, bool):
                self.resizable(resizable, resizable)
            else:
                self.resizable(resizable[0], resizable[1])
        
        # Minimum size
        if 'minsize' in kwargs:
            self.minsize(*kwargs['minsize'])
        else:
            self.minsize(400, 300)
        
        # Maximum size
        if 'maxsize' in kwargs:
            self.maxsize(*kwargs['maxsize'])
        
        # Always on top
        if kwargs.get('topmost', False):
            self.attributes('-topmost', True)
        
        # Transparency (Windows)
        if 'alpha' in kwargs:
            try:
                self.attributes('-alpha', kwargs['alpha'])
            except tk.TclError:
                pass

# Test window
if __name__ == "__main__":
    def test_btk():
        """Test the BTk main window"""
        app = BTk("BetterTkinter Demo", width=600, height=400)
        
        # Add some content to test
        header = tk.Frame(app, bg="#FFFFFF", pady=20)
        header.pack(fill="x")
        
        tk.Label(header, 
                text="BetterTkinter Professional",
                font=(BTk.DEFAULT_FONT, 18, "bold"),
                bg="#FFFFFF", fg="#333333").pack()
        
        tk.Label(header,
                text="Modern UI components for Python applications",
                font=(BTk.DEFAULT_FONT, 11, "normal"),
                bg="#FFFFFF", fg="#666666").pack(pady=(5, 0))
        
        # Content area
        content = tk.Frame(app, bg="#F8F9FA", pady=30)
        content.pack(fill="both", expand=True, padx=20, pady=20)
        
        tk.Label(content,
                text="This window demonstrates the BTk main window class",
                font=(BTk.DEFAULT_FONT, 12, "normal"),
                bg="#F8F9FA", fg="#333333").pack()
        
        tk.Label(content,
                text="Features: Centered positioning, custom icon, professional styling",
                font=(BTk.DEFAULT_FONT, 10, "normal"),
                bg="#F8F9FA", fg="#666666").pack(pady=(10, 0))
        
        app.mainloop()
    
    test_btk()
