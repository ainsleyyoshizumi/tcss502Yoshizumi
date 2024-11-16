from datetime import datetime

class Clock:       #create a Clock object and specify the starting hour, minute, and second via parameters (we will use integer values for our data)

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self): #gets current time in string format

        return f"{self.hour:0}:{self.minute:0}:{self.second:0}"

    __repr__= __str__ #same as __str__ for what we are doing

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_second(self):
        return self.second

    def set_hour(self, new_hour):
        if not (0<= new_hour <= 23):
            raise ValueError("New hour must be between 0 and 23.")

        self.hour = new_hour

    def set_minute(self, new_minute):
        if not (0<= new_minute <= 59):
            raise ValueError("New minute must be between 0 and 59.")

        self.minute = new_minute

    def set_second(self, new_second):
        if not (0<= new_second <= 59):
            raise ValueError("New second must be between 0 and 59.")

        self.second = new_second

    def advance_hour(self, amount_to_advance):
        if amount_to_advance < 0:
            raise ValueError("Amount must be more than 0.")
        self.hour = (self.hour + amount_to_advance) % 24

    def advance_minute(self, amount_to_advance): #hour needs to update accordingly, if time == 8:30 and I add 30 mins, its need to update to 9
        if amount_to_advance < 0:
            raise ValueError("Amount must be more than 0.")
        total_min = self.minute + amount_to_advance
        self.hour = (self.hour + total_min // 60) % 24
        self.minute = total_min % 60

    def set_to_current_time(self):
        now = datetime.now()
        self.hour = now.hour
        self.minute = now.minute
        self.second = now.second

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return self.hour == other.hour and self.minute == other.minute and self.second == other.second

    def __lt__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        if self.hour != other.hour:
            return self.hour < other.hour
        if self.minute != other.minute:
            return self.minute < other.minute
        return self.second < other.second

    def __gt__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        if self.hour != other.hour:
            return self.hour > other.hour
        if self.minute != other.minute:
            return self.minute > other.minute
        return self.second > other.second



