# 💬 BTkDialog - Modern Dialogs

The `BTkDialog` component provides modern, customizable dialog windows for user interactions, including message boxes, confirmation dialogs, and custom forms.

## 📋 Overview

`BTkDialog` offers:
- Modern, themed dialog windows
- Built-in message box types (info, warning, error, success)
- Customizable buttons and layouts
- Modal and non-modal dialogs
- Smooth animations and transitions
- Static methods for quick dialogs

## 🚀 Basic Usage

```python
from bettertkinter import BTk, BTkDialog, BTkButton

app = BTk()

# Static method dialogs (recommended for simple cases)
def show_info():
    BTkDialog.show_info("Information", "This is an info message!")

def show_warning():
    BTkDialog.show_warning("Warning", "This is a warning!")

# Quick dialogs
BTkButton(app, text="Show Info", command=show_info).pack(pady=5)
BTkButton(app, text="Show Warning", command=show_warning).pack(pady=5)

app.mainloop()
```

## 🔧 Constructor

```python
BTkDialog(parent=None, title="Dialog", message="", 
          bg_color=None, title_bg=None, width=400, height=200,
          modal=True, **kwargs)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent` | Widget | None | Parent window (None for root) |
| `title` | str | "Dialog" | Dialog title |
| `message` | str | "" | Dialog message text |
| `bg_color` | str | None | Background color |
| `title_bg` | str | None | Title bar background color |
| `width` | int | 400 | Dialog width |
| `height` | int | 200 | Dialog height |
| `modal` | bool | True | Whether dialog is modal |
| `**kwargs` | dict | {} | Additional parameters |

## 🎨 Static Methods (Quick Dialogs)

### Information Dialogs

#### `BTkDialog.show_info(title, message, parent=None)`
Shows an information dialog.

```python
BTkDialog.show_info("Success", "Operation completed successfully!")
```

#### `BTkDialog.show_success(title, message, parent=None)`
Shows a success dialog with green theming.

```python
BTkDialog.show_success("Saved", "File saved successfully!")
```

### Warning and Error Dialogs

#### `BTkDialog.show_warning(title, message, parent=None)`
Shows a warning dialog with orange theming.

```python
BTkDialog.show_warning("Warning", "This action cannot be undone!")
```

#### `BTkDialog.show_error(title, message, parent=None)`
Shows an error dialog with red theming.

```python
BTkDialog.show_error("Error", "Failed to save file!")
```

### Question Dialogs

#### `BTkDialog.ask_yes_no(title, message, parent=None)`
Shows a yes/no question dialog.

```python
result = BTkDialog.ask_yes_no("Confirm", "Do you want to save changes?")
if result == "Yes":
    print("User chose Yes")
```

**Returns:**
- `str`: "Yes" or "No" based on user choice

## 🔧 Instance Methods

### Dialog Management

#### `show()`
Displays the dialog and returns the result.

```python
dialog = BTkDialog(app, title="Custom", message="Choose an option")
dialog.add_button("Option 1", style="primary")
dialog.add_button("Option 2", style="secondary")
result = dialog.show()
```

**Returns:**
- `str`: Text of the clicked button, or None if closed

#### `close(result=None)`
Closes the dialog with an optional result.

```python
dialog.close("Custom Result")
```

#### `center_on_parent()`
Centers the dialog on its parent window.

```python
dialog.center_on_parent()
```

### Button Management

#### `add_button(text, style="default", command=None)`
Adds a button to the dialog.

```python
dialog.add_button("OK", style="primary")
dialog.add_button("Cancel", style="secondary")
dialog.add_button("Custom", style="warning", command=custom_action)
```

**Parameters:**
- `text` (str): Button text
- `style` (str): Button style
- `command` (callable): Custom command (optional)

#### `clear_buttons()`
Removes all buttons from the dialog.

```python
dialog.clear_buttons()
```

### Content Management

#### `set_message(message)`
Updates the dialog message.

```python
dialog.set_message("Updated message text")
```

#### `add_widget(widget)`
Adds a custom widget to the dialog.

```python
from bettertkinter import BTkEntry
entry = BTkEntry(dialog)
dialog.add_widget(entry)
```

## 📱 Examples

### Basic Dialog Types

