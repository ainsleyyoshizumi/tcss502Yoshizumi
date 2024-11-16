from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self, observable):
        observable.register_observer(self)

    @abstractmethod
    def update(self, hobbits, dwarves, elves, men):
        pass