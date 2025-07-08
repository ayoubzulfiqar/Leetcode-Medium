class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        m = len(rolls)
        
        total_rolls_count = n + m
        target_total_sum = mean * total_rolls_count
        
        current_rolls_sum = sum(rolls)
        
        required_missing_sum = target_total_sum - current_rolls_sum
        
        min_possible_missing_sum = n * 1
        max_possible_missing_sum = n * 6
        
        if required_missing_sum < min_possible_missing_sum or required_missing_sum > max_possible_missing_sum:
            return []
            
        missing_rolls_result = [0] * n
        
        base_value = required_missing_sum // n
        remainder = required_missing_sum % n
        
        for i in range(n):
            missing_rolls_result[i] = base_value
        
        for i in range(remainder):
            missing_rolls_result[i] += 1
            
        return missing_rolls_result