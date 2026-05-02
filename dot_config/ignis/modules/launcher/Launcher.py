from ignis import widgets
from ignis.services.applications import ApplicationsService
from ignis.services.applications import Application


app = ApplicationsService.get_default()


class Launcher(widgets.Window):

    def __init__(self, monitor):

        all_apps = app.apps

        super().__init__(
            namespace=f"launcher-{monitor}",
            css_classes=["launcher-window"],
            anchor=["top"],

        )


class AppItem(widgets.Box):

    def __init__(self, app: Application):

        self.lbl = widgets.Label(label=app.name)
        self.icon = widgets.Icon(image=app.icon, pixel_size=40)
        super().__init__(
            css_classes=["appitem-box"],
            vertical=True,
            spacing=5,
            child=[self.icon, self.lbl]
        )
