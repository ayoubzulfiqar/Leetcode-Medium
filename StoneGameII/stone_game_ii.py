import functools

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = piles[i] + suffix_sums[i + 1]

        @functools.lru_cache(None)
        def dp(i: int, m: int) -> int:
            if i == n:
                return 0
            
            max_stones_current_player = -1

            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                
                score_for_this_x = suffix_sums[i] - dp(i + x, max(m, x))
                max_stones_current_player = max(max_stones_current_player, score_for_this_x)
            
            return max_stones_current_player

        return dp(0, 1)