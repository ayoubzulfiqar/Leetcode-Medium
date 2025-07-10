class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)

        s1_even_chars = []
        s1_odd_chars = []
        s2_even_chars = []
        s2_odd_chars = []

        for i in range(n):
            if i % 2 == 0:  # Even index
                s1_even_chars.append(s1[i])
                s2_even_chars.append(s2[i])
            else:  # Odd index
                s1_odd_chars.append(s1[i])
                s2_odd_chars.append(s2[i])
        
        s1_even_chars.sort()
        s1_odd_chars.sort()
        s2_even_chars.sort()
        s2_odd_chars.sort()

        return s1_even_chars == s2_even_chars and s1_odd_chars == s2_odd_chars