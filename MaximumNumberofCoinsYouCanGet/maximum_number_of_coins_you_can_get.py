class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        n = len(piles)
        my_coins = 0
        left = 0
        right = n - 1

        while left < right:
            my_coins += piles[right - 1]
            right -= 2
            left += 1
        
        return my_coins