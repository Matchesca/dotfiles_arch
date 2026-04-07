from ignis import widgets
from modules.dynamic_island.Pomodoro import Pomodoro


class WidgetWindow(widgets.Window):
    def __init__(self, monitor: int):

        super().__init__(
            namespace=f"widgets-container-{monitor}",
            css_classes=["widgets-container"],
            anchor=["top", "right"],
            exclusivity="ignore",
            child=Pomodoro()
        )
