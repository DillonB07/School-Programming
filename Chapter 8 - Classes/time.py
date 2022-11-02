class Time:
    def __init__(self, hour:int = 12, minute: int=0, second: int=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_second(self):
        return self.second

    def print_time(self):
        print(f'{self.hour}:{self.minute}:{self.second}')

    def set_hour(self, hour: int = 0):
        self.hour = hour

    def set_minute(self, minute: int = 0):
        self.minute = minute

    def set_second(self, second: int = 0):
        self.second = second

    def increment_second(self):
        self.second += 1
        if self.second >= 60:
            self.minute += 1
            self.second = 0
            

    def increment_minute(self):
        self.minute += 1
        if self.minute >= 60:
            self.hour += 1
            self.minute = 0
            

    def increment_hour(self):
        self.hour += 1
        if self.hour > 12:
            self.hour = 1


        
t_a = Time()
t_b = Time(6,38,57)

t_b.get_hour()
t_b.get_minute()
t_b.get_second()
t_b.print_time()

t_a.print_time()
t_a.set_hour(5)
t_a.set_minute(59)
t_a.set_second(6)

t_a.increment_hour()
t_a.increment_minute()

t_a.print_time()

