class Solution:
    def totalCharacters(self, s: str, t: int) -> int:
        MOD = 10**9 + 7

        counts = [0] * 26
        for char_code in s:
            counts[ord(char_code) - ord('a')] += 1

        L = len(s)

        for _ in range(t):
            num_z = counts[25]

            L = (L + num_z) % MOD

            new_counts = [0] * 26

            for i in range(25):
                new_counts[i+1] = (new_counts[i+1] + counts[i]) % MOD

            new_counts[0] = (new_counts[0] + num_z) % MOD
            new_counts[1] = (new_counts[1] + num_z) % MOD

            counts = new_counts
        
        return L