class Solution:
    def evenProductSubarrays(self, nums: list[int]) -> int:
        total_even_product_subarrays = 0
        # This variable tracks the count of subarrays ending at the *current* index
        # that have an even product.
        # If the current number is odd, this count is simply inherited from the previous index.
        # If the current number is even, all subarrays ending at the current index will have an even product.
        current_subarrays_with_even_product_ending_here = 0
        
        for i, num in enumerate(nums):
            if num % 2 == 0:  # If the current number is even
                # Any subarray ending at 'i' will have an even product because 'num' is even.
                # The number of such subarrays is (i + 1), which are:
                # nums[0...i], nums[1...i], ..., nums[i...i]
                current_subarrays_with_even_product_ending_here = i + 1
            else:  # If the current number is odd
                # A subarray ending at 'i' (nums[j...i]) will have an even product
                # ONLY IF the subarray nums[j...i-1] had an even product.
                # The count of such subarrays is therefore the same as the count
                # of even-product subarrays ending at the previous index (i-1).
                # So, current_subarrays_with_even_product_ending_here retains its value
                # from the previous iteration.
                pass 
            
            # Add the count of even-product subarrays ending at the current index 'i'
            # to the total count.
            total_even_product_subarrays += current_subarrays_with_even_product_ending_here
            
        return total_even_product_subarrays