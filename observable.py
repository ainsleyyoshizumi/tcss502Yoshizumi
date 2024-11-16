
class EyeOfSauron:
    def __init__(self):
        self._observers = []
        self._changed = False

    def add_observer(self, observer):
        observer._subject = self
        self._observers.append(observer)

    def remove_observer(self, observer):
        observer._subject = None
        self._observers.remove(observer)

    def notify_observer(self, hobbits, dwarves, elves, men):
        if self.has_changed():
            for observer in self._observers:
                observer.update(hobbits, dwarves, elves, men)
            self.clear_changed()

    def set_changed(self):
        self._changed = True

    def has_changed(self):
        return self._changed

    def clear_changed(self):
        self._changed = False

    def count_observers(self):
        return len(self._observers)

