import datetime
from ignis import widgets
from ignis import utils


def update_label(clock_label: widgets.Label) -> None:
    text = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.set_label(text)


def bar(monitor: int) -> widgets.Window:
    clock_label = widgets.Label()

    utils.Poll(1000, lambda x: update_label(clock_label))

    return widgets.Window(
        namespace=f"some-window-{monitor}",
        monitor=monitor,
        child=widgets.Box(
            vertical=True,
            spacing=10,
            child=[clock_label],
        ),
    )


bar(0)
