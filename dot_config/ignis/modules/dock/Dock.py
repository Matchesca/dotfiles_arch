from ignis import widgets


class Dock(widgets.Window):

    def __init__(self, monitor):
        super().__init__(
            namespace=f"dock-{monitor}",
            css_classes=["dock"],
            anchor=["bottom"],
            exclusivity="ignore",
            child=None
        )
