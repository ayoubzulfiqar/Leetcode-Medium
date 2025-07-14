class Solution:
    def maxTheNumber(self, k: int, x: int) -> int:
        # Helper function to calculate the accumulated price for a given number 'num'
        # and bit position multiplier 'x'.
        # The accumulated price is the sum of prices for numbers from 1 to 'num'.
        # The price of a number 'i' is the count of set bits at positions x, 2x, 3x, ...
        def calculate_accumulated_price(num: int, x: int) -> int:
            total_price = 0
            j = 1
            
            # Iterate through relevant bit positions: x, 2x, 3x, ...
            # The 0-indexed bit positions are (j*x - 1).
            # We need to consider bit positions as long as they can contribute to the sum.
            # The maximum possible 'num' for k=10^15 is around 2 * 10^14, which is less than 2^48.
            # So, bit positions up to around 47-50 are relevant.
            # A safe upper bound for bit positions for numbers up to 2^60 (approx 10^18) is 60.
            # If (j*x - 1) exceeds this, 2^(j*x-1) will be very large, and its contribution
            # to the count of set bits for numbers up to 'num' will be zero.
            while True:
                pos = j * x - 1  # 0-indexed bit position
                
                # If the current bit position is too high, it won't contribute to the sum
                # for any number up to the maximum possible 'num'.
                if pos > 60: 
                    break

                # Calculate 2^pos and 2^(pos+1) efficiently using bit shifts
                half_block = 1 << pos      # Represents 2^pos
                block_size = 1 << (pos + 1) # Represents 2^(pos+1)

                # Count