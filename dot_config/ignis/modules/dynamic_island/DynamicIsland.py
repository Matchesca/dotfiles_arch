from ignis import widgets
from modules.dynamic_island.IslandManager import imanager


class DynamicIsland(widgets.Window):
    def __init__(self, monitor: int):
        super().__init__(
            namespace=f"dynamic-island-{monitor}",
            css_classes=["dynamic-island"],
            layer="overlay",
            anchor=["top"],
            exclusivity="ignore",
            kb_mode="none",
            child=widgets.CenterBox(
                css_classes=["island-container"],
                center_widget=imanager.container),
        ),
        imanager.set_iwindow(self)
