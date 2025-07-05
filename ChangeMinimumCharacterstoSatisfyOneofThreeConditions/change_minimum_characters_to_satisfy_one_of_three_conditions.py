class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        freq_a = [0] * 26
        freq_b = [0] * 26

        for char_code in map(ord, a):
            freq_a[char_code - ord('a')] += 1
        for char_code in map(ord, b):
            freq_b[char_code - ord('a')] += 1

        len_a = len(a)
        len_b = len(b)

        min_ops = float('inf')

        # Condition 3: Both a and b consist of only one distinct letter.
        for i in range(26):
            ops = (len_a - freq_a[i]) + (len_b - freq_b[i])
            min_ops = min(min_ops, ops)

        prefix_sum_a = [0] * 26
        prefix_sum_b = [0] * 26

        prefix_sum_a[0] = freq_a[0]
        prefix_sum_b[0] = freq_b[0]
        for i in range(1, 26):
            prefix_sum_a[i] = prefix_sum_a[i-1] + freq_a[i]
            prefix_sum_b[i] = prefix_sum_b[i-1] + freq_b[i]

        # Condition 1 & 2: a < b or b < a
        # Iterate through possible split characters 'a' to 'y' (index 0 to 24)
        for i in range(25):
            # Condition 1: Every letter in a is strictly less than every letter in b.
            # All chars in 'a' must be <= char at index 'i'.
            # All chars in 'b' must be >= char at index 'i+1'.
            cost_a_less_b = (len_a - prefix_sum_a[i]) + prefix_sum_b[i]
            min_ops = min(min_ops, cost_a_less_b)

            # Condition 2: Every letter in b is strictly less than every letter in a.
            # All chars in 'b' must be <= char at index 'i'.
            # All chars in 'a' must be >= char at index 'i+1'.
            cost_b_less_a = (len_b - prefix_sum_b[i]) + prefix_sum_a[i]
            min_ops = min(min_ops, cost_b_less_a)

        return min_ops