class Solution:
    def maxUniqueSplits(self, s: str) -> int:
        self.max_splits = 0

        def backtrack(start_index, current_unique_substrings):
            if start_index == len(s):
                self.max_splits = max(self.max_splits, len(current_unique_substrings))
                return

            for end_index in range(start_index, len(s)):
                substring = s[start_index : end_index + 1]

                if substring not in current_unique_substrings:
                    current_unique_substrings.add(substring)
                    backtrack(end_index + 1, current_unique_substrings)
                    current_unique_substrings.remove(substring)

        backtrack(0, set())
        
        return self.max_splits