class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Ensure words1 is the shorter or equal length list
        if len(words1) > len(words2):
            words1, words2 = words2, words1

        n1 = len(words1)
        n2 = len(words2)

        # Pointers for matching from left and right
        left = 0
        right = 0

        # Match common prefix
        while left < n1 and words1[left] == words2[left]:
            left += 1

        # Match common suffix
        # The condition 'right < n1 - left' ensures that the suffix match
        # does not overlap with the prefix match in the shorter sentence (words1).
        # It means we can match at most (n1 - left) words from the suffix.
        while right < n1 - left and words1[n1 - 1 - right] == words2[n2 - 1 - right]:
            right += 1

        # If the sum of matched prefix words and matched suffix words
        # is greater than or equal to the length of the shorter sentence,
        # then the shorter sentence can be formed by removing a contiguous block
        # from the middle of the longer sentence (or from its beginning/end).
        return left + right >= n1