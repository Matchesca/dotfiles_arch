from ignis import widgets
from ignis.services.mpris import MprisService
from ignis.utils import Utils
from utils.icons import getIcon
from utils.color import get_colors

mpris = MprisService.get_default()


class Media(widgets.Overlay):
    def __init__(self):
        self.factory = MediaFactory()
        self.players = {}
        self.active_player = None

        super().__init__(css_classes=["media-container"], overflow="hidden")

        mpris.connect("player_added", lambda x,
                      player: self._add_player(player))

    def _add_player(self, player, *_):
        item = PlayerItem(player, self.factory.get_strategy(player.identity))
        item.add_css_class("active")

        # flash the newly added player
        if not self.active_player:
            self.active_player = item
        else:
            previous_item = self.active_player
            self.active_player = item
            Utils.Timeout(ms=3000, target=lambda: self._flash_animation(
                previous_item, item))

        self.players[player] = item
        self.add_overlay(item)
        player.connect("closed", lambda x: self._remove_player(player))

    def _remove_player(self, player):
        if player in self.players:
            item = self.players.pop(player)
            self.remove_overlay(item)

            # if current active player is removed
            if self.active_player == item:
                if len(self.players) > 0:
                    # Pick the last player added to the dict as the new primary
                    new_active = list(self.players.values())[-1]

                    self.active_player = new_active
                    new_active.remove_css_class("peek")
                    new_active.add_css_class("active")
                else:
                    self.active_player = None
            print(f"removed {player}")

    def _flash_animation(self, previous_item, new_item):
        self.active_player = previous_item
        new_item.remove_css_class("active")
        new_item.add_css_class("peek")


class PlayerItem(widgets.Box):
    def __init__(self, player, strategy):
        self.player = player
        self.strat = strategy

        self.title_label = widgets.Label(
            ellipsize="end", max_width_chars=14, wrap_mode="word")
        self.title_art = widgets.Picture(css_classes=["title-art"])
        self.title_icon = widgets.Icon(
            css_classes=["title-icon"], pixel_size=22)

        self.buttons_container = widgets.Box(
            css_classes=["button-container"],
            child=[widgets.Button(
                css_classes=["play-button"],
                child=widgets.Icon(
                    pixel_size=22,
                    css_classes=["button-label"], image=getIcon("play"))
            )]
        )

        super().__init__(css_classes=["player-item"],
                         spacing=6,
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
            self._apply_color()
        elif icon["type"] == "icon":
            self.title_icon.image = icon["source"]
            self.title_icon.visible = True
            self.title_art.visible = False

    def _apply_color(self):
        theme = get_colors(self.title_art.image)
        self.style = f"background-color: {theme["background"]};"
        self.title_label.style = f"color: {theme["on-surface"]};"
        play_button = self.buttons_container.child[0]
        play_button.style = f"background-color: {theme["primary-container"]};"


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
