class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        beautiful_count = 0

        for i in range(n):
            current_vowels = 0
            current_consonants = 0
            for j in range(i, n):
                if s[j] in vowels_set:
                    current_vowels += 1
                else:
                    current_consonants += 1

                if current_vowels == current_consonants:
                    if (current_vowels * current_consonants) % k == 0:
                        beautiful_count += 1
        
        return beautiful_count