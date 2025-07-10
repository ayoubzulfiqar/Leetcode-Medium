class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        n = len(skill)
        
        total_skill_sum = sum(skill)
        num_teams = n // 2
        
        if total_skill_sum % num_teams != 0:
            return -1
        
        target_team_skill_sum = total_skill_sum // num_teams
        
        skill.sort()
        
        total_chemistry = 0
        left = 0
        right = n - 1
        
        while left < right:
            player1_skill = skill[left]
            player2_skill = skill[right]
            
            if player1_skill + player2_skill == target_team_skill_sum:
                total_chemistry += (player1_skill * player2_skill)
                left += 1
                right -= 1
            else:
                return -1
                
        return total_chemistry