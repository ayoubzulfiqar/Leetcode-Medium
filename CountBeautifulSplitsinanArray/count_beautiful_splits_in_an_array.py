class Solution:
    def countBeautifulSplits(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        P1, M1 = 53, 1_000_000_007
        P2, M2 = 31, 1_000_000_009 

        prefix_hashes1 = [0] * (n + 1)
        powers_P1 = [1] * (n + 1)
        for k in range(n):
            prefix_hashes1[k+1]