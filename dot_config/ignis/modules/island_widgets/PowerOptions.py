import os
from ignis import widgets
from gi.repository import Gtk
from modules.dynamic_island.IslandManager import islandManager
from modules.managers.Manager import ManagerWidget


class PowerOptionsWidget(ManagerWidget):
    def __init__(self):
        self.buttons = [
            widgets.Button(css_classes=[
                "power-options-button"], on_click=lambda _: os.system("shutdown now"), child=widgets.Icon(pixel_size=50, image="power-settings-new")),
            widgets.Button(css_classes=[
                "power-options-button"], on_click=lambda _: os.system("reboot"), child=widgets.Icon(pixel_size=50, image="autorenew")),
            widgets.Button(css_classes=[
                "power-options-button"], child=widgets.Icon(pixel_size=50, image="lock"))
        ]
        self.focus_index = -1
        self.main_box = widgets.Box(
            css_classes=["power-options-box"],
            spacing=22,
            child=self.buttons
        )
        super().__init__(manager=islandManager, child=self.main_box,
                         title="power-options", needs_kb=True, priority=4)

        self.register()

        key_controller = Gtk.EventControllerKey()
        key_controller.set_propagation_phase(Gtk.PropagationPhase.CAPTURE)
        self.main_box.add_controller(key_controller)

        key_controller.connect("key-pressed", self.on_key_pressed)

    def on_key_pressed(self, event_controller_key, keyval, keycode, state):
        if keycode == 65289:
            self._handle_tab_input()
            return True

        if keyval == 65307:
            self.request_hide()
            return True
        return False

    def _handle_tab_input(self):
        self.focus_index = (self.focus_index + 1) % len(self.buttons)

        target = self.buttons[self.focus_index]
        target.grab_focus()

    def focus_for_kb(self):
        self.buttons[0].grab_focus()
