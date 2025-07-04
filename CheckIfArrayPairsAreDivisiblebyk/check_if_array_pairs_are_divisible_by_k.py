class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        freq = [0] * k

        for num in arr:
            remainder = num % k
            freq[remainder] += 1

        if freq[0] % 2 != 0:
            return False

        if k % 2 == 0:
            if freq[k // 2] % 2 != 0:
                return False

        for r in range(1, k // 2):
            if freq[r] != freq[k - r]:
                return False

        return True