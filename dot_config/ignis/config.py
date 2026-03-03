from ignis import widgets
from modules.clock import date_box
from modules.power import power_module
from modules.network import network_module
from modules.audio import Audio_Module
from modules.dynamic_island.Island import DynamicIsland
from ignis.app import IgnisApp
import os

app = IgnisApp.get_default()
app.apply_css(os.path.expanduser("~/.config/ignis/styles/style.scss"))


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
                start_widget=date_box(),
                end_widget=widgets.Box(
                    css_classes=["information_panel"],
                    spacing=10,
                    child=[Audio_Module(), network_module(), power_module()])
            ),
        )


Bar(0)
DynamicIsland(0)
