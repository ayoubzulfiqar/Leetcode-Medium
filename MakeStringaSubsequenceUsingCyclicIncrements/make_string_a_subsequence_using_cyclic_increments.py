class Solution:
    def canBeSubsequence(self, str1: str, str2: str) -> bool:
        p1 = 0
        p2 = 0

        len1 = len(str1)
        len2 = len(str2)

        while p1 < len1 and p2 < len2:
            char1 = str1[p1]
            char2 = str2[p2]

            incremented_char1_code = (ord(char1) - ord('a') + 1) % 26 + ord('a')
            incremented_char1 = chr(incremented_char1_code)

            if char1 == char2 or incremented_char1 == char2:
                p2 += 1
            
            p1 += 1

        return p2 == len2