class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # length[i] stores the length of the longest increasing subsequence ending at index i
        length = [1] * n
        # count[i] stores the number of longest increasing subsequences ending at index i
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # If we found a longer LIS ending at i
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    # If we found another LIS of the same maximum length ending at i
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = 0
        if n > 0:
            max_len = max(length)
        
        result = 0
        for i in range(n):
            if length[i] == max_len:
                result += count[i]
        
        return result