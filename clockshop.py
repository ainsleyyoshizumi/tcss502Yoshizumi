from clock import Clock


class ClockShop:
    def __init__(self):
        self._clocks = []

    def fill_clock_shop(self, list_of_times):
        for time in list_of_times:
            hour, minute, second = map(int, time.split(":"))
            new_clock = Clock(hour, minute, second)
            self._clocks.append(new_clock)

    def sort_clocks(self):
        self._clocks.sort()

    def find_clock(self, a_clock):
        for index, clock in enumerate(self._clocks):
            if clock == a_clock:
                return index
        return -1

    def __str__(self):
        return "\n".join(str(clock) for clock in self._clocks) + ("\n" if self._clocks else "")

    def get_clock(self, index):
        if 0 <= index < len(self._clocks):
            return self._clocks[index]
        else:
            raise IndexError("Index out of range")

    def set_clock(self, a_clock, index):
        if 0 <= index < len(self._clocks):
            self._clocks[index] = a_clock
        else:
            raise ValueError("Index out of range")
