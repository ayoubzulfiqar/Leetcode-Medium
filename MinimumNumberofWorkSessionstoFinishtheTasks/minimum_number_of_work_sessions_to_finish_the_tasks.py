import math

class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        n = len(tasks)
        
        dp = [(math.inf, -1)] * (1 << n)
        
        dp[0] = (1, sessionTime)
        
        for mask in range(1 << n):
            if dp[mask][0] == math.inf:
                continue
            
            current_sessions, current_remaining_time = dp[mask]
            
            for i in range(n):
                if not (mask & (1 << i)):
                    task_time = tasks[i]
                    next_mask = mask | (1 << i)
                    
                    new_sessions = current_sessions
                    new_remaining_time = current_remaining_time
                    
                    if new_remaining_time >= task_time:
                        new_remaining_time -= task_time
                    else:
                        new_sessions += 1
                        new_remaining_time = sessionTime - task_time
                    
                    if new_sessions < dp[next_mask][0]:
                        dp[next_mask] = (new_sessions, new_remaining_time)
                    elif new_sessions == dp[next_mask][0] and new_remaining_time > dp[next_mask][1]:
                        dp[next_mask] = (new_sessions, new_remaining_time)
                        
        return dp[(1 << n) - 1][0]