```python
from bettertkinter import BTk, BTkButton, BTkDialog, BTkFrame

class DialogDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Dialog Demo")
        self.geometry("400x500")
        
        self.create_dialog_buttons()
    
    def create_dialog_buttons(self):
        container = BTkFrame(self)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        from bettertkinter import BTkLabel
        BTkLabel(container, text="Dialog Examples", 
                font_size=16).pack(pady=20)
        
        # Info dialog
        BTkButton(container, text="Show Info", 
                 command=self.show_info, style="primary").pack(pady=5, fill="x")
        
        # Success dialog
        BTkButton(container, text="Show Success", 
                 command=self.show_success, style="success").pack(pady=5, fill="x")
        
        # Warning dialog
        BTkButton(container, text="Show Warning", 
                 command=self.show_warning, style="warning").pack(pady=5, fill="x")
        
        # Error dialog
        BTkButton(container, text="Show Error", 
                 command=self.show_error, style="danger").pack(pady=5, fill="x")
        
        # Question dialog
        BTkButton(container, text="Ask Question", 
                 command=self.ask_question, style="secondary").pack(pady=5, fill="x")
        
        # Custom dialog
        BTkButton(container, text="Custom Dialog", 
                 command=self.show_custom, style="secondary").pack(pady=5, fill="x")
    
    def show_info(self):
        BTkDialog.show_info("Information", 
                           "This is an informational message.\n\nIt can contain multiple lines.")
    
    def show_success(self):
        BTkDialog.show_success("Success", "Operation completed successfully! ✅")
    
    def show_warning(self):
        BTkDialog.show_warning("Warning", 
                              "This action may have consequences.\n\nProceed with caution.")
    
    def show_error(self):
        BTkDialog.show_error("Error", "An error occurred while processing your request.")
    
    def ask_question(self):
        result = BTkDialog.ask_yes_no("Confirm Action", 
                                     "Do you want to proceed with this operation?")
        if result == "Yes":
            BTkDialog.show_info("Result", "You chose to proceed!")
        else:
            BTkDialog.show_info("Result", "Operation cancelled.")
    
    def show_custom(self):
        dialog = BTkDialog(self, title="Custom Dialog", 
                          message="Choose your favorite option:")
        
        dialog.add_button("Option A", style="primary")
        dialog.add_button("Option B", style="success")
        dialog.add_button("Option C", style="warning")
        dialog.add_button("Cancel", style="secondary")
        
        result = dialog.show()
        if result:
            BTkDialog.show_info("Selection", f"You chose: {result}")

app = DialogDemo()
app.mainloop()
```

### Custom Input Dialog

```python
from bettertkinter import BTk, BTkDialog, BTkButton, BTkEntry, BTkLabel

class InputDialog(BTkDialog):
    """Custom dialog for text input"""
    
    def __init__(self, parent, title="Input", prompt="Enter value:", default=""):
        super().__init__(parent, title=title, message="", height=250)
        
        self.result_value = None
        self.create_input_ui(prompt, default)
    
    def create_input_ui(self, prompt, default):
        # Remove default message area and create custom layout
        
        # Prompt label
        prompt_label = BTkLabel(self, text=prompt, font_size=12)
        prompt_label.pack(pady=(20, 10))
        
        # Input entry
        self.entry = BTkEntry(self, width=300)
        self.entry.pack(pady=10, padx=20, fill="x")
        self.entry.insert(0, default)
        self.entry.focus_set()
        
        # Button frame
        self.clear_buttons()  # Remove default buttons
        self.add_button("OK", style="primary")
        self.add_button("Cancel", style="secondary")
        
        # Bind Enter key to OK
        self.entry.bind("<Return>", lambda e: self.button_clicked("OK"))
        self.bind("<Escape>", lambda e: self.button_clicked("Cancel"))
    
    def button_clicked(self, button_text):
        if button_text == "OK":
            self.result_value = self.entry.get()
        else:
            self.result_value = None
        self.close(button_text)
    
    def get_input(self):
        """Show dialog and return input value"""
        result = self.show()
        return self.result_value if result == "OK" else None

# Usage example
class InputDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Input Dialog Demo")
        self.geometry("300x200")
        
        BTkButton(self, text="Get User Name", 
                 command=self.get_name).pack(pady=20)
        BTkButton(self, text="Get Email", 
                 command=self.get_email).pack(pady=10)
        
        self.result_label = BTkLabel(self, text="", font_size=12)
        self.result_label.pack(pady=20)
    
    def get_name(self):
        dialog = InputDialog(self, "Name Input", "Enter your name:", "John Doe")
        name = dialog.get_input()
        
        if name:
            self.result_label.configure(text=f"Hello, {name}!")
        else:
            self.result_label.configure(text="Input cancelled")
    
    def get_email(self):
        dialog = InputDialog(self, "Email Input", "Enter your email:", "user@example.com")
        email = dialog.get_input()
        
        if email:
            self.result_label.configure(text=f"Email: {email}")
        else:
            self.result_label.configure(text="Input cancelled")

app = InputDemo()
app.mainloop()
```

### Progress Dialog

