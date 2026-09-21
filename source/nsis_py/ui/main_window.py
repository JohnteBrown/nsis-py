import sys
from pathlib import Path

import wx
import wx.xrc as xrc

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nsis_py.ui.child_frame import ChildWindow
from nsis_py.ui.ui_theme_controller import UIThemeController


def MainWindow() -> wx.Frame:
    """Create and return the main window from the XRC resource."""

    base_dir = Path(__file__).resolve().parent.parent
    xrc_path = base_dir / "resources" / "main_window.xrc"

    if not xrc_path.is_file():
        raise FileNotFoundError(f"XRC file not found: {xrc_path}")

    # Load the XRC resource.
    resource = xrc.XmlResource(str(xrc_path))

    if not resource.IsOk():
        raise RuntimeError(f"Could not load XRC resource: {xrc_path}")

    # LoadFrame(None, ...) creates and returns the wx.Frame.
    frame = resource.LoadFrame(None, "MainWindow")

    if frame is None:
        raise RuntimeError(
            "Could not create frame 'MainWindow'. "
            "Check the object name and class in main_window.xrc."
        )

    # Keep the resource alive for the lifetime of the frame.
    frame.xrc_resource = resource

    # Retrieve controls defined in the XRC file.
    frame.main_panel = xrc.XRCCTRL(frame, "main_panel")
    frame.info_label = xrc.XRCCTRL(frame, "info_label")
    frame.open_settings_btn = xrc.XRCCTRL(frame, "open_settings_btn")

    controls = {
        "main_panel": frame.main_panel,
        "info_label": frame.info_label,
        "open_settings_btn": frame.open_settings_btn,
    }

    missing = [name for name, control in controls.items() if control is None]
    if missing:
        raise RuntimeError(
            "The following controls were not found in main_window.xrc: "
            + ", ".join(missing)
        )

    # Apply the application theme.
    frame.theme_controller = UIThemeController(
        frame,
        "nullsoft graphical installer utility - python edition",
    )

    def on_open_child_window(event: wx.CommandEvent) -> None:
        child = ChildWindow(frame)

        # Keep a reference if ChildWindow does not already parent/manage itself.
        frame.child_window = child
        child.Show()

    frame.open_settings_btn.Bind(wx.EVT_BUTTON, on_open_child_window)

    return frame
