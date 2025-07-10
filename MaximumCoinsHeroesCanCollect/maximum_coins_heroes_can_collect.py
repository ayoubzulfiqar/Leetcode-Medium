class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        my_coins = 0
        n = len(piles)
        
        num_triplets = n // 3
        
        current_right_idx = n - 1
        for _ in range(num_triplets):
            my_coins += piles[current_right_idx - 1]
            current_right_idx -= 2
            
        return my_coins