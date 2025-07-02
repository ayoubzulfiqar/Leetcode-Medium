class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        max_dist = 0
        
        # Initialize min_so_far and max_so_far with the values from the first array.
        # These variables will track the overall minimum and maximum values encountered
        # from arrays processed *before* the current one.
        min_so_far = arrays[0][0]
        max_so_far = arrays[0][-1]
        
        # Iterate through the arrays starting from the second array (index 1).
        # This ensures that when we calculate the distance, the 'current_array'
        # is always distinct from the arrays that contributed to 'min_so_far'
        # and 'max_so_far'.
        for i in range(1, len(arrays)):
            current_array = arrays[i]
            current_min = current_array[0]
            current_max = current_array[-1]
            
            # Calculate potential maximum distances:
            # 1. The absolute difference between the current array's minimum value
            #    and the maximum value seen so far from previous arrays.
            # 2. The absolute difference between the current array's maximum value
            #    and the minimum value seen so far from previous arrays.
            # Update 'max_dist' with the largest of these possibilities.
            max_dist = max(max_dist, abs(current_min - max_so_far))
            max_dist = max(max_dist, abs(current_max - min_so_far))
            
            # Update 'min_so_far' and 'max_so_far' to include the current array's
            # extreme values. These updated values will be used when considering
            # subsequent arrays.
            min_so_far = min(min_so_far, current_min)
            max_so_far = max(max_so_far, current_max)
            
        return max_dist