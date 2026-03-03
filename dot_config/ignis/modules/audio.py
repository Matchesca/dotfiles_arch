from ignis import widgets
from ignis.services.audio import AudioService
import asyncio

audio = AudioService.get_default()


class Audio_Module(widgets.Box):
    def __init__(self):
        self.audio_icon = widgets.Label(
            css_classes=["material-icon", "audio-icon"])

        def get_volume_icon(volume, is_muted):
            if is_muted or volume == 0:
                return "volume_mute"
            elif volume <= 33:
                return "volume_down"
            else:
                return "volume_up"

        self.audio_icon.bind_property2("label", audio.speaker, [
                                       "volume", "is-muted"], transform=lambda vol, muted: get_volume_icon(vol, muted))

        self.volume_slider = widgets.Scale(
            min=0,
            max=100,
            step=1,
            draw_value=False,
            value=audio.speaker.bind("volume"),
            on_change=lambda x: audio.speaker.set_volume(x.value),
            css_classes=["volume-slider"],  # customize style in style.css
        )

        self.slider_revealer = widgets.Revealer(
            child=self.volume_slider, transition_type='slide_left', transition_duration=400
        )

        super().__init__(
            child=[self.audio_icon, self.slider_revealer]
        )

        self.hide_task = None

        audio.speaker.connect("notify::volume", self.show_slider)

    def show_slider(self, *_):
        self.slider_revealer.reveal_child = True

        # If already opened and cancelling, keep it open
        if self.hide_task:
            self.hide_task.cancel()
        self.hide_task = asyncio.create_task(self.hide_slider())

    async def hide_slider(self, *_):
        await asyncio.sleep(2)
        self.slider_revealer.reveal_child = False
