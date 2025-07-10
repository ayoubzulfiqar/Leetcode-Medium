class Solution:
    def minimumAdditions(self, word: str) -> int:
        additions = 0
        current_expected_idx = 0
        char_to_idx = {'a': 0, 'b': 1, 'c': 2}

        for char in word:
            char_idx = char_to_idx[char]

            if char_idx == current_expected_idx:
                current_expected_idx = (current_expected_idx + 1) % 3
            elif char_idx > current_expected_idx:
                additions += (char_idx - current_expected_idx)
                current_expected_idx = (char_idx + 1) % 3
            else:
                additions += (3 - current_expected_idx)
                additions += char_idx
                current_expected_idx = (char_idx + 1) % 3
        
        additions += (3 - current_expected_idx) % 3

        return additions