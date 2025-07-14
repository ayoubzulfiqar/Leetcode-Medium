import math

def _gcd(a, b):
    return math.gcd(a, b)

def _lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // _gcd(a, b)

def calculate_gcd_of_list(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    result = arr[0]
    for i in range(1, len(arr)):
        result = _gcd(result, arr[i])
    return result

def calculate_lcm_of_list(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
        
    result = arr[0]
    for i in range(1, len(arr)):
        result = _lcm(result, arr[i])
    return result

class Solution:
    def maxFactorScore(self, nums: list[int]) -> int:
        n = len(nums)
        max_score = 0

        # Case 1: No element removed
        if n > 0:
            current_gcd = calculate_gcd_of_list(nums)
            current_lcm = calculate_lcm_of_list(nums)
            max_score = max(max_score, current_gcd * current_lcm)
        else: # Empty array, score is 0.
            return 0

        # Case 2: Remove one element
        for i in range(n):
            temp_nums = nums[:i] + nums[i+1:]
            
            # If removing the only element, array becomes empty.
            # calculate_gcd_of_list and calculate_lcm_of_list will return 0 for empty list,
            # resulting in a factor score of 0, which is correct for an empty array.
            current_gcd = calculate_gcd_of_list(temp_nums)
            current_lcm = calculate_lcm_of_list(temp_nums)
            max_score = max(max_score, current_gcd * current_lcm)

        return max_score