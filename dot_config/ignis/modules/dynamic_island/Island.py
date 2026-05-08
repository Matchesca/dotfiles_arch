from ignis import widgets
from ignis.services.hyprland import HyprlandService
from modules.dynamic_island.IslandManager import IslandManager

hyprland = HyprlandService.get_default()
imanager = IslandManager()


class DynamicIsland(widgets.Window):
    def __init__(self, monitor: int):

        super().__init__(
            namespace=f"dynamic-island-{monitor}",
            css_classes=["dynamic-island"],
            anchor=["top"],
            exclusivity="ignore",
            dynamic_input_region=True,
            child=widgets.CenterBox(
                css_classes=["island-container"],
                center_widget=imanager.container
            ),
        )
