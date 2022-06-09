class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def print_time(self):
        print(self.hours + ":" + self.minutes + ":" + self.seconds)

    def is_AM(self):
        if (self.hour < 12):
            return True
        else:
            return False

    def is_AM(self):
        if (self.hour > 11):
            return True
        else:
            return False

    def elapsed_time(self, end_time, in_seconds):
        returned = [self.hours, self.minutes, self.seconds]
        beg_sec = self.hours*3600+self.minutes*60+self.seconds
        end_sec=end_time.hours*3600+end_time.minutes*60+end_time.seconds
        if in_seconds:
            return abs(beg_sec-end_sec)
        else:
            return abs((beg_sec-end_sec)/60)
