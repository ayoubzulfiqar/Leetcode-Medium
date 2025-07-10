class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        char_values = {}
        for i in range(len(chars)):
            char_values[chars[i]] = vals[i]

        for i in range(26):
            char = chr(ord('a') + i)
            if char not in char_values:
                char_values[char] = i + 1

        max_so_far = 0
        current_max = 0

        for char_s in s:
            value = char_values[char_s]
            current_max = max(value, current_max + value)
            max_so_far = max(max_so_far, current_max)

        return max_so_far