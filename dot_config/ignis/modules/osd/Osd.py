from ignis import widgets


class OSDManager(widgets.Window):

    def __init__(self, monitor):

        super().__init__(
            namespace=f"osd-{monitor}",
            css_classes=["osd-window"],
            anchor=["top", "left", "right"],

            child=widgets.CenterBox(
                center_widget=widgets.Label(label="hellow manh")
            )
        )
