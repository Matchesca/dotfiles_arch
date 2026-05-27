from modules.managers.Manager import Manager
from modules.managers.Manager import ManagerWidget
from ignis import widgets


osd_manager = Manager(transition_type="crossfade")


class OSD(widgets.Window):
    def __init__(self, monitor: int):
        super().__init__(
            namespace=f"OSD-{monitor}",
            css_classes=["OSD"],
            layer="overlay",
            anchor=["top"],
            exclusivity="ignore",
            kb_mode="none",
            margin_top=50,
            child=widgets.CenterBox(
                css_classes=["OSD-container"],
                center_widget=osd_manager.container)
        ),
        osd_manager.set_iwindow(self)


class Dummy(ManagerWidget):
    def __init__(self):
        self.dummy_box = widgets.Box()
        super().__init__(child=self.dummy_box, manager=osd_manager, title="default")

        self.register()


d = Dummy()
