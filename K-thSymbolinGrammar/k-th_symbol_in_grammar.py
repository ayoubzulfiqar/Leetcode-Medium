class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        # Calculate the length of the first half of the current row (n).
        # This is equivalent to the length of the (n-1)th row.
        # The length of row 'm' is 2^(m-1).
        # So, the length of row (n-1) is 2^((n-1)-1) = 2^(n-2).
        # This also represents the midpoint for the current row 'n'.
        mid = 1 << (n - 2)

        if k <= mid:
            # If k is in the first half, the symbol is the same as
            # the k-th symbol in the (n-1)th row.
            return self.kthGrammar(n - 1, k)
        else:
            # If k is in the second half, the symbol is the complement of
            # the corresponding symbol in the (n-1)th row.
            # The corresponding index in the (n-1)th row is k - mid.
            prev_symbol = self.kthGrammar(n - 1, k - mid)
            # Flip the bit: 0 becomes 1, 1 becomes 0.
            return 1 - prev_symbol