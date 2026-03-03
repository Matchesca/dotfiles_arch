from ignis import widgets
from ignis.services.hyprland import HyprlandService
from modules.dynamic_island.Workspace import Workspace
from modules.dynamic_island.Media import Media


hyprland = HyprlandService.get_default()


class DynamicIsland(widgets.Window):
    def __init__(self, monitor: int):

        super().__init__(
            namespace=f"dynamic-island-{monitor}",
            css_classes=["dynamic-island"],
            anchor=["top"],
            exclusivity="ignore",
            child=widgets.CenterBox(
                css_classes=["island-container"],
                start_widget=widgets.Box(
                    child=[
                        Workspace(),
                    ]),
                center_widget=Media()
            ),
        )
