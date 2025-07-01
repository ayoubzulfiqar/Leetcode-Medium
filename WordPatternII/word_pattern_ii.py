class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        char_map = {}
        used_substrings = set()

        return self._backtrack(pattern, s, 0, 0, char_map, used_substrings)

    def _backtrack(self, pattern: str, s: str, p_idx: int, s_idx: int, char_map: dict, used_substrings: set) -> bool:
        if p_idx == len(pattern) and s_idx == len(s):
            return True
        
        if p_idx == len(pattern):
            return False
        if s_idx == len(s):
            return False

        current_char = pattern[p_idx]

        if current_char in char_map:
            mapped_substring = char_map[current_char]
            if s_idx + len(mapped_substring) <= len(s) and \
               s[s_idx : s_idx + len(mapped_substring)] == mapped_substring:
                return self._backtrack(pattern, s, p_idx + 1, s_idx + len(mapped_substring), char_map, used_substrings)
            else:
                return False
        
        for i in range(s_idx, len(s)):
            current_substring = s[s_idx : i + 1]

            if current_substring in used_substrings:
                continue

            char_map[current_char] = current_substring
            used_substrings.add(current_substring)

            if self._backtrack(pattern, s, p_idx + 1, i + 1, char_map, used_substrings):
                return True

            del char_map[current_char]
            used_substrings.remove(current_substring)
        
        return False