class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len = len(s)
        p_len = len(p)

        if s_len < p_len:
            return []

        p_counts = [0] * 26
        window_counts = [0] * 26

        # Populate counts for string p
        for char_p in p:
            p_counts[ord(char_p) - ord('a')] += 1

        # Populate counts for the initial window in s
        for i in range(p_len):
            window_counts[ord(s[i]) - ord('a')] += 1

        results = []

        # Check the initial window
        if p_counts == window_counts:
            results.append(0)

        # Slide the window across s
        for i in range(p_len, s_len):
            # Remove the character leaving the window from the left
            window_counts[ord(s[i - p_len]) - ord('a')] -= 1
            # Add the character entering the window from the right
            window_counts[ord(s[i]) - ord('a')] += 1

            # If the current window's character counts match p's counts,
            # it's an anagram. Add its starting index to results.
            if p_counts == window_counts:
                results.append(i - p_len + 1) # Current window's start index

        return results