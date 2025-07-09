class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        
        min_char_suffix = [''] * n
        min_char_suffix[n - 1] = s[n - 1]
        for i in range(n - 2, -1, -1):
            min_char_suffix[i] = min(s[i], min_char_suffix[i + 1])
            
        p = []
        t = []
        
        s_ptr = 0
        
        while s_ptr < n or t:
            if not t:
                t.append(s[s_ptr])
                s_ptr += 1
            else:
                if s_ptr == n:
                    p.append(t.pop())
                else:
                    if t[-1] <= min_char_suffix[s_ptr]:
                        p.append(t.pop())
                    else:
                        t.append(s[s_ptr])
                        s_ptr += 1
                        
        return "".join(p)