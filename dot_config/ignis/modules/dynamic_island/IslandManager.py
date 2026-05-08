from ignis import widgets


class IslandWidget(widgets.Revealer):
    def __init__(self, manager, child, priority=0):
        self.manager = manager
        self.priority = priority
        super().__init__(transition_type="slide_down", transition_duration=500, child=child)

    def request_show(self):
        self.manager.show(self)

    def request_hide(self):
        self.manager.hide(self)

    def register(self):
        self.manager.add_widget(self)


class IslandManager():
    def __init__(self):
        self.active_widget = None
        self.widgets = {}
        self.container = widgets.Overlay()

    def show(self, widget: IslandWidget):
        widget.reveal_child = True

    def hide(self, widget: IslandWidget):
        widget.reveal_child = False

    def add_widget(self, widget: IslandWidget):
        if widget not in self.widgets:
            self.widgets[widget] = 0
            self.container.add_overlay(widget)
