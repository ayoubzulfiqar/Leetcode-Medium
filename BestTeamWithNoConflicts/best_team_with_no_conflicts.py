class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        n = len(scores)
        
        players = []
        for i in range(n):
            players.append((ages[i], scores[i]))
        
        players.sort() 
        
        dp = [0] * n
        
        max_overall_score = 0
        
        for i in range(n):
            current_age, current_score = players[i]
            
            dp[i] = current_score 
            
            for j in range(i):
                prev_age, prev_score = players[j]
                
                if prev_score <= current_score:
                    dp[i] = max(dp[i], current_score + dp[j])
            
            max_overall_score = max(max_overall_score, dp[i])
            
        return max_overall_score