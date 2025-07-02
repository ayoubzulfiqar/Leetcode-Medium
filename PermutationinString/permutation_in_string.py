class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_counts = [0] * 26
        window_counts = [0] * 26

        for i in range(len_s1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_counts[i] == window_counts[i]:
                matches += 1

        if matches == 26:
            return True

        for i in range(len_s1, len_s2):
            char_in_idx = ord(s2[i]) - ord('a')
            char_out_idx = ord(s2[i - len_s1]) - ord('a')

            # Update for character entering the window
            if s1_counts[char_in_idx] == window_counts[char_in_idx]:
                matches -= 1
            window_counts[char_in_idx] += 1
            if s1_counts[char_in_idx] == window_counts[char_in_idx]:
                matches += 1

            # Update for character leaving the window
            if s1_counts[char_out_idx] == window_counts[char_out_idx]:
                matches -= 1
            window_counts[char_out_idx] -= 1
            if s1_counts[char_out_idx] == window_counts[char_out_idx]:
                matches += 1

            if matches == 26:
                return True

        return False