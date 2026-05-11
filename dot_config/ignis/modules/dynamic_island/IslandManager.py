from ignis import widgets

# Priority: -1 default, 0 non-essential active, 1 notification, 2 urgent notification, 3 kb focus


class IslandWidget(widgets.StackPage):
    def __init__(self, manager, child, title, priority=0, needs_kb=False):
        self.manager = manager
        self.priority = priority
        self.needs_kb = needs_kb
        self.widget_title = title
        self.active = False
        super().__init__(child=child, title=self.widget_title)

    def request_show(self):
        self.active = True
        self.manager.show(self)

    def focus_for_kb(self):
        if self.needs_kb:
            raise NotImplementedError(
                "Widget must focus on its first button or element")

    def request_hide(self):
        self.active = False
        self.manager.hide(self)

    def register(self):
        self.manager.add_widget(self)


class IslandManager():
    def __init__(self):
        self.active_widget = None
        self.iwindow = None
        self.kb_mode_window = "none"
        self.widgets = {-1: [], 0: [], 1: [], 2: [], 3: []}
        self.container = widgets.Stack(
            transition_type="slide_down",
            transition_duration=300
        )
        self.container.hhomogeneous = False
        self.container.vhomogeneous = False
        self.container.interpolate_size = True

    def set_iwindow(self, iwindow):
        self.iwindow = iwindow

    def show(self, widget: IslandWidget):
        if widget.needs_kb:
            self.iwindow.set_kb_mode("exclusive")
            widget.focus_for_kb()
        self.container.set_visible_child_name(widget.widget_title)

    def hide(self, widget: IslandWidget):
        if widget.needs_kb:
            self.iwindow.set_kb_mode("none")
        self._show_next(widget.widget_title)

    def add_widget(self, widget: IslandWidget):
        if widget not in self.widgets:
            self.widgets[widget.priority].append(widget)
            self.container.add_titled(
                child=widget.child, title=widget.widget_title, name=widget.widget_title)

    def _show_by_name(self, name):
        self.container.set_visible_child_name(name)

    def _show_next(self, hiding_name: str):
        if len(self.widgets[0]) > 0:
            for w in self.widgets[0]:
                if w.active and w.widget_title != hiding_name:
                    self.show(w)
                    return
        self._show_by_name("default")


imanager = IslandManager()
