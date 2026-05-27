from ignis import widgets

# Priority: -1 default, 0 non-essential active, 1 OSD, 2 notification, 3 urgent notification, 4 kb focus


class ManagerWidget(widgets.StackPage):
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


class Manager():
    def __init__(self, transition_type="slide_down"):
        self.active_widget = None
        self.iwindow = None
        self.kb_mode_window = "none"
        self.widgets = {-1: [], 0: [], 1: [], 2: [], 3: [], 4: []}
        self.container = widgets.Stack(
            transition_type=transition_type,
            transition_duration=300
        )
        self.container.hhomogeneous = False
        self.container.vhomogeneous = False
        self.container.interpolate_size = True

    def set_iwindow(self, iwindow):
        self.iwindow = iwindow

    def show(self, widget):
        self.container.set_visible_child_name(widget.widget_title)
        self.container.grab_focus()

        if widget.needs_kb:
            self.iwindow.set_kb_mode("exclusive")
            widget.focus_for_kb()

    def hide(self, widget):
        if widget.needs_kb:
            self.iwindow.set_kb_mode("none")
        self._show_next(widget.widget_title)

    def add_widget(self, widget):
        if widget not in self.widgets:
            self.widgets[widget.priority].append(widget)
            self.container.add_titled(
                child=widget.child, title=widget.widget_title, name=widget.widget_title)

    def _show_by_name(self, name):
        self.container.set_visible_child_name(name)

    # Write an algorithm to figure out priorities and the best next widget to show, if nothing to show then default
    def _show_next(self, hiding_name: str):
        for priority in sorted(self.widgets.keys(), reverse=True):
            if priority < 0:
                continue  # Skip default priority until the very end

            for w in self.widgets[priority]:
                if w.active and w.widget_title != hiding_name:
                    self.show(w)
                    return

        self._show_by_name("default")
