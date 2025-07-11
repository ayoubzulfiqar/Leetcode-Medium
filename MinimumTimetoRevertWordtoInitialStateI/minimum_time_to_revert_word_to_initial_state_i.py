class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)

        # Iterate through possible times t, starting from 1.
        # At each second 't', we conceptually remove the first 'k' characters 't' times.
        # This means the prefix of length 't*k' is removed.
        # The remaining part of the word is `word[t*k:]`.
        # To revert to the initial state, the remaining part `word[t*k:]`
        # must match the prefix of the original word of the same length,
        # which is `word[:n - t*k]`.
        # The problem states we can add *any* k characters. This implies that if the
        # remaining suffix matches the required prefix of the original word,
        # we can always add the necessary characters to complete the original word.

        # The loop continues as long as t*k is a valid index for slicing, up to n.
        # If t*k equals n, it means the entire string has been effectively shifted.
        # In this case, `word[n:]` is an empty string, and `word[:n-n]` (i.e., `word[:0]`)
        # is also an empty string. Empty strings are equal, so this case always results
        # in a match, meaning the word has reverted to its initial state.
        # Therefore, the loop must go up to `n // k` (integer division) for `t`.
        # `range(1, n // k + 1)` covers all relevant `t` values.

        for t in range(1, n // k + 1):
            # Check if the suffix of the current word (after t*k characters are removed)
            # matches the prefix of the original word of the same length.
            if word[t * k:] == word[:n - t * k]:
                return t

        # This line should theoretically not be reached because at worst,
        # when t*k equals n (i.e., t = n/k), the condition word[n:] == word[:0]
        # (empty string == empty string) will always be true, and the function will return t.
        # The problem guarantees a solution exists.