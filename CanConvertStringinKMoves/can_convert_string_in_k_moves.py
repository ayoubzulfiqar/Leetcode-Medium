class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        required_shifts_counts = [0] * 26

        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            
            shift_needed = (ord(t[i]) - ord(s[i]) + 26) % 26
            
            required_shifts_counts[shift_needed] += 1
        
        for d in range(1, 26):
            count_for_this_d = required_shifts_counts[d]
            
            if count_for_this_d > 0:
                max_move_required_for_this_d = d + (count_for_this_d - 1) * 26
                
                if max_move_required_for_this_d > k:
                    return False
        
        return True