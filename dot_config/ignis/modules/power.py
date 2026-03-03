from ignis import widgets
from ignis import utils
from . import constants


def power_module() -> widgets.Widget:
    return widgets.Box(
        css_classes=["power_module"],
        child=[widgets.Label(css_classes=["material-icon", "power-icon"],
                             label='power_settings_new')]
    )
