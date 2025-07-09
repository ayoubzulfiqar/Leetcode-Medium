import collections

class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        counts = collections.Counter(words)
        length = 0
        has_center = False

        for word in list(counts.keys()):
            if counts[word] == 0:
                continue

            if word[0] == word[1]:  # Symmetric word, e.g., "gg"
                length += (counts[word] // 2) * 4
                if counts[word] % 2 == 1:
                    has_center = True
                counts[word] = 0 
            else:  # Asymmetric word, e.g., "lc"
                rev_word = word[1] + word[0]
                if rev_word in counts and counts[rev_word] > 0:
                    num_pairs = min(counts[word], counts[rev_word])
                    length += num_pairs * 4
                    counts[word] -= num_pairs
                    counts[rev_word] -= num_pairs
        
        if has_center:
            length += 2
            
        return length