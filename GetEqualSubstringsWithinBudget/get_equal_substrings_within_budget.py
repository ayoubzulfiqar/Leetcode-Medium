class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        
        costs = [0] * n
        for i in range(n):
            costs[i] = abs(ord(s[i]) - ord(t[i]))
        
        left = 0
        current_cost = 0
        max_length = 0
        
        for right in range(n):
            current_cost += costs[right]
            
            while current_cost > maxCost:
                current_cost -= costs[left]
                left += 1
            
            max_length = max(max_length, right - left + 1)
            
        return max_length