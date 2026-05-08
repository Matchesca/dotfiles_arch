from ignis import widgets
from modules.clock import date_box
from modules.power import power_module
# from modules.network import network_module
# from modules.audio import Audio_Module
from modules.dynamic_island.Island import DynamicIsland
from modules.osd.Osd import OSDManager
from modules.dynamic_island.Workspace import Workspace
from modules.dynamic_island.Tools import Tools
from modules.dynamic_island.SystemTray import Tray
from modules.launcher.Launcher import Launcher
from modules.widgets import *
from ignis.app import IgnisApp
from ignis.icon_manager import IconManager
import os

app = IgnisApp.get_default()
app.apply_css(os.path.expanduser("~/.config/ignis/styles/style.scss"))

icon_manager = IconManager.get_default()
icon_manager.add_icons(os.path.expanduser("~/.config/ignis/icons"))


class Bar(widgets.Window):
    def __init__(self, monitor: int):
        super().__init__(
            namespace=f"primary-window-{monitor}",
            css_classes=["bar_container"],
            monitor=monitor,
            anchor=["top", "left", "right"],
            exclusivity="exclusive",
            child=widgets.CenterBox(
                css_classes=["bar"],
                start_widget=widgets.Box(
                    spacing=6, child=[date_box(), Workspace()]),
                end_widget=widgets.Box(
                    spacing=6, child=[Tray(), Tools(), power_module()]),
            ),
        )


DynamicIsland(0)
Launcher(0)
Bar(0)
