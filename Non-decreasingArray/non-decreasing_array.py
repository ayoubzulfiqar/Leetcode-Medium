class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        n = len(nums)
        violations = 0

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                violations += 1
                if violations > 1:
                    return False

                # This is the first violation. Decide which element to modify.
                # Option 1: Decrease nums[i] to nums[i+1]
                # This is preferred as it keeps numbers smaller, making it easier for subsequent elements to be non-decreasing.
                # This is valid if i == 0 (no element before nums[i])
                # OR if nums[i-1] <= nums[i+1] (modifying nums[i] won't break the previous non-decreasing property)
                if i == 0 or nums[i + 1] >= nums[i - 1]:
                    nums[i] = nums[i + 1]
                # Option 2: Increase nums[i+1] to nums[i]
                # This must be chosen if Option 1 is not viable (i.e., nums[i-1] > nums[i+1])
                # Modifying nums[i] would make nums[i-1] > new_nums[i], creating a new violation.
                else:
                    nums[i + 1] = nums[i]
        
        return True