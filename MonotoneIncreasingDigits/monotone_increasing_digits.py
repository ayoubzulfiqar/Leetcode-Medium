class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        n_len = len(s)
        
        mark = n_len
        
        for i in range(n_len - 2, -1, -1):
            if int(s[i]) > int(s[i+1]):
                s[i] = str(int(s[i]) - 1)
                mark = i + 1
        
        for j in range(mark, n_len):
            s[j] = '9'
            
        return int("".join(s))