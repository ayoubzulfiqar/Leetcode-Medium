class Solution:
    def nextClosestTime(self, time: str) -> str:
        hours_str, minutes_str = time.split(':')
        current_minutes = int(hours_str) * 60 + int(minutes_str)

        available_digits = set()
        for char_digit in time:
            if char_digit != ':':
                available_digits.add(int(char_digit))

        for _ in range(1, 24 * 60 + 1):
            current_minutes = (current_minutes + 1) % (24 * 60)
            
            next_H = current_minutes // 60
            next_M = current_minutes % 60
            
            next_HH_str = f"{next_H:02d}"
            next_MM_str = f"{next_M:02d}"

            is_valid = True
            for char_digit in next_HH_str + next_MM_str:
                if int(char_digit) not in available_digits:
                    is_valid = False
                    break
            
            if is_valid:
                return f"{next_HH_str}:{next_MM_str}"
        
        # This part should theoretically not be reached given the problem constraints
        # that a valid time will always be found (at least the original time itself
        # on the next day if no other combination is possible).
        return ""