class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)

        current_a = a
        repetitions = 1

        # Keep repeating 'a' until 'current_a' is at least as long as 'b'
        # This covers the case where b is a direct multiple of a, or slightly longer.
        while len(current_a) < len_b:
            current_a += a
            repetitions += 1
        
        # At this point, len(current_a) >= len_b.
        # Check if 'b' is a substring of 'current_a'.
        if b in current_a:
            return repetitions
        
        # If 'b' is not found, it might be because 'b' spans across the boundary
        # of 'current_a' and the next 'a'.
        # For example, if a = "abc", b = "cab".
        # After the loop, current_a = "abc", repetitions = 1. 'cab' is not in "abc".
        # Appending 'a' one more time makes current_a = "abcabc", repetitions = 2.
        # Now 'cab' is in "abcabc".
        # This single additional repetition is sufficient because 'b' can span at most
        # two 'a' blocks (e.g., suffix of first 'a' + prefix of second 'a'),
        # or it can span more blocks but will still fit within the length of current_a + a.
        # The maximum length of b is 10^4.
        # The length of current_a is roughly len_b.
        # If 'b' is not in current_a, it means 'b' must start in the last 'a' block
        # of current_a and extend into the next 'a' block.
        # So current_a + a should cover this case.
        
        current_a += a
        repetitions += 1
        
        if b in current_a:
            return repetitions
        
        # If 'b' is still not found after checking up to (ceil(len_b / len_a) + 1) repetitions,
        # it's impossible for 'b' to be a substring of any repetition of 'a'.
        return -1