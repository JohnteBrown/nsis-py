import wx

class ChildWindow(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title="Child Window")
        self.SetSize((300, 200))