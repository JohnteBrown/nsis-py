import wx


class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(
            parent=None,
            title="nsis-py",
            size=(900, 600)
        )

        panel = wx.Panel(self)

        label = wx.StaticText(
            panel,
            label="nsis-py",
            pos=(20, 20)
        )