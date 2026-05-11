from ignis import widgets
from ignis.services.hyprland import HyprlandService
from modules.dynamic_island.IslandManager import imanager

hyprland = HyprlandService.get_default()


class DynamicIsland(widgets.Window):
    def __init__(self, monitor: int):

        super().__init__(
            namespace=f"dynamic-island-{monitor}",
            css_classes=["dynamic-island"],
            anchor=["top"],
            exclusivity="ignore",
            dynamic_input_region=True,
            kb_mode="none",
            child=widgets.CenterBox(
                css_classes=["island-container"],
                center_widget=imanager.container
            ),
        )

        imanager.set_iwindow(self)
