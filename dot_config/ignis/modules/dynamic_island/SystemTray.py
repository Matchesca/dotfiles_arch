from ignis.services.system_tray import SystemTrayService
from ignis import widgets

sys_tray = SystemTrayService.get_default()


class Tray(widgets.EventBox):

    def __init__(self):
        self.items = {}

        super().__init__(
            css_classes=["system-tray-box"],
            spacing=10
        )

        sys_tray.connect("added", lambda x, item: self._on_added(item))

    def _on_added(self, item):
        tray_item = TrayItem(item)
        self.items[item.id] = tray_item
        item.connect("removed", lambda x: self._on_removed(item.id))
        self._render()

    def _on_removed(self, id):
        if id in self.items:
            del self.items[id]
            self._render()
        else:
            print("Error system tray item not found")

    def _render(self):
        self.child = list(self.items.values())


class TrayItem(widgets.Button):

    def __init__(self, item):

        tray_icon = widgets.Icon(
            css_classes=["system-tray-item-icon"],
            image=item.icon,
            pixel_size=16
        )

        super().__init__(
            css_classes=["system-tray-item-button"],
            child=tray_icon
        )
