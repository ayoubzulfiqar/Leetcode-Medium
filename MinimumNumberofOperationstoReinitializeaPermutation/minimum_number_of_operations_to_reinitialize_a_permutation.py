class Solution:
    def reinitializePermutation(self, n: int) -> int:
        current_pos = 1
        operations = 0

        while True:
            operations += 1
            if current_pos < n / 2:
                current_pos = 2 * current_pos
            else:
                current_pos = 2 * current_pos - n + 1

            if current_pos == 1:
                return operations