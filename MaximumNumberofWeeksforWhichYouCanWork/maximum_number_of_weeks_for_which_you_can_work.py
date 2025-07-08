class Solution:
    def numberOfWeeks(self, milestones: list[int]) -> int:
        max_milestones = 0
        total_milestones = 0
        for m in milestones:
            if m > max_milestones:
                max_milestones = m
            total_milestones += m
        
        other_milestones_sum = total_milestones - max_milestones
        
        if max_milestones - 1 <= other_milestones_sum:
            return total_milestones
        else:
            return 2 * other_milestones_sum + 1