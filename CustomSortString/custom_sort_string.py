import collections

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counts = collections.Counter(s)
        result_chars = []

        for char_in_order in order:
            if char_in_order in s_counts:
                result_chars.append(char_in_order * s_counts[char_in_order])
                del s_counts[char_in_order]

        for remaining_char, count in s_counts.items():
            result_chars.append(remaining_char * count)

        return "".join(result_chars)