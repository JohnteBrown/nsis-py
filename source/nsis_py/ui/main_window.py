# imports
import wx
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from nsis_py.ui.ui_theme_controller import UIThemeController
from nsis_py.ui.child_frame import ChildWindow

# define the main window class
class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title="nullsoft graphical installer utility - python edition",
            size=(900, 600)
        )

        panel = wx.Panel(self)
        self.theme_controller = UIThemeController(self, "nullsoft graphical installer utility - python edition")

        label = wx.StaticText(
            panel,
            label="how many shrimps do I have to eat before I make my skin turn pink, eat too much and you'll get sick, shrimps are pretty rich!",
            pos=(20, 20),
            style=wx.ST_ELLIPSIZE_END
        )
        label.SetForegroundColour("#FFFFFF")

        button = wx.Button(panel, label="Open Settings", pos=(20, 60))
        button.Bind(wx.EVT_BUTTON, self.on_open_child_window)

    def on_open_child_window(self, event):
        child = ChildWindow(self)
        child.Show()