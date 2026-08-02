# imports
import wx
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from nsis_py.ui.main_window import MainWindow

# define the main application class
class NsisPyApp(wx.App):
    def OnInit(self):
        frame = MainWindow()
        frame.Show()
        return True


if __name__ == "__main__":
    app = NsisPyApp()
    app.MainLoop()