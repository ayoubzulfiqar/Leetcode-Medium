class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        max_combination_size = 0
        
        # Iterate through all possible bit positions.
        # Since candidates[i] <= 10^7, the maximum value is less than 2^24.
        # This means numbers can have bits set from position 0 up to 23.
        # So, we need to check bits from 0 to 23 inclusive.
        for bit_pos in range(24): # Covers bit positions 0 to 23
            current_bit_count = 0
            # Count how many numbers in candidates have the current bit_pos set
            for num in candidates:
                # Check if the bit_pos-th bit is set in 'num'
                # (num >> bit_pos) shifts the bit to the 0th position.
                # & 1 isolates that 0th bit. If it's 1, the bit was set.
                if (num >> bit_pos) & 1:
                    current_bit_count += 1
            
            # Update the maximum combination size found so far
            max_combination_size = max(max_combination_size, current_bit_count)
            
        return max_combination_size