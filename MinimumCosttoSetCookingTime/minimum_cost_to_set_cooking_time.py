import math

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        
        min_total_cost = float('inf')

        def calculate_cost(digits_str, current_startAt, current_moveCost, current_pushCost):
            actual_digits = digits_str.lstrip('0')
            
            if not actual_digits:
                actual_digits = "0"
            
            cost = 0
            current_finger_pos = current_startAt

            for digit_char in actual_digits:
                digit = int(digit_char)
                if digit != current_finger_pos:
                    cost += current_moveCost
                cost += current_pushCost
                current_finger_pos = digit
            return cost

        # Iterate through possible minute (m) values
        # A valid (m, s) pair must satisfy:
        # 0 <= m <= 99 (minutes are two digits)
        # 0 <= s <= 99 (seconds are two digits)
        # where s = targetSeconds - m * 60

        # Derive the range for m:
        # From s >= 0: targetSeconds - m * 60 >= 0  =>  m * 60 <= targetSeconds  =>  m <= targetSeconds / 60
        # From s <= 99: targetSeconds - m * 60 <= 99 =>  