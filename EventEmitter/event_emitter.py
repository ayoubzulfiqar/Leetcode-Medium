class EventEmitter:
    def __init__(self):
        self._events = {}

    def subscribe(self, event_name, callback):
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(callback)

        def unsubscribe_method():
            if event_name in self._events and callback in self._events[event_name]:
                self._events[event_name].remove(callback)
                if not self._events[event_name]:
                    del self._events[event_name]
            return None

        return {"unsubscribe": unsubscribe_method}

    def emit(self, event_name, args=None):
        if args is None:
            args = []

        results = []
        callbacks_to_call = list(self._events.get(event_name, []))

        for callback in callbacks_to_call:
            results.append(callback(*args))
        return results