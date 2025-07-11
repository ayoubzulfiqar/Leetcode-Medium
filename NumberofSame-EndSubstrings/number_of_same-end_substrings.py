import collections

def count_same_end_substrings(s: str) -> int:
    total_same_end_substrings = 0
    char_frequencies = collections.defaultdict(int)
    for char in s:
        total_same_end_substrings += 1
        total_same_end_substrings += char_frequencies[char]
        char_frequencies[char] += 1
    return total_same_end_substrings