from ignis import widgets
from ignis.services.mpris import MprisService
from utils.icons import getIcon


# Should show the current active media.
# If not active media then suggest something idk what yet

mpris = MprisService.get_default()


class Media(widgets.Box):

    def __init__(self):
        self.factory = MediaFactory()
        self.players = {}

        super().__init__(css_classes=["media-container"], overflow="hidden")

        mpris.connect("player_added", lambda x,
                      player: self._add_player(player))

    def _add_player(self, player, *_):
        id = player.identity
        item = PlayerItem(player, self.factory.get_strategy(player.identity))
        self.players[player] = item
        self.append(item)
        player.connect("closed", lambda x: self._remove_player(id))

    def _remove_player(self, id):
        if id in self.players:
            item = self.players.pop(id)
            self.remove(item)
            print(f"removed {id}")


class PlayerItem(widgets.Box):
    def __init__(self, player, strategy):
        self.player = player
        self.strat = strategy

        self.title_label = widgets.Label(
            ellipsize="end", max_width_chars=16, wrap_mode="word")
        self.title_art = widgets.Picture()
        self.title_icon = widgets.Icon(pixel_size=22)

        super().__init__(css_classes=["player-item"],
                         spacing=12,
                         child=[self.title_art, self.title_icon, self.title_label])

        player.connect("notify::title", lambda x,
                       y: self._sync())
        self._sync()

    def _sync(self):
        self.title_label.label = self.player.title

        icon = self.strat.get_icon(self.player)

        if icon["type"] == "picture":
            self.title_art.image = icon["source"]
            self.title_icon.visible = False
            self.title_art.visible = True
        elif icon["type"] == "icon":
            self.title_icon.image = icon["source"]
            self.title_icon.visible = True
            self.title_art.visible = False


class BaseMediaStrategy():
    def get_background_color(self): return "gray"

    def get_icon(self, player):
        return {
            "type": "icon",
            "source": "audio-x-generic"
        }


class SpotifyStrategy(BaseMediaStrategy):

    def get_icon(self, player):
        return {
            "type": "picture",
            "source": player.art_url
        }


class BrowserStrategy(BaseMediaStrategy):

    def get_icon(self, player):
        return {
            "type": "icon",
            "source": getIcon("zen")
        }


class MediaFactory():
    @staticmethod
    def get_strategy(id):
        id = id.lower()
        if "spotify" in id:
            return SpotifyStrategy()
        if "zen" in id:
            return BrowserStrategy()
        return BaseMediaStrategy()
