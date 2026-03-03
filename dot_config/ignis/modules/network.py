from ignis import widgets
from ignis import utils
from ignis.services.network import NetworkService
from . import constants


ntw = NetworkService.get_default()


def get_icon(*args) -> str:
    if ntw.wifi.is_connected:
        return ntw.wifi.icon_name
    elif ntw.ethernet.is_connected:
        return "settings_ethernet"
    else:
        return "network-offline-symbolic"


def network_module() -> widgets.Widget:
    ntw_icon = widgets.Label(
        css_classes=["material-icon", "network-icon"],
        label=get_icon())

    # updater
    def update_icon(*args):
        ntw_icon.image = get_icon()

    # connect to signals
    ntw.wifi.connect("notify::is-connected", update_icon)
    ntw.ethernet.connect("notify::is-connected", update_icon)

    return widgets.Box(
        css_classes=["network_module"],
        child=[ntw_icon],
    )
