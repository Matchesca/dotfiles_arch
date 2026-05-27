from gi.repository import GLib  # Used to handle the hide delay timer
from modules.managers.Manager import ManagerWidget
from modules.osd.OSDManager import osd_manager
from ignis import widgets
from ignis.services.audio import AudioService
import gi
gi.require_version('GLib', '2.0')


class Volume(ManagerWidget):
    def __init__(self):
        self.audio = AudioService.get_default()
        self.value = self.audio.speaker.volume

        self.timeout_id = None
        self.scale = widgets.Scale(css_classes=[
                                   "test-slider"], vertical=False, min=0, max=100, step=1, draw_value=False, value=self.value)

        self.volume_box = widgets.Box(
            css_classes=["volume-box"], child=[self.scale])
        super().__init__(child=self.volume_box, manager=osd_manager,
                         title="volume_slider", priority=1)

        self.register()
        self.audio.speaker.connect("notify::volume", self.on_volume_change)

    def on_volume_change(self, speaker, *args):
        self.request_show()

        self.value = speaker.volume
        self.scale.set_value(self.value)

        # Clear any active pending timeout so it doesn't hide mid-adjustment
        if self.timeout_id is not None:
            GLib.source_remove(self.timeout_id)

        self.timeout_id = GLib.timeout_add(2500, self._auto_hide_callback)

    def _auto_hide_callback(self):
        self.request_hide()
        self.timeout_id = None
        return False
