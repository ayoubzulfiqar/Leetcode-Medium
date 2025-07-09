class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_ptr = 0
        t_ptr = 0
        
        len_s = len(s)
        len_t = len(t)
        
        while s_ptr < len_s and t_ptr < len_t:
            if s[s_ptr] == t[t_ptr]:
                t_ptr += 1
            s_ptr += 1
            
        return len_t - t_ptr