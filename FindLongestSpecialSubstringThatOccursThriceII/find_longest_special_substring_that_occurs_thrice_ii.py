import collections

class Solution:
    def longestSpecialSubstring(self, s: str) -> int:
        char_top_lengths = collections.defaultdict(lambda: [0, 0, 0])

        n = len(s)
        if n == 0:
            return -1

        current_char = s[0]
        current_length = 0

        for i in range(n):
            if s[i] == current_char:
                current_length += 1
            else:
                lengths = char_top_lengths[current_char]
                if current_length > lengths[0]:
                    lengths[2] = lengths[1]
                    lengths[1] = lengths[0]
                    lengths[0] = current_length
                elif current_length > lengths[1]:
                    lengths[2] = lengths[1]
                    lengths[1] = current_length
                elif current_length