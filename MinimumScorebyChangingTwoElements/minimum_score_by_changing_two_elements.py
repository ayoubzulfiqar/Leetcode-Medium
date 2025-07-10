class Solution:
    def minScore(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        # Scenario 1: Change the two smallest elements (nums[0] and nums[1])
        # The new minimum will be nums[2], and the maximum will be nums[n-1].
        # The range is nums[n-1] - nums[2].
        # We can change nums[0] and nums[1] to nums[2] to make min_abs_diff = 0.
        score_option1 = nums[n-1] - nums[2]

        # Scenario 2: Change the two largest elements (nums[n-1] and nums[n-2])
        # The new minimum will be nums[0], and the maximum will be nums[n-3].
        # The range is nums[n-3] - nums[0].
        # We can change nums[n-1] and nums[n-2] to nums[n-3] to make min_abs_diff = 0.
        score_option2 = nums[n-3] - nums[0]

        # Scenario 3: Change one smallest (nums[0]) and one largest (nums[n-1]) element
        # The new minimum will be nums[1], and the maximum will be nums[n-2].
        # The range is nums[n-2] - nums[1].
        # We can change nums[0] to nums[1] and nums[n-1] to nums[1] (or nums[n-2])
        # to make min_abs_diff = 0.
        score_option3 = nums[n-2] - nums[1]

        return min(score_option1, score_option2, score_option3)