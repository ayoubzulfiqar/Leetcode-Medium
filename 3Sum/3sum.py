class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Optimization: If nums[i] is already positive,
            # the sum cannot be 0 with sorted non-decreasing numbers.
            # This also handles cases where all remaining numbers are positive.
            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second element (left pointer)
                    # Move left pointer past any duplicates of the current nums[left]
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    # Skip duplicate values for the third element (right pointer)
                    # Move right pointer past any duplicates of the current nums[right]
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    # Move both pointers to find next distinct pair
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    # Sum is too small, need a larger number from the left side
                    left += 1
                else: # current_sum > 0
                    # Sum is too large, need a smaller number from the right side
                    right -= 1
        
        return result