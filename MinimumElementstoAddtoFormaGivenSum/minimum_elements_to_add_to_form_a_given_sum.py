class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        current_sum = sum(nums)
        
        diff = goal - current_sum
        
        needed_sum_abs = abs(diff)
        
        # To minimize the number of elements, each added element should contribute
        # the maximum possible absolute value, which is 'limit'.
        # We use ceiling division to find how many 'limit'-sized chunks are needed
        # to cover 'needed_sum_abs'.
        # ceil(a / b) for non-negative a and positive b can be calculated as (a + b - 1) // b.
        return (needed_sum_abs + limit - 1) // limit