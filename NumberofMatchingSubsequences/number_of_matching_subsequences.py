import collections

class Solution:
    def numMatchingSubsequences(self, s: str, words: list[str]) -> int:
        waiting_words = collections.defaultdict(list)
        for word in words:
            waiting_words[word[0]].append((word, 0))

        count = 0
        for char_s in s:
            words_to_process = waiting_words[char_s]
            waiting_words[char_s] = [] 
            
            for word, index in words_to_process:
                index += 1
                if index == len(word):
                    count += 1
                else:
                    next_char = word[index]
                    waiting_words[next_char].append((word, index))
        
        return count