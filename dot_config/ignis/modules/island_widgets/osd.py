from ignis import widgets
from modules.dynamic_island.IslandManager import imanager, IslandWidget


class OSDManager(IslandWidget):
    def __init__(self):
        self.main_box = widgets.Box(css_classes=["osd-main-box"])
        super().__init__(manager=imanager, child=self.main_box, priority=1, title="OSD")
