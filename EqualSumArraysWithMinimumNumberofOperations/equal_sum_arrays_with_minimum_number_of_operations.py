import collections

class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)

        if len1 * 6 < len2 * 1 or len2 * 6 < len1 * 1:
            return -1

        s1 = sum(nums1)
        s2 = sum(nums2)

        if s1 == s2:
            return 0

        if s1 < s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        
        diff = s1 - s2
        operations = 0

        gains_counts = collections.Counter()

        for x in nums1:
            gains_counts[x - 1] += 1

        for x in nums2:
            gains_counts[6 - x] += 1
        
        for gain in range(5, 0, -1):
            if diff <= 0:
                break

            count_for_this_gain = gains_counts[gain]

            if count_for_this_gain == 0:
                continue

            num_ops_needed_at_this_gain = (diff + gain - 1) // gain

            ops_to_take = min(count_for_this_gain, num_ops_needed_at_this_gain)

            operations += ops_to_take
            diff -= ops_to_take * gain

        return operations