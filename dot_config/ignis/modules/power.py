from ignis import widgets
from modules.widgets import power_options_widget


def power_module() -> widgets.Widget:
    return widgets.EventBox(
        css_classes=["top-pill"],
        child=[widgets.Button(css_classes=["tools-btn"], on_click=lambda _: power_options_widget.request_show(), child=widgets.Icon(css_classes=["tools-icon"],
                                                                                                                                    image="power-settings",
                                                                                                                                    pixel_size=24))]
    )
