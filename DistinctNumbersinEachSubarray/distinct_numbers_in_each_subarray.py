import collections

class Solution:
    def distinctNumbers(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        if k == 0 or k > n:
            return []

        counts = collections.Counter()
        result = []

        # Initialize the first window
        for i in range(k):
            counts[nums[i]] += 1
        
        # Add the distinct count for the first window
        result.append(len(counts))

        # Slide the window
        for i in range(k, n):
            # Remove the element leaving the window
            left_element = nums[i - k]
            counts[left_element] -= 1
            if counts[left_element] == 0:
                del counts[left_element]
            
            # Add the element entering the window
            right_element = nums[i]
            counts[right_element] += 1
            
            # Add the distinct count for the current window
            result.append(len(counts))
            
        return result