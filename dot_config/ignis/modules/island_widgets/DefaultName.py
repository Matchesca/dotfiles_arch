import getpass
import socket
from ignis import widgets
from modules.dynamic_island.IslandManager import IslandWidget, imanager


class DefaultNameWidget(IslandWidget):
    def __init__(self):
        self.hostname = socket.gethostname()
        self.user = getpass.getuser()
        self.name_box = widgets.CenterBox(
            css_classes=["default-name-box"],
            center_widget=widgets.Label(
                css_classes=["default-name-label"], label=f"{self.user}@{self.hostname}")
        )
        super().__init__(child=self.name_box, manager=imanager, title="default", priority=-1)
        self.register()
        self.request_show()
