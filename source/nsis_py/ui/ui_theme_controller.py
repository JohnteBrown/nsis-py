import wx
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

class UIThemeController:
    def __init__(self, parent, title):
        self.parent = parent
        self.title = title
        self.panel = wx.Panel(parent)

        # Set dark theme colors
        dark_bg_color = "#252525"  # Dark background color
        dark_fg_color = "#FFFFFF"  # Light foreground color

        # Apply colors to the frame and panel
        parent.SetBackgroundColour(dark_bg_color)
        self.panel.SetBackgroundColour(dark_bg_color)

        # Create a text control with dark mode
        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.text_ctrl.SetBackgroundColour(dark_bg_color)
        self.text_ctrl.SetForegroundColour(dark_fg_color)