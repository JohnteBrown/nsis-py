import wx
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))


class UIThemeController:
    def __init__(self, parent, title):
        self.parent = parent
        self.title = title

        # Set dark theme colors
        dark_bg_color = "#252525"  # Dark background color
        dark_fg_color = "#FFFFFF"  # Light foreground color

        # Apply colors to the frame and panel
        parent.SetBackgroundColour(dark_bg_color)

        # Apply theme to all child windows
        self._apply_theme_recursive(parent, dark_bg_color, dark_fg_color)

    def _apply_theme_recursive(self, window, bg_color, fg_color):
        """Recursively apply theme colors to window and all its children"""
        window.SetBackgroundColour(bg_color)

        # Apply theme to specific widget types
        if isinstance(window, wx.Panel):
            window.SetBackgroundColour(bg_color)

        if isinstance(window, wx.StaticText):
            window.SetForegroundColour(fg_color)

        if isinstance(window, wx.TextCtrl):
            window.SetBackgroundColour(bg_color)
            window.SetForegroundColour(fg_color)

        # Recursively apply to all child windows
        for child in window.GetChildren():
            self._apply_theme_recursive(child, bg_color, fg_color)

        # exclude text
        if isinstance(window, wx.TextCtrl):
            window.SetBackgroundColour(bg_color)
            window.SetForegroundColour(fg_color)