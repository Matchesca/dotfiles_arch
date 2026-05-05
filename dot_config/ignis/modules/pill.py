from ignis import widgets


class Pill(widgets.Box):
    def __init__(self):
        super().__init__(
            css_classes=["top-pill"],
            spacing=5
        )
