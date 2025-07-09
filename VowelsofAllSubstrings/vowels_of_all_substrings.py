class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        total_vowels_sum = 0

        for i in range(n):
            if word[i] in vowels:
                total_vowels_sum += (i + 1) * (n - i)
        
        return total_vowels_sum