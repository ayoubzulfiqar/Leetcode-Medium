import collections

class Solution:
    def identifyLargestOutlier(self, nums: list[int]) -> int:
        n = len(nums)
        
        total_sum = sum(nums)
        
        counts = collections.Counter(nums)
        
        max_outlier = -float('inf')
        
        for potential_outlier in nums:
            # The problem can be modeled by the equation:
            # total_sum_of_all_elements = sum_of_special_numbers + sum_element + outlier
            # Since sum_element is equal to sum_of_special_numbers:
            # total_sum_of_all_elements = 2 * sum_element + outlier
            #
            # We are iterating through each 'potential_outlier' from 'nums'.
            # We need to find the 'required_sum_element_val' that satisfies the equation.
            # 2 * required_sum_element_val = total_sum_of_all_elements - potential_outlier
            # required_sum_element_val = (total_sum_of_all_elements - potential_outlier) / 2
            
            numerator = total_sum - potential_outlier
            
            # The 'required_sum_element_val' must be an integer.
            # This means 'numerator' must be an even number.
            if numerator % 2 != 0:
                continue
            
            required_sum_element_val = numerator // 2
            
            # Check if the calculated 'required_sum_element_val' exists in the original array 'nums'.
            if required_sum_element_val not in counts:
                continue
            
            # Ensure that the 'potential_outlier' and 'required_sum_element_val'
            # can be selected from distinct indices in the original array.
            # This is crucial because they represent two distinct elements (outlier and sum_element).
            
            if potential_outlier == required_sum_element_val:
                # If the value of the potential outlier is the same as the required sum element value,
                # we need at least two occurrences of this value in 'nums'
                # to pick one as the outlier and one as the sum element.
                if counts[potential_outlier] >= 2:
                    max_outlier = max(max_outlier,