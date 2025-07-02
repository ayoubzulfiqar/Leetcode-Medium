class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        max_xor = 0
        mask = 0
        
        # Iterate from the most significant bit (30th bit for 2^31 - 1)
        # down to the least significant bit (0th bit).
        for i in range(30, -1, -1):
            # Update the mask to include the current bit.
            # The mask grows from MSB to LSB, accumulating bits we are considering.
            # For example:
            # i=30, mask = 100...00 (1 << 30)
            # i=29, mask = 110...00 ((1 << 30) | (1 << 29))
            mask = mask | (1 << i)
            
            # Create a set of prefixes for all numbers in nums,
            # considering only the bits covered by the current mask.
            # For a number `num`, `num & mask` gives its prefix up to bit `i`.
            prefix_set = set()
            for num in nums:
                prefix_set.add(num & mask)
            
            # This is the potential maximum XOR value we are trying to achieve.
            # We assume we can set the current bit (i) to 1 in max_xor.
            # If we can achieve this, it means there exist two numbers whose XOR
            # has this prefix (up to bit i).
            temp_max_xor = max_xor | (1 << i)
            
            # Check if temp_max_xor can be formed by XORing two prefixes from prefix_set.
            # For any prefix `p` in `prefix_set`, if `(p ^ temp_max_xor)` is also in `prefix_set`,
            # it means we found two numbers, say `num_a` and `num_b`, such that:
            # (num_a & mask) = p
            # (num_b & mask) = (p ^ temp_max_xor)
            # Then, (num_a & mask) ^ (num_b & mask) = p ^ (p ^ temp_max_xor) = temp_max_xor.
            # This implies that the XOR of `num_a` and `num_b` (when truncated by mask)
            # is equal to `temp_max_xor`.
            # If such a pair exists, it means we successfully set the i-th bit to 1
            # in our current `max_xor`.
            found = False
            for p in prefix_set:
                if (p ^ temp_max_xor) in prefix_set:
                    max_xor = temp_max_xor
                    found = True
                    break # Found a pair for this bit, move to the next lower bit
            
        return max_xor