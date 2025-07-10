class Solution:
    def maximumOr(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Precompute prefix ORs
        # prefix_or[i] stores the bitwise OR of nums[0] through nums[i-1].
        # prefix_or[0] will be 0 (representing an empty prefix).
        prefix_or = [0] * n
        current_prefix_or = 0
        for i in range(n):
            prefix_or[i] = current_prefix_or
            current_prefix_or |= nums[i]

        # Precompute suffix ORs
        # suffix_or[i] stores the bitwise OR of nums[i+1] through nums[n-1].
        # suffix_or[n-1] will be 0 (representing an empty suffix).
        suffix_or = [0] * n
        current_suffix_or = 0
        for i in range(n - 1, -1, -1):
            suffix_or[i] = current_suffix_or
            current_suffix_or |= nums[i]

        max_overall_or = 0
        
        # Calculate 2^k, which is equivalent to 1 << k
        multiplier = 1 << k

        # Iterate through each element in nums
        # For each nums[i], assume we apply all k operations to it.
        for i in range(n):
            # Calculate the bitwise OR of:
            # 1. The OR of elements before nums[i] (prefix_or[i])
            # 2. nums[i] after being multiplied by 2^k (nums[i] * multiplier)
            # 3. The OR of elements after nums[i] (suffix_or[i])
            current_overall_or = prefix_or[i] | (nums[i] * multiplier) | suffix_or[i]
            
            # Update the maximum OR sum found so far
            if current_overall_or > max_overall_or:
                max_overall_or = current_overall_or
        
        return max_overall_or