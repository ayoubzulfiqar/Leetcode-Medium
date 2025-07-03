import itertools

class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        max_minutes = -1
        
        for p in itertools.permutations(arr):
            h1, h2, m1, m2 = p[0], p[1], p[2], p[3]
            
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2
            
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                current_total_minutes = hours * 60 + minutes
                if current_total_minutes > max_minutes:
                    max_minutes = current_total_minutes
                    
        if max_minutes == -1:
            return ""
        else:
            final_hours = max_minutes // 60
            final_minutes = max_minutes % 60
            return f"{final_hours:02d}:{final_minutes:02d}"