import wx
import os
import sys
from pathlib import Path
from nsis_py.ui.main_window import MainWindow

class HealthService:
    def __init__(self):
        self.app = wx.App(False)
        self.main_window = MainWindow(None, title="Health Service")
        self.main_window.Show()
        self.app.MainLoop()