```python
from bettertkinter import BTk, BTkDialog, BTkButton, BTkProgressBar, BTkLabel
import threading
import time

class ProgressDialog(BTkDialog):
    """Dialog showing progress of an operation"""
    
    def __init__(self, parent, title="Progress", operation_name="Processing"):
        super().__init__(parent, title=title, message="", height=200, modal=True)
        
        self.cancelled = False
        self.create_progress_ui(operation_name)
    
    def create_progress_ui(self, operation_name):
        # Status label
        self.status_label = BTkLabel(self, text=f"{operation_name}...", font_size=12)
        self.status_label.pack(pady=20)
        
        # Progress bar
        self.progress_bar = BTkProgressBar(self, width=300)
        self.progress_bar.pack(pady=10, padx=20, fill="x")
        
        # Cancel button
        self.clear_buttons()
        self.add_button("Cancel", style="secondary")
    
    def update_progress(self, value, status_text=None):
        """Update progress bar and status"""
        self.progress_bar.set_value(value)
        if status_text:
            self.status_label.configure(text=status_text)
    
    def button_clicked(self, button_text):
        if button_text == "Cancel":
            self.cancelled = True
        self.close(button_text)

# Usage example
class ProgressDemo(BTk):
    def __init__(self):
        super().__init__()
        self.title("Progress Dialog Demo")
        self.geometry("300x150")
        
        BTkButton(self, text="Start Long Operation", 
                 command=self.start_operation).pack(pady=50)
    
    def start_operation(self):
        # Show progress dialog
        progress_dialog = ProgressDialog(self, "Processing", "Downloading files")
        
        # Start background operation
        def background_task():
            for i in range(101):
                if progress_dialog.cancelled:
                    break
                
                # Update progress in main thread
                self.after(0, lambda p=i: progress_dialog.update_progress(
                    p, f"Processing item {p}/100"))
                
                time.sleep(0.05)  # Simulate work
            
            # Close dialog when done
            if not progress_dialog.cancelled:
                self.after(0, lambda: progress_dialog.close("Complete"))
        
        # Start thread and show dialog
        thread = threading.Thread(target=background_task, daemon=True)
        thread.start()
        
        result = progress_dialog.show()
        
        if result == "Complete":
            BTkDialog.show_success("Complete", "Operation completed successfully!")
        elif progress_dialog.cancelled:
            BTkDialog.show_info("Cancelled", "Operation was cancelled by user.")

app = ProgressDemo()
app.mainloop()
```

### Settings Dialog

