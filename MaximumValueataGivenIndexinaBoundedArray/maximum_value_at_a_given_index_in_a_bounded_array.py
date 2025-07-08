class Solution:
    def get_sum_for_side(self, peak_val: int, num_elements_on_side: int) -> int:
        if num_elements_on_side == 0:
            return 0

        # Case 1: The sequence decreases strictly down to a positive number,
        # without hitting 1 for all `num_elements_on_side` terms.
        # The elements would be: peak_val-1, peak_val-2, ..., peak_val - num_elements_on_side
        # This occurs if (peak_val - 1) is greater than or equal to num_elements_on_side.
        if peak_val - 1 >= num_elements_on_side:
            first_term = peak_val - 1
            last_term = peak_val - num_elements_on_side
            # Sum of an arithmetic series: count * (first_term + last_term) / 2
            return num_elements_on_side * (first_term + last_term) // 2
        else:
            # Case 2: The sequence decreases to 1 and then continues with 1s.
            # The decreasing part is from (peak_val-1) down to 1.
            # Number of terms in this decreasing part is (peak_val-1).
            # Sum of 1 to (peak_val-1) is (peak_val-1) * peak_val / 2.
            sum_decreasing_part = (peak_val - 1) * peak_val // 2
            
            # The remaining terms must be 1.
            # Number of remaining terms = num_elements_on_side - (peak_val - 1)
            num_ones = num_elements_on_side - (peak_val - 1)
            return sum_decreasing_part + num_ones

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left_len = index
        right_len = n - 1 - index

        low = 1
        high = maxSum # The maximum possible value for nums[index] is maxSum itself (e.g., if n=1)
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2 # This `mid` is our candidate value for nums[index]
            
            current_sum = mid # Start with the value at nums[index]
            
            # Add the minimum possible sum for elements to the left of index
            current_sum += self.get_sum_for_side(mid, left_len)
            
            # Add the minimum possible sum for elements to the right of index
            current_sum += self.get_sum_for_side(mid, right_len)
            
            if current_sum <= maxSum:
                # If current_sum is within maxSum, this `mid` is a possible answer.
                # Try to find a larger `mid` in the upper half.
                ans = mid
                low = mid + 1
            else:
                # If current_sum exceeds maxSum, `mid` is too large.
                # Try a smaller `mid` in the lower half.
                high = mid - 1
                
        return ans