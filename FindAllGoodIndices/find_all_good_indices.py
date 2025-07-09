class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        
        left_non_inc = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                left_non_inc[i] = left_non_inc[i - 1] + 1
            else:
                left_non_inc[i] = 1

        right_non_dec = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right_non_dec[i] = right_non_dec[i + 1] + 1
            else:
                right_non_dec[i] = 1
        
        good_indices = []
        for i in range(k, n - k):
            if left_non_inc[i - 1] >= k and right_non_dec[i + 1] >= k:
                good_indices.append(i)
                
        return good_indices