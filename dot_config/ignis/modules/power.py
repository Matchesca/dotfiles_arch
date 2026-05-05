from ignis import widgets


def power_module() -> widgets.Widget:
    return widgets.EventBox(
        css_classes=["top-pill"],
        child=[widgets.Button(css_classes=["tools-btn"], on_click=lambda _: print("hello"), child=widgets.Icon(css_classes=["tools-icon"],
                                                                                                               image="power-settings",
                                                                                                               pixel_size=24))]
    )


class PowerOSD(widgets.Window):
    def __init__(self, monitor):
        super().__init__(
            namespace="power-menu-osd",
            anchor=["top", "bottom", "left", "right"],
            layer="overlay",
            kb_mode="exclusive",
            exclusivity="exclusive",
            popup=True,
            visible=False,
            child=widgets.Box(
                css_classes=["power-osd-blur"],
                spacing=20,
                child=[

                ]
            )
        )
