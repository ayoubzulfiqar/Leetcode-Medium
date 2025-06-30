class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        results = []

        for i in range(n - 3):
            # Skip duplicate for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Optimization 1: If the sum of the current element and the three largest elements is less than target,
            # then nums[i] is too small to form a sum equal to target with any combination.
            # Continue to the next i.
            # This check is important to avoid unnecessary iterations when nums[i] is very small.
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue

            # Optimization 2: If the sum of the current element and the next three elements is greater than target,
            # then any subsequent quadruplets starting with nums[i] will also be greater than target.
            # So, we can break the outer loop.
            # This check is important to avoid unnecessary iterations when nums[i] is very large.
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break

            for j in range(i + 1, n - 2):
                # Skip duplicate for j
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                # Optimization 3: If the sum of nums[i], nums[j] and the two largest elements is less than target,
                # then nums[j] is too small to form a sum equal to target with nums[i].
                # Continue to the next j.
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue

                # Optimization 4: If the sum of nums[i], nums[j] and the next two elements is greater than target,
                # then any subsequent quadruplets starting with nums[i], nums[j] will also be greater than target.
                # So, we can break this inner loop.
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break

                left = j + 1
                right = n - 1
                current_target_for_two_sum = target - nums[i] - nums[j]

                while left < right:
                    current_sum_of_two = nums[left] + nums[right]

                    if current_sum_of_two == current_target_for_two_sum:
                        results.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for left pointer
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        # Skip duplicates for right pointer
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        
                        # Move both pointers to find next distinct pair
                        left += 1
                        right -= 1
                    elif current_sum_of_two < current_target_for_two_sum:
                        left += 1
                    else: # current_sum_of_two > current_target_for_two_sum
                        right -= 1
        
        return results