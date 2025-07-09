class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            points_i = questions[i][0]
            brainpower_i = questions[i][1]
            
            skip_points = dp[i + 1]
            
            solve_next_q_index = i + brainpower_i + 1
            
            solve_points = points_i
            if solve_next_q_index <= n:
                solve_points += dp[solve_next_q_index]
            
            dp[i] = max(skip_points, solve_points)
            
        return dp[0]