class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                char_code = ord(s[j]) - ord('a')
                freq[char_code] += 1

                max_f = 0
                min_f = float('inf')

                for k in range(26):
                    if freq[k] > 0:
                        max_f = max(max_f, freq[k])
                        min_f = min(min_f, freq[k])
                
                total_beauty += (max_f - min_f)
        
        return total_beauty