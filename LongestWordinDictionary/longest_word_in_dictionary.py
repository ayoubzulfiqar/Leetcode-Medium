class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()
        
        words_set = set(words)
        
        best_word = ""
        
        for word in words:
            is_buildable = True
            # Check if all prefixes (from length 1 up to len(word)-1) exist in the dictionary
            for i in range(1, len(word)):
                prefix = word[:i]
                if prefix not in words_set:
                    is_buildable = False
                    break
            
            if is_buildable:
                # If the current word is longer than the best_word found so far, update it.
                # If it's the same length, because we sorted `words` lexicographically,
                # the `best_word` would have been set by an earlier (lexicographically smaller) word,
                # so we don't need to update in that case.
                if len(word) > len(best_word):
                    best_word = word
        
        return best_word