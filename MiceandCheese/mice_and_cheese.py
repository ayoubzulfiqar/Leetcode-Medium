class Solution:
    def miceAndCheese(self, reward1: list[int], reward2: list[int], k: int) -> int:
        n = len(reward1)
        
        total_points = sum(reward2)
        
        differences = [reward1[i] - reward2[i] for i in range(n)]
            
        differences.sort(reverse=True)
        
        for i in range(k):
            total_points += differences[i]
            
        return total_points