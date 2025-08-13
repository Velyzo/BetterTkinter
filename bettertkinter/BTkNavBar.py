import tkinter as tk
from tkinter import ttk
import math

class BTkNavBar(tk.Frame):
    """Modern BetterTkinter navigation bar component with multiple positions"""
    
    # Constants
    DEFAULT_FONT = "Segoe UI"
    
    # Position styles
    POSITION_TOP = "top"
    POSITION_LEFT = "left" 
    POSITION_BOTTOM = "bottom"
    
    def __init__(self, parent, position=POSITION_TOP, **kwargs):
        # Configuration
        self.position = position
        self.tabs = []
        self.active_tab = 0
        self.tab_change_callback = kwargs.get('on_tab_change', None)
        
        # Dimensions based on position
        if position == self.POSITION_LEFT:
            self.nav_width = kwargs.get('width', 200)
            self.nav_height = kwargs.get('height', 400)
        elif position == self.POSITION_BOTTOM:
            self.nav_width = kwargs.get('width', 600)
            self.nav_height = kwargs.get('height', 60)
        else:  # TOP
            self.nav_width = kwargs.get('width', 600)
            self.nav_height = kwargs.get('height', 50)
        
        # Colors
        self.bg_color = kwargs.get('bg_color', "#F8F9FA")
        self.active_color = kwargs.get('active_color', "#007BFF")
        self.inactive_color = kwargs.get('inactive_color', "#6C757D")
        self.hover_color = kwargs.get('hover_color', "#E9ECEF")
        self.text_color = kwargs.get('text_color', "#333333")
        self.active_text_color = kwargs.get('active_text_color', "#FFFFFF")
        
        # Initialize frame
        super().__init__(parent, 
                        bg=self.bg_color,
                        width=self.nav_width,
                        height=self.nav_height)
        
        # Prevent frame from shrinking
        self.pack_propagate(False)
        self.grid_propagate(False)
        
        # Tab buttons list
        self.tab_buttons = []
        
        # Setup layout based on position
        self._setup_layout()
    
    def _setup_layout(self):
        """Setup layout based on position"""
        if self.position == self.POSITION_LEFT:
            # Vertical layout for left sidebar
            self.tab_frame = tk.Frame(self, bg=self.bg_color)
            self.tab_frame.pack(fill="both", expand=True, padx=10, pady=10)
        elif self.position == self.POSITION_BOTTOM:
            # Horizontal layout for bottom bar
            self.tab_frame = tk.Frame(self, bg=self.bg_color)
            self.tab_frame.pack(fill="x", expand=True, pady=10)
        else:  # TOP
            # Horizontal layout for top bar
            self.tab_frame = tk.Frame(self, bg=self.bg_color)
            self.tab_frame.pack(fill="x", expand=True, pady=8)
    
    def add_tab(self, name, content_frame=None, icon=None):
        """Add a new tab to the navigation bar"""
        tab_data = {
            'name': name,
            'content_frame': content_frame,
            'icon': icon,
            'index': len(self.tabs)
        }
        
        self.tabs.append(tab_data)
        self._create_tab_button(tab_data)
        
        # Hide content frame initially if not active tab
        if content_frame and tab_data['index'] != self.active_tab:
            content_frame.pack_forget()
        
        return tab_data['index']
    
    def _create_tab_button(self, tab_data):
        """Create button for tab"""
        index = tab_data['index']
        is_active = index == self.active_tab
        
        # Button configuration based on position
        if self.position == self.POSITION_LEFT:
            # Vertical button for sidebar
            btn_width = 25
            btn_height = 2
            btn_anchor = "w"
            btn_padx = (10, 10)
            btn_pady = (5, 2)
            btn_side = "top"
        elif self.position == self.POSITION_BOTTOM:
            # Horizontal button for bottom bar
            btn_width = 15
            btn_height = 1
            btn_anchor = "center"
            btn_padx = (10, 10)
            btn_pady = (5, 5)
            btn_side = "left"
        else:  # TOP
            # Horizontal button for top bar
            btn_width = 15
            btn_height = 1
            btn_anchor = "center"
            btn_padx = (15, 15)
            btn_pady = (5, 5)
            btn_side = "left"
        
        # Button colors
        if is_active:
            bg_color = self.active_color
            fg_color = self.active_text_color
        else:
            bg_color = self.bg_color
            fg_color = self.text_color
        
        # Create button text (with icon if provided)
        button_text = tab_data['name']
        if tab_data['icon'] and self.position == self.POSITION_LEFT:
            button_text = f"{tab_data['icon']} {button_text}"
        
        # Create button
        btn = tk.Button(self.tab_frame,
                       text=button_text,
                       command=lambda: self._switch_tab(index),
                       bg=bg_color,
                       fg=fg_color,
                       activebackground=self.hover_color,
                       activeforeground=self.text_color,
                       font=(self.DEFAULT_FONT, 9, "normal"),
                       relief="flat",
                       bd=0,
                       width=btn_width,
                       height=btn_height,
                       anchor=btn_anchor,
                       cursor="hand2")
        
        # Pack button based on position
        btn.pack(side=btn_side, padx=btn_padx, pady=btn_pady, fill="x" if self.position == self.POSITION_LEFT else None)
        
        # Bind hover events
        self._bind_hover_events(btn, index)
        
        # Store button reference
        self.tab_buttons.append(btn)
    
    def _bind_hover_events(self, button, index):
        """Bind hover events to button"""
        def on_enter(event):
            if index != self.active_tab:
                button.config(bg=self.hover_color)
        
        def on_leave(event):
            if index != self.active_tab:
                button.config(bg=self.bg_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def _switch_tab(self, new_tab_index):
        """Switch to a different tab"""
        if new_tab_index == self.active_tab or new_tab_index >= len(self.tabs):
            return
        
        old_tab = self.active_tab
        self.active_tab = new_tab_index
        
        # Update button appearances
        self._update_button_appearance(old_tab, False)
        self._update_button_appearance(new_tab_index, True)
        
        # Handle content frame switching
        self._switch_content_frames(old_tab, new_tab_index)
        
        # Call callback if provided
        if self.tab_change_callback:
            try:
                self.tab_change_callback(new_tab_index, self.tabs[new_tab_index]['name'])
            except Exception as e:
                print(f"Tab change callback error: {e}")
    
    def _update_button_appearance(self, tab_index, is_active):
        """Update button appearance for active/inactive state"""
        if tab_index < len(self.tab_buttons):
            button = self.tab_buttons[tab_index]
            
            if is_active:
                button.config(bg=self.active_color, fg=self.active_text_color)
            else:
                button.config(bg=self.bg_color, fg=self.text_color)
    
    def _switch_content_frames(self, old_tab_index, new_tab_index):
        """Switch content frames"""
        # Hide old content frame
        if old_tab_index < len(self.tabs):
            old_frame = self.tabs[old_tab_index]['content_frame']
            if old_frame:
                old_frame.pack_forget()
        
        # Show new content frame
        if new_tab_index < len(self.tabs):
            new_frame = self.tabs[new_tab_index]['content_frame']
            if new_frame:
                new_frame.pack(fill="both", expand=True)
    
    def get_active_tab(self):
        """Get currently active tab index"""
        return self.active_tab
    
    def set_active_tab(self, tab_index):
        """Set active tab programmatically"""
        self._switch_tab(tab_index)
    
    def remove_tab(self, tab_index):
        """Remove a tab"""
        if 0 <= tab_index < len(self.tabs):
            # Remove tab data
            removed_tab = self.tabs.pop(tab_index)
            
            # Remove and destroy button
            if tab_index < len(self.tab_buttons):
                btn = self.tab_buttons.pop(tab_index)
                btn.destroy()
            
            # Update indices for remaining tabs
            for i in range(len(self.tabs)):
                self.tabs[i]['index'] = i
            
            # Adjust active tab if necessary
            if self.active_tab >= len(self.tabs) and len(self.tabs) > 0:
                self.active_tab = len(self.tabs) - 1
            elif self.active_tab > tab_index:
                self.active_tab -= 1
            
            # Update button appearances
            self._refresh_all_buttons()
    
    def _refresh_all_buttons(self):
        """Refresh all button appearances"""
        for i, btn in enumerate(self.tab_buttons):
            self._update_button_appearance(i, i == self.active_tab)
