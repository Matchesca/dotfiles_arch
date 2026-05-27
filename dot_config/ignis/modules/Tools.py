import subprocess
from ignis import widgets
from modules.island_widgets.widgets import pomodoro_timer

SCREENSHOT_OUTPUT = "~/Pictures"


class Tools(widgets.EventBox):
    def __init__(self):

        super().__init__(
            spacing=6,
            css_classes=["top-pill"],
            child=[widgets.Button(
                   on_click=lambda _: pomodoro_timer.request_show(),
                   css_classes=["tools-btn"],
                   child=widgets.Icon(
                       css_classes=["tools-icons"],
                       image="timer-symbolic", pixel_size=22)),
                   widgets.Button(
                on_click=lambda _: self._on_screenshot(),
                css_classes=["tools-btn"],
                child=widgets.Icon(
                    css_classes=["tools-icons"],
                    image="screenshot-region-symbolic", pixel_size=22)),
                   ]
        )

    def _on_screenshot(self):
        subprocess.Popen(["hyprcap", "shot", "region", "-w", "-c"])
