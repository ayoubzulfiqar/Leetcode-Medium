class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.bookings:
            if startTime < end and start < endTime:
                return False
        
        self.bookings.append([startTime, endTime])
        return True