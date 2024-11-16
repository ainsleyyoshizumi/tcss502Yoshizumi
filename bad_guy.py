from observer import Observer

class BadGuy(Observer):
    def __init__(self, eye, name):
        self.name = name
        self.eye = eye
        self.eye.add_observer(self)

    def update(self, hobbits, dwarves, elves, men):
        print (f"{self.name} has spotted {hobbits} hobbits, {dwarves} dwarves, {elves} elves, and {men} men.")

    def defeated(self):
        self.eye.remove_observer(self)
        print(f"{self.name} has defeated {self.eye}")


