class RLEIterator:

    def __init__(self, encoded: list[int]):
        self.encoded = encoded
        self.ptr = 0  # Pointer to the current count in the encoded array

    def next(self, n: int) -> int:
        last_exhausted_value = -1

        while n > 0 and self.ptr < len(self.encoded):
            current_count = self.encoded[self.ptr]
            current_value = self.encoded[self.ptr + 1]

            if current_count >= n:
                # The current segment has enough or more elements than 'n'
                self.encoded[self.ptr] -= n  # Reduce the count in the current segment
                last_exhausted_value = current_value
                n = 0  # All 'n' elements have been exhausted
            else:
                # The current segment does not have enough elements
                n -= current_count  # Exhaust all elements in the current segment
                self.ptr += 2  # Move to the next segment (skip count and value)
                # last_exhausted_value is not updated here because we need to find
                # the *last* element exhausted. If we exhaust this segment and still
                # need more, the true last element will come from a subsequent segment.

        if n > 0:
            # If n is still greater than 0, it means we ran out of elements in the encoded array
            return -1
        else:
            # All 'n' elements were exhausted, return the value of the last one
            return last_exhausted_value