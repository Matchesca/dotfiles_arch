from ignis import widgets
from gi.repository import GLib


class Pomodoro(widgets.EventBox):

    def __init__(self):
        self.total_time = 50 * 60
        self.time_left = self.total_time
        self.is_running = False

        self.time_label = widgets.Label(
            css_classes=["pomodoro-label"], label="50:00")

        self.reset_button = widgets.Button(
            visible=False,
            css_classes=["pomodoro-btn"], child=widgets.Icon(image="replay-symbolic", pixel_size=18),
            on_click=lambda x: self._reset()
        )

        self.pause_icon = widgets.Icon(
            visible=False, image="pause-symbolic", pixel_size=22)
        self.play_icon = widgets.Icon(
            image="play-arrow-symbolic", pixel_size=22)

        play_pause_button = widgets.Button(
            css_classes=["pomodoro-btn"],
            child=widgets.Box(child=[self.pause_icon, self.play_icon]),
            on_click=lambda x: self.toggle_timer()
        )

        self.btn_box = widgets.EventBox(
            child=[self.reset_button, play_pause_button]
        )

        super().__init__(
            css_classes=["pomodoro-container"], child=[widgets.CenterBox(css_classes=["pomodoro-inside-box"], hexpand=True, start_widget=self.time_label, end_widget=self.btn_box)])

    def toggle_timer(self):
        if not self.is_running:
            self.is_running = True
            self.play_icon.visible = False
            self.pause_icon.visible = True
            self.reset_button.visible = False

            GLib.timeout_add(1000, self._on_tick)
        else:
            self.is_running = False
            self.play_icon.visible = True
            self.pause_icon.visible = False
            self.reset_button.visible = True

    def _reset(self):
        self.is_running = False
        self.time_left = self.total_time
        self.update_ui()

        self.reset_button.visible = False
        self.play_icon.visible = True
        self.pause_icon.visible = False

    def _on_tick(self):
        if not self.is_running:
            return False

        if self.time_left > 0:
            self.time_left -= 1
            self.update_ui()
            return True  # Keep ticking

        # Timer reached 0
        self.is_running = False
        return False

    def update_ui(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.time_label.label = f"{minutes:02d}:{seconds:02d}"
