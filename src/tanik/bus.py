class EventBus:
    def __init__(self):
        self._subscribers = {}

    def connect(self, event_name, callback):
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(callback)

    def disconnect(self, event_name, callback):
        if event_name in self._subscribers:
            self._subscribers[event_name].remove(callback)

    def emit(self, event_name, *args, **kwargs):
        if event_name in self._subscribers:
            for callback in self._subscribers[event_name]:
                callback(*args, **kwargs)

bus = EventBus()