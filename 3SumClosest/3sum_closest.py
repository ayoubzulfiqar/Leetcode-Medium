class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        closest_sum = nums[0] + nums[1] + nums[2]
        min_diff = abs(closest_sum - target)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)

                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum
                
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum