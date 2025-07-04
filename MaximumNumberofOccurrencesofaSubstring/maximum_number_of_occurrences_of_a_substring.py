import collections

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # According to the problem constraints and common insights for this problem type,
        # we only need to consider substrings of length minSize.
        # If a longer substring (up to maxSize) satisfies the conditions,
        # its prefix of length minSize will also satisfy the maxLetters condition
        # and will occur at least as many times. Therefore, the maximum frequency
        # will always be found among substrings of length minSize.

        n = len(s)
        if n < minSize:
            return 0

        char_counts = collections.defaultdict(int)
        unique_count = 0
        substring_counts = collections.defaultdict(int)
        max_occurrences = 0

        # Initialize the first window of size minSize
        for i in range(minSize):
            char_counts[s[i]] += 1
            if char_counts[s[i]] == 1:
                unique_count += 1

        if unique_count <= maxLetters:
            current_substring = s[0:minSize]
            substring_counts[current_substring] += 1
            max_occurrences = max(max_occurrences, substring_counts[current_substring])

        # Slide the window
        for i in range(minSize, n):
            # Remove character leaving the window from the left
            char_to_remove = s[i - minSize]
            char_counts[char_to_remove] -= 1
            if char_counts[char_to_remove] == 0:
                unique_count -= 1

            # Add character entering the window from the right
            char_to_add = s[i]
            char_counts[char_to_add] += 1
            if char_counts[char_to_add] == 1:
                unique_count += 1

            # Check the current window (substring of length minSize)
            if unique_count <= maxLetters:
                current_substring = s[i - minSize + 1 : i + 1]
                substring_counts[current_substring] += 1
                max_occurrences = max(max_occurrences, substring_counts[current_substring])

        return max_occurrences