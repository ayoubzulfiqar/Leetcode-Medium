class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 0:
                # If the target bit for (a OR b) is 0,
                # then both the current bits of 'a' and 'b' must be 0.
                # Count flips if they are 1.
                if bit_a == 1:
                    flips += 1
                if bit_b == 1:
                    flips += 1
            else: # bit_c == 1
                # If the target bit for (a OR b) is 1,
                # then at least one of the current bits of 'a' or 'b' must be 1.
                # If both are 0, we need one flip (either a or b to 1).
                if bit_a == 0 and bit_b == 0:
                    flips += 1
                # If (bit_a == 1 or bit_b == 1), then (bit_a OR bit_b) is already 1,
                # so no flips are needed for this bit position.

            # Move to the next bit (right shift)
            a >>= 1
            b >>= 1
            c >>= 1
            
        return flips