class Time:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def minToSec(self):
        return self.minutes * 60 + self.seconds
