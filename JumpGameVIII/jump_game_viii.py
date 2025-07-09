from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        
        q = deque([0]) 
        
        for i in range(1, n):
            while q and q[0] < i - maxJump:
                q.popleft()
            
            if s[i] == '0' and q and q[0] <= i - minJump:
                dp[i] = True
                q.append(i)
        
        return dp[n - 1]