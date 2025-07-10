class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        n = len(words)
        prefix_vowel_counts = [0] * (n + 1)
        
        for i in range(n):
            word = words[i]
            is_vowel_word = 0
            if word[0] in vowels and word[-1] in vowels:
                is_vowel_word = 1
            
            prefix_vowel_counts[i+1] = prefix_vowel_counts[i] + is_vowel_word
            
        ans = []
        for li, ri in queries:
            count = prefix_vowel_counts[ri + 1] - prefix_vowel_counts[li]
            ans.append(count)
            
        return ans