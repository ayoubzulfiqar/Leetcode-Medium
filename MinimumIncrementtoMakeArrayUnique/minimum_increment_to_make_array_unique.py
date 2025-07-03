class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        
        moves = 0
        
        # expected_val tracks the smallest value the current number (nums[i])
        # should take to ensure uniqueness, given that nums[0] through nums[i-1]
        # have already been made unique and minimal.
        # For the first element (nums[0]), it takes its own value.
        # Thus, the next element (nums[1]) must be at least nums[0] + 1.
        expected_val = nums[0] + 1 
        
        # Iterate from the second element of the sorted array
        for i in range(1, len(nums)):
            val = nums[i]
            
            if val < expected_val:
                # If the current value is less than the expected minimum,
                # we must increment it to expected_val.
                moves += expected_val - val
                
                # After incrementing nums[i] to expected_val, the next number
                # must be at least expected_val + 1.
                expected_val += 1
            else:
                # If the current value is already greater than or equal to
                # the expected minimum, it's already unique relative to the
                # previous elements. No moves needed for this element.
                # The next number must be at least val + 1.
                expected_val = val + 1
                
        return moves