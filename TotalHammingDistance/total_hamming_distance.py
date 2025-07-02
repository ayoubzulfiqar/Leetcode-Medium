class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        total_distance = 0
        # Iterate over each bit position from 0 up to 29 (inclusive).
        # The maximum value for nums[i] is 10^9, which is less than 2^30.
        # Therefore, bits beyond the 29th bit will always be 0 for all numbers.
        # Checking 30 bits (from 0 to 29) is sufficient.
        for i in range(30):
            count_zero = 0
            count_one = 0
            for num in nums:
                # Check the i-th bit of the current number
                if (num >> i) & 1:
                    count_one += 1
                else:
                    count_zero += 1
            
            # For the current bit position, each pair consisting of one number
            # with a 0 at this bit and one number with a 1 at this bit
            # contributes 1 to the total Hamming distance.
            # The number of such pairs is count_zero * count_one.
            total_distance += count_zero * count_one
            
        return total_distance