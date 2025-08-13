import tkinter as tk
from tkinter import scrolledtext, font

class BTkTextEditor(tk.Frame):
    def __init__(self, parent, width=600, height=400, bg_color="#FFFFFF", 
                 fg_color="#333333", font_family="Consolas", font_size=11,
                 line_numbers=True, syntax_highlight=False, **kwargs):
        super().__init__(parent, bg=parent.cget('bg'), **kwargs)
        
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.font_family = font_family
        self.font_size = font_size
        self.line_numbers = line_numbers
        self.syntax_highlight = syntax_highlight
        
        self.create_editor()
        
    def create_editor(self):
        # Main container
        self.editor_frame = tk.Frame(self, bg=self.bg_color, relief="solid", borderwidth=1)
        self.editor_frame.pack(fill="both", expand=True)
        
        # Create font
        self.editor_font = font.Font(family=self.font_family, size=self.font_size)
        
        # Line numbers frame (if enabled)
        if self.line_numbers:
            self.line_frame = tk.Frame(self.editor_frame, bg="#F0F0F0", width=50)
            self.line_frame.pack(side="left", fill="y")
            
            self.line_canvas = tk.Canvas(self.line_frame, bg="#F0F0F0", width=50,
                                       highlightthickness=0)
            self.line_canvas.pack(fill="both", expand=True)
        
        # Text widget with scrollbar
        self.text_widget = scrolledtext.ScrolledText(
            self.editor_frame,
            font=self.editor_font,
            bg=self.bg_color,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            selectbackground="#0078D7",
            selectforeground="white",
            wrap=tk.NONE,
            undo=True,
            maxundo=50
        )
        self.text_widget.pack(fill="both", expand=True, side="right")
        
        # Bind events
        if self.line_numbers:
            self.text_widget.bind("<KeyRelease>", self.update_line_numbers)
            self.text_widget.bind("<Button-1>", self.update_line_numbers)
            self.text_widget.bind("<MouseWheel>", self.on_mousewheel)
            
        if self.syntax_highlight:
            self.text_widget.bind("<KeyRelease>", self.highlight_syntax)
            
        # Configure syntax highlighting tags
        if self.syntax_highlight:
            self.configure_syntax_tags()
            
        # Initial line numbers
        if self.line_numbers:
            self.update_line_numbers()
    
    def configure_syntax_tags(self):
        """Configure tags for basic syntax highlighting"""
        # Keywords (Python example)
        self.text_widget.tag_configure("keyword", foreground="#0000FF", font=(self.font_family, self.font_size, "bold"))
        
        # Strings
        self.text_widget.tag_configure("string", foreground="#008000")
        
        # Comments
        self.text_widget.tag_configure("comment", foreground="#808080", font=(self.font_family, self.font_size, "italic"))
        
        # Numbers
        self.text_widget.tag_configure("number", foreground="#FF8000")
        
        # Functions
        self.text_widget.tag_configure("function", foreground="#800080", font=(self.font_family, self.font_size, "bold"))
    
    def highlight_syntax(self, event=None):
        """Basic syntax highlighting for Python-like code"""
        if not self.syntax_highlight:
            return
            
        content = self.text_widget.get("1.0", tk.END)
        
        # Clear previous tags
        for tag in ["keyword", "string", "comment", "number", "function"]:
            self.text_widget.tag_delete(tag)
            
        # Keywords
        keywords = ["def", "class", "if", "else", "elif", "for", "while", "try", "except", "import", "from", "return", "break", "continue", "pass", "lambda", "with", "as", "yield", "global", "nonlocal", "assert", "del", "and", "or", "not", "in", "is", "True", "False", "None"]
        
        lines = content.split('\n')
        for line_num, line in enumerate(lines, 1):
            # Highlight keywords
            words = line.split()
            col = 0
            for word in words:
                word_start = line.find(word, col)
                if word in keywords:
                    start_pos = f"{line_num}.{word_start}"
                    end_pos = f"{line_num}.{word_start + len(word)}"
                    self.text_widget.tag_add("keyword", start_pos, end_pos)
                col = word_start + len(word)
            
            # Highlight strings
            import re
            for match in re.finditer(r'(["\'])(?:(?=(\\?))\2.)*?\1', line):
                start_pos = f"{line_num}.{match.start()}"
                end_pos = f"{line_num}.{match.end()}"
                self.text_widget.tag_add("string", start_pos, end_pos)
            
            # Highlight comments
            comment_pos = line.find('#')
            if comment_pos != -1:
                start_pos = f"{line_num}.{comment_pos}"
                end_pos = f"{line_num}.{len(line)}"
                self.text_widget.tag_add("comment", start_pos, end_pos)
            
            # Highlight numbers
            for match in re.finditer(r'\b\d+\.?\d*\b', line):
                start_pos = f"{line_num}.{match.start()}"
                end_pos = f"{line_num}.{match.end()}"
                self.text_widget.tag_add("number", start_pos, end_pos)
    
    def update_line_numbers(self, event=None):
        """Update line numbers display"""
        if not self.line_numbers:
            return
            
        self.line_canvas.delete("all")
        
        # Get visible lines
        try:
            first_line = int(self.text_widget.index("@0,0").split('.')[0])
            last_line = int(self.text_widget.index(f"@0,{self.text_widget.winfo_height()}").split('.')[0])
            
            line_height = self.editor_font.metrics("linespace")
            
            for line_num in range(first_line, last_line + 1):
                y_pos = (line_num - first_line) * line_height + line_height // 2
                self.line_canvas.create_text(
                    45, y_pos, 
                    text=str(line_num), 
                    anchor="e", 
                    fill="#666666",
                    font=(self.font_family, self.font_size - 1)
                )
        except Exception:
            pass  # Handle edge cases gracefully
            
        # Schedule next update
        self.after_idle(lambda: None)
    
    def on_mousewheel(self, event):
        """Sync line numbers with text scrolling"""
        self.update_line_numbers()
    
    def get_text(self):
        """Get all text content"""
        return self.text_widget.get("1.0", tk.END + "-1c")
    
    def set_text(self, text):
        """Set text content"""
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", text)
        if self.line_numbers:
            self.update_line_numbers()
        if self.syntax_highlight:
            self.highlight_syntax()
    
    def clear(self):
        """Clear all text"""
        self.text_widget.delete("1.0", tk.END)
        if self.line_numbers:
            self.update_line_numbers()
    
    def set_font_size(self, size):
        """Change font size"""
        self.font_size = size
        self.editor_font.configure(size=size)
        if self.line_numbers:
            self.update_line_numbers()
    
    def toggle_line_numbers(self):
        """Toggle line numbers visibility"""
        self.line_numbers = not self.line_numbers
        if self.line_numbers:
            self.line_frame.pack(side="left", fill="y", before=self.text_widget)
            self.update_line_numbers()
        else:
            self.line_frame.pack_forget()
    
    def toggle_syntax_highlight(self):
        """Toggle syntax highlighting"""
        self.syntax_highlight = not self.syntax_highlight
        if self.syntax_highlight:
            self.highlight_syntax()
        else:
            # Clear all syntax tags
            for tag in ["keyword", "string", "comment", "number", "function"]:
                self.text_widget.tag_delete(tag)
