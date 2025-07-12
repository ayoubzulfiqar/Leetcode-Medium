import collections

class Solution:
    def minimumAddedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        nums1.sort()
        nums2.sort()

        possible_x_values = set()

        def check(x_val: int) -> bool:
            counts = collections.Counter(nums1)
            
            for val_s2 in nums2:
                expected_s1_val = val_s2 - x_val
                if counts[expected_s1_val] > 0:
                    counts[expected_s1_val] -= 1
                else:
                    return False
            
            return True

        # Case 1: The smallest element of the remaining nums1 is nums1[0].
        # This implies nums1[0] was not one of the two removed elements.
        # The value of x must be nums2[0] - nums1[0].
        x1 = nums2[0] - nums1[0]
        if check(x1):
            possible_x_values.add(x1)

        # Case 2: The smallest element of the remaining nums1 is nums1[1].
        # This implies nums1[0] was removed, and nums1[1] was not.
        # The value of x must be nums2[0] - nums1[1].
        x2 = nums2[0] - nums1[1]
        if check(x2):
            possible_x_values.add(x2)

        # Case 3: The smallest element of the remaining nums1 is nums1[2].
        # This implies nums1[0] and nums1[1] were removed, and nums1[2] was not.
        # The value of x must be nums2[0] - nums1[2].
        x3 = nums2[0] - nums1[2]
        if check(x3):
            possible_x_values.add(x3)
        
        return min(possible_x_values)