class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        
        def calculate_sum_for_divisor(divisor: int) -> int:
            current_sum = 0
            for num in nums:
                # Ceiling division: (a + b - 1) // b for positive integers a, b
                current_sum += (num + divisor - 1) // divisor
            return current_sum

        # The search space for the divisor is from 1 to max(nums).
        # A divisor of 1 will give the largest sum (sum(nums)).
        # A divisor of max(nums) (or any number >= max(nums)) will give the smallest sum (len(nums)).
        # Since the problem guarantees an answer and nums.length <= threshold,
        # max(nums) is always a valid upper bound for the search space and a potential answer.
        left = 1
        right = max(nums) 
        
        # 'ans' will store the smallest divisor found so far that satisfies the condition.
        # Initialize it with the largest possible value in the search space.
        ans = right 

        while left <= right:
            mid = left + (right - left) // 2
            
            # Calculate the sum of divisions using 'mid' as the divisor
            current_sum_with_mid = calculate_sum_for_divisor(mid)
            
            if current_sum_with_mid <= threshold:
                # If the sum is less than or equal to the threshold, 'mid' is a possible answer.
                # We want the *smallest* such divisor, so we record 'mid' and try to find a smaller one
                # in the left half of the search space.
                ans = mid
                right = mid - 1
            else:
                # If the sum is greater than the threshold, 'mid' is too small (it results in too large a sum).
                # We need a larger divisor to reduce the sum, so we search in the right half.
                left = mid + 1
                
        return ans