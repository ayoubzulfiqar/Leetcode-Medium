class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        current_substring_chars = set()

        if not s:
            return 0

        count = 1

        for char in s:
            if char in current_substring_chars:
                count += 1
                current_substring_chars.clear()
                current_substring_chars.add(char)
            else:
                current_substring_chars.add(char)
        
        return count