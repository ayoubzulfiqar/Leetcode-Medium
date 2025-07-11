class Solution:
    def longestUnequalAdjacentGroupsSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        n = len(words)

        dp = [1] * n
        prev = [-1] * n

        def hamming_distance(s1, s2):
            dist = 0
            for k in range(len(s1)):
                if s1[k] != s2[k]:
                    dist += 1
            return dist

        for i in range(n):
            for j in range(i):
                if groups[j] != groups[i]:
                    if len(words[j]) == len(words[i]):
                        if hamming_distance(words[j], words[i]) == 1:
                            if dp[j] + 1 > dp[i]:
                                dp[i] = dp[j] + 1
                                prev[i] = j

        max_len = 0
        max_len_idx = -1

        if n > 0:
            max_len = 1
            max_len_idx = 0
            for i in range(n):
                if dp[i] > max_len:
                    max_len = dp[i]
                    max_len_idx = i
        else:
            return []

        result_indices = []
        current_idx = max_len_idx
        while current_idx != -1:
            result_indices.append(current_idx)
            current_idx = prev[current_idx]

        result_indices.reverse()

        result_words = [words[i] for i in result_indices]

        return result_words