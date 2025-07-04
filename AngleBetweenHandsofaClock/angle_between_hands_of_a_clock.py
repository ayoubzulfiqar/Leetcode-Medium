class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculate the angle of the minute hand
        # 60 minutes = 360 degrees, so 1 minute = 6 degrees
        minute_angle = minutes * 6

        # Calculate the angle of the hour hand
        # 12 hours = 360 degrees, so 1 hour = 30 degrees
        # The hour hand also moves with the minutes
        # For every minute, the hour hand moves 30/60 = 0.5 degrees
        
        # Adjust hour for 12 o'clock (12 becomes 0 for calculation purposes)
        if hour == 12:
            hour = 0
        
        hour_angle = (hour * 30) + (minutes * 0.5)

        # Calculate the absolute difference between the angles
        diff = abs(hour_angle - minute_angle)

        # The smaller angle is either diff or 360 - diff
        return min(diff, 360 - diff)