import wx
import wx.xrc
from pathlib import Path


def ChildWindow(parent):
    """Factory function to create a child window from XRC"""
    # Load the XRC resource
    xrc_path = Path(__file__).parent / "resources" / "child_frame.xrc"
    res = wx.xrc.XmlResource(str(xrc_path))

    # Create frame from XRC resource
    frame = wx.Frame(parent)
    res.LoadFrame(frame, parent, "ChildWindow")

    # Store reference to XRC resource
    frame.res = res

    # Get widgets from XRC by name
    frame.child_panel = wx.xrc.XRCCTRL(frame, "child_panel")
    frame.child_label = wx.xrc.XRCCTRL(frame, "child_label")

    return frame
