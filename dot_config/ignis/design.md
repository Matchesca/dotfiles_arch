## Island Manager

- This class should manage the visible widget on the dynamic island.
- It should also handle widgets of different priorities.
- It should handle notifications on top of other active widgets.

### Design

- A list of all the registered widgets that can be displayed on the island.
- Call handler to accept requests to be displayed on the island.
  - With a queue mechanism??
- Call handler to accept remove requests on the island

### Island widget

- The class should also provide a class that can be inherited to implement island widgets specifically.

#### Notes

- When i log in the default widget is visible. When music starts playing the media widgets asks the manager to be showed.
- The manager puts media widget on
- When music stops media widget asks to be put out.
- How can the media widget call manager and manager know who is talking and what to show.
  - One solution is to have a manager widget as the parent with overlay as the widget type.
  - A widget registers with the manager and the manager adds that widgets revealer to the manager overlay class
  - When a widget registers, the widget id and the widget is added to a hashmap.
  - A listener is attached to the widget for requests, so that the manager knows who is calling.
- Will the media have to register with the manager first to be put on the list.
