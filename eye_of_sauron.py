from observable import EyeOfSauron

class EyeOfSauron(EyeOfSauron):

    def setEnemies(self, hobbits, dwarves, elves, men):
        self.set_changed()
        self.notify_observer(hobbits, dwarves, elves, men)

    def __str__(self):
        return "Eye of Sauron"