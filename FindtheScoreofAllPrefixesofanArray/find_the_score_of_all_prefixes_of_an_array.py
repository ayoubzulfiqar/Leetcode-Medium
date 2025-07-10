class Solution:
    def findThePrefixScores(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        current_max = 0
        current_score_sum = 0

        for i in range(n):
            current_max = max(current_max, nums[i])
            conversion_value = nums[i] + current_max
            current_score_sum += conversion_value
            ans.append(current_score_sum)

        return ans