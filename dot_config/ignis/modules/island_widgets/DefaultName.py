import getpass
import socket
from ignis import widgets
from modules.dynamic_island.IslandManager import islandManager
from modules.managers.Manager import ManagerWidget


class DefaultNameWidget(ManagerWidget):
    def __init__(self):
        self.hostname = socket.gethostname()
        self.user = getpass.getuser()
        self.name_box = widgets.CenterBox(
            css_classes=["default-name-box"],
            center_widget=widgets.Label(
                css_classes=["default-name-label"], label=f"{self.user}@{self.hostname}")
        )
        super().__init__(child=self.name_box,
                         manager=islandManager, title="default", priority=-1)
        self.register()
        self.request_show()
