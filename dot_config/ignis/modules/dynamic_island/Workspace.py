from ignis import widgets
from ignis.services.hyprland import HyprlandService
from utils.icons import getIcon


hyprland = HyprlandService.get_default()


class Workspace(widgets.Box):
    def __init__(self):

        # add workspaces
        self.workspace_list = [i.id for i in hyprland.workspaces]
        self.active_workspace = hyprland.active_workspace.id

        # active workspace title
        self.active_title = hyprland.active_window.title

        super().__init__(
            css_classes=["workspace-container"],
            spacing=50,
            child=[widgets.Box(
                css_classes=["workspace-btn-container"], child=self._create_workspace_buttons()),
            ]
        ),

        hyprland.connect("notify::active-workspace",
                         self._update_ui)

        hyprland.connect("notify::active-window", self._update_ui)

        # initial update
        self._update_ui()

    def _create_workspace_buttons(self):
        buttons = []
        for i in range(1, 6):
            id = i
            btn = widgets.Button(
                css_classes=["workspace-btn", f"workspace-btn-{str(id)}"],
                child=widgets.Box(
                    css_classes=["workspace-btn-inside-box"],
                    child=[widgets.Label(
                        css_classes=["workspace-btn-label",
                                     f"workspace-btn-label-{id}"],
                        label=str(id)),
                        widgets.Icon(
                        css_classes=["workspace-btn-icon"],
                            pixel_size=16)
                    ]))
            buttons.append(btn)

        self.buttons = buttons
        return buttons

    def _update_active_window_icon(self, *_):
        self.active_workspace = hyprland.active_workspace.id
        btn = self.buttons[self.active_workspace-1]
        box = btn.child
        icon = box.child[1]
        icon.image = getIcon(hyprland.active_window.initial_class)

    def _update_active_workspace(self, *_):
        self.active_workspace = hyprland.active_workspace.id
        for i, btn in enumerate(self.buttons):
            box = btn.child
            label = box.child[0]
            icon = box.child[1]
            if i+1 == self.active_workspace:
                icon.image = getIcon(
                    hyprland.active_window.initial_class)
                btn.add_css_class("active")
                label.add_css_class("active")
            else:
                btn.remove_css_class("active")
                label.remove_css_class("active")

    def _update_ui(self, *_):
        active_ws = hyprland.active_workspace.id
        windows = hyprland.windows

        ws_icons = {}

        # get all the windows and their active windows
        for win in windows:
            ws_id = win.workspace_id
            if 1 <= ws_id <= 5:
                ws_icons[ws_id] = win.initial_class

        # check for the active window and overwrite its icon
        if hyprland.active_window:
            active_win_ws = hyprland.active_window.workspace_id
            ws_icons[active_win_ws] = hyprland.active_window.initial_class

        # update the buttons
        for i, btn in enumerate(self.buttons):
            box = btn.child
            label = box.child[0]
            icon = box.child[1]
            if i+1 == active_ws:
                btn.add_css_class("active")
                label.add_css_class("active")
            else:
                btn.remove_css_class("active")
                label.remove_css_class("active")

            # updating the icon
            new_icon = getIcon(ws_icons.get(i+1, ""))
            if icon.image != new_icon:
                icon.image = new_icon
