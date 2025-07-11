class Solution:
    def minPatches(self, coins: list[int], target: int) -> int:
        coins.sort()
        
        added_coins_count = 0
        current_reachable_sum = 0
        
        i = 0
        n = len(coins)
        
        while current_reachable_sum < target:
            if i < n and coins[i] <= current_reachable_sum + 1:
                current_reachable_sum += coins[i]
                i += 1
            else:
                added_coins_count += 1
                current_reachable_sum += (current_reachable_sum + 1)
                
        return added_coins_count