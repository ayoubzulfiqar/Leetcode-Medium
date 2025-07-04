class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        count = 0
        n = len(s)
        m = len(t)

        for i in range(n):
            for j in range(m):
                diff = 0
                # Iterate through possible lengths of substrings
                # k represents the offset from the starting characters s[i] and t[j]
                # The length of the current substring being compared is (k + 1)
                for k in range(min(n - i, m - j)):
                    if s[i + k] != t[j + k]:
                        diff += 1
                    
                    # If exactly one character differs, increment the total count
                    if diff == 1:
                        count += 1
                    # If more than one character differs,
                    # any longer substring starting from s[i] and t[j]
                    # will also have more than one difference.
                    # So, we can stop extending this pair.
                    elif diff > 1:
                        break
        return count