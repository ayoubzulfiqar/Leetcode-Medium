class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        
        def count_chars(s: str) -> list[int]:
            counts = [0] * 26
            for char_code in s:
                counts[ord(char_code) - ord('a')] += 1
            return counts

        max_counts_b = [0] * 26
        for b_word in words2:
            current_b_counts = count_chars(b_word)
            for i in range(26):
                max_counts_b[i] = max(max_counts_b[i], current_b_counts[i])

        result = []
        for a_word in words1:
            counts_a = count_chars(a_word)
            is_universal = True
            for i in range(26):
                if counts_a[i] < max_counts_b[i]:
                    is_universal = False
                    break
            if is_universal:
                result.append(a_word)

        return result