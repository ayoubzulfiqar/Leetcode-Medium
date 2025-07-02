class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        
        def is_subsequence(word: str, s: str) -> bool:
            i = 0  # pointer for word
            j = 0  # pointer for s
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return i == len(word)

        longest_word = ""

        for word in dictionary:
            if is_subsequence(word, s):
                if len(word) > len(longest_word):
                    longest_word = word
                elif len(word) == len(longest_word):
                    if word < longest_word:
                        longest_word = word
        
        return longest_word