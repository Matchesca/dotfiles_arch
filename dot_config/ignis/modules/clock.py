import datetime
from ignis import widgets
from ignis import utils


def update_label(clock_label: widgets.Label) -> None:
    text = datetime.datetime.now().strftime("%-I:%M")
    clock_label.set_label(text)


def clock() -> widgets.Widget:
    clock_label = widgets.Label(
        justify="left",
        css_classes=["clock_label"]
    )
    utils.Poll(1000, lambda x: update_label(clock_label))
    return clock_label


def date_widget() -> widgets.Widget:
    date_label = widgets.Label(
        css_classes=["date_label"]
    )
    date_text = datetime.datetime.now().strftime("%a, %b %d")
    date_label.set_label(date_text)
    return date_label


def date_box() -> widgets.Widget:
    return widgets.Box(
        css_classes=["date_box"],
        vertical=True,
        child=[
            widgets.Box(
                child=[clock()],
            ),
            date_widget(),
        ],
    )
