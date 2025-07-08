class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        coins.sort()
        
        reachable_max = 0
        
        for coin in coins:
            if coin > reachable_max + 1:
                break
            
            reachable_max += coin
            
        return reachable_max + 1