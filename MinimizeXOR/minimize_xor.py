class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits_count = bin(num2).count('1')
        x = 0

        # Phase 1: Try to set bits in x where num1 also has set bits, from MSB to LSB.
        # This minimizes the XOR value by making (x_i XOR num1_i) = 0 for high-order bits.
        # Iterate from a sufficiently high bit (e.g., 30, as 2^30 > 10^9) down to 0.
        for i in range(30, -1, -1):
            # If the i-th bit of num1 is set
            if (num1 >> i) & 1:
                # And we still need to set bits in x
                if set_bits_count > 0:
                    x |= (1 << i) # Set the i-th bit of x
                    set_bits_count -= 1
        
        # Phase 2: If we still need to set bits in x, set them in positions where num1 has 0.
        # To minimize the XOR value, set these remaining bits at the lowest possible positions.
        # Iterate from LSB (0) up to a sufficiently high bit (e.g., 30).
        for i in range(31):
            # If we still need to set bits in x AND
            # the i-th bit of x is currently unset (meaning num1 also had it unset, or it was already set in phase 1)
            if set_bits_count > 0 and not ((x >> i) & 1):
                x |= (1 << i) # Set the i-th bit of x
                set_bits_count -= 1
            
            # If all required bits are set, we can stop early
            if set_bits_count == 0:
                break
                
        return x