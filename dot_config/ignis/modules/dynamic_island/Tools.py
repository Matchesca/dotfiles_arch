import subprocess
from ignis import widgets

SCREENSHOT_OUTPUT = "~/Pictures"


class Tools(widgets.EventBox):
    def __init__(self):

        super().__init__(
            spacing=12,
            css_classes=["tools-container"],
            child=[widgets.Button(
                on_click=lambda _: self._on_screenshot(),
                css_classes=["tools-btn"],
                child=widgets.Icon(
                    css_classes=["tools-icons"],
                    image="screenshot-region-symbolic", pixel_size=22))]
        )

    def _on_screenshot(self):
        subprocess.Popen(["hyprcap", "shot", "region", "-w", "-c"])