```python
from bettertkinter import (
    BTk, BTkDialog, BTkButton, BTkCheckBox, 
    BTkLabel, BTkEntry, BTkFrame
)

class SettingsDialog(BTkDialog):
    """Comprehensive settings dialog"""
    
    def __init__(self, parent, current_settings=None):
        super().__init__(parent, title="Settings", message="", 
                        width=500, height=400)
        
        self.settings = current_settings or {
            'username': 'User',
            'email': 'user@example.com',
            'notifications': True,
            'dark_mode': False,
            'auto_save': True
        }
        
        self.create_settings_ui()
    
    def create_settings_ui(self):
        # Create scrollable content area
        content_frame = BTkFrame(self)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # User Information Section
        user_frame = BTkFrame(content_frame)
        user_frame.pack(fill="x", pady=(0, 15))
        
        BTkLabel(user_frame, text="User Information", 
                font_size=14, text_color="#2E8B57").pack(anchor="w", pady=(5, 10))
        
        # Username
        BTkLabel(user_frame, text="Username:").pack(anchor="w")
        self.username_entry = BTkEntry(user_frame)
        self.username_entry.pack(fill="x", pady=(2, 10))
        self.username_entry.insert(0, self.settings['username'])
        
        # Email
        BTkLabel(user_frame, text="Email:").pack(anchor="w")
        self.email_entry = BTkEntry(user_frame)
        self.email_entry.pack(fill="x", pady=(2, 10))
        self.email_entry.insert(0, self.settings['email'])
        
        # Preferences Section
        prefs_frame = BTkFrame(content_frame)
        prefs_frame.pack(fill="x", pady=15)
        
        BTkLabel(prefs_frame, text="Preferences", 
                font_size=14, text_color="#2E8B57").pack(anchor="w", pady=(5, 10))
        
        # Checkboxes
        self.notifications_check = BTkCheckBox(prefs_frame, text="Enable notifications")
        self.notifications_check.pack(anchor="w", pady=2)
        if self.settings['notifications']:
            self.notifications_check.select()
        
        self.dark_mode_check = BTkCheckBox(prefs_frame, text="Dark mode")
        self.dark_mode_check.pack(anchor="w", pady=2)
        if self.settings['dark_mode']:
            self.dark_mode_check.select()
        
        self.auto_save_check = BTkCheckBox(prefs_frame, text="Auto-save documents")
        self.auto_save_check.pack(anchor="w", pady=2)
        if self.settings['auto_save']:
            self.auto_save_check.select()
        
        # Buttons
        self.clear_buttons()
        self.add_button("Save", style="primary")
        self.add_button("Cancel", style="secondary")
        self.add_button("Reset to Defaults", style="warning")
    
    def button_clicked(self, button_text):
        if button_text == "Save":
            self.save_settings()
        elif button_text == "Reset to Defaults":
            self.reset_to_defaults()
            return  # Don't close dialog
        
        self.close(button_text)
    
    def save_settings(self):
        """Collect and save current settings"""
        self.settings.update({
            'username': self.username_entry.get(),
            'email': self.email_entry.get(),
            'notifications': self.notifications_check.get(),
            'dark_mode': self.dark_mode_check.get(),
            'auto_save': self.auto_save_check.get()
        })
    
    def reset_to_defaults(self):
        """Reset all settings to default values"""
        defaults = {
            'username': 'User',
            'email': 'user@example.com',
            'notifications': True,
            'dark_mode': False,
            'auto_save': True
        }
        
        # Update UI
        self.username_entry.delete(0, "end")
        self.username_entry.insert(0, defaults['username'])
        self.email_entry.delete(0, "end")
        self.email_entry.insert(0, defaults['email'])
        
        if defaults['notifications']:
            self.notifications_check.select()
        else:
            self.notifications_check.deselect()
        
        if defaults['dark_mode']:
            self.dark_mode_check.select()
        else:
            self.dark_mode_check.deselect()
        
        if defaults['auto_save']:
            self.auto_save_check.select()
        else:
            self.auto_save_check.deselect()

# Usage
class SettingsApp(BTk):
    def __init__(self):
        super().__init__()
        self.title("Settings Demo")
        self.geometry("300x200")
        
        self.settings = {
            'username': 'John Doe',
            'email': 'john@example.com',
            'notifications': True,
            'dark_mode': False,
            'auto_save': True
        }
        
        BTkButton(self, text="Open Settings", 
                 command=self.open_settings).pack(pady=50)
        
        self.status_label = BTkLabel(self, text="", font_size=10)
        self.status_label.pack(pady=20)
        
        self.update_status()
    
    def open_settings(self):
        dialog = SettingsDialog(self, self.settings.copy())
        result = dialog.show()
        
        if result == "Save":
            self.settings = dialog.settings
            self.update_status()
            BTkDialog.show_success("Settings", "Settings saved successfully!")
    
    def update_status(self):
        status = f"User: {self.settings['username']} | Theme: {'Dark' if self.settings['dark_mode'] else 'Light'}"
        self.status_label.configure(text=status)

app = SettingsApp()
app.mainloop()
```

## 🔧 Advanced Features

### Custom Dialog Themes

```python
# Create themed dialogs
info_dialog = BTkDialog(
    app, 
    title="Information",
    message="Custom themed dialog",
    bg_color="#E8F4FD",
    title_bg="#D1ECFF"
)

warning_dialog = BTkDialog(
    app,
    title="Warning", 
    message="Warning themed dialog",
    bg_color="#FFF3CD",
    title_bg="#FFEAA7"
)
```

### Non-Modal Dialogs

```python
# Create non-modal dialog (doesn't block parent)
non_modal = BTkDialog(app, title="Non-Modal", modal=False)
non_modal.show()  # Doesn't block, returns immediately
```

## 🐛 Common Issues

### Issue: Dialog not appearing
```python
# Ensure parent exists and is visible
if app.winfo_exists():
    dialog = BTkDialog(app, title="Test")
    dialog.show()
```

### Issue: Dialog behind other windows
```python
# Force dialog to front
dialog = BTkDialog(app, title="Test")
dialog.lift()
dialog.focus_force()
```

### Issue: Button text not updating
```python
# Recreate buttons instead of trying to modify
dialog.clear_buttons()
dialog.add_button("New Text", style="primary")
```

## 🎯 Best Practices

1. **Use static methods for simple dialogs**: `show_info()`, `show_error()`, etc.
2. **Make dialogs modal for important actions**: Prevents user confusion
3. **Provide clear button labels**: "Save Changes" vs "OK"
4. **Handle cancellation gracefully**: Always check dialog results
5. **Keep messages concise**: Long text is hard to read in dialogs
6. **Use appropriate colors**: Match dialog type (error = red, success = green)

## 🔗 Related Components

- [BTkButton](BTkButton.md) - Dialog buttons
- [BTkEntry](BTkEntry.md) - Input dialogs
- [BTkCheckBox](BTkCheckBox.md) - Settings dialogs

---

**Ready to create beautiful dialogs with BTkDialog!** 🎉
