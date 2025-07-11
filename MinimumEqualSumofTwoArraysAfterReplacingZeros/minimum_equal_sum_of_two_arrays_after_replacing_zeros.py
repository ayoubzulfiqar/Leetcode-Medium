class Solution:
    def minimumEqualSum(self, nums1: list[int], nums2: list[int]) -> int:
        sum1 = 0
        zeros1 = 0
        for num in nums1:
            if num == 0:
                zeros1 += 1
            sum1 += num

        sum2 = 0
        zeros2 = 0
        for num in nums2:
            if num == 0:
                zeros2 += 1
            sum2 += num

        # Calculate minimum possible sum for each array if all zeros are replaced by 1
        min_possible_sum1 = sum1 + zeros1
        min_possible_sum2 = sum2 + zeros2

        # Case 1: Both arrays have zeros
        if zeros1 > 0 and zeros2 > 0:
            # The minimum equal sum is the maximum of their individual minimum possible sums.
            # This is always achievable because we can always increase the sum of an array
            # that has zeros by replacing a zero with a value greater than 1.
            return max(min_possible_sum1, min_possible_sum2)

        # Case 2: Only nums1 has zeros (nums2 has no zeros)
        elif zeros1 > 0 and zeros2 == 0:
            # nums2's sum is fixed at sum2.
            # For nums1 to match, its sum must be exactly sum2.
            # This is possible only if sum2 is greater than or equal to nums1's minimum possible sum.
            if sum2 >= min_possible_sum1:
                return sum2
            else:
                return -1 # Cannot make nums1's sum equal to sum2
        
        # Case 3: Only nums2 has zeros (nums1 has no zeros)
        elif zeros1 == 0 and zeros2 > 0:
            # nums1's sum is fixed at sum1.
            # For nums2 to match, its sum must be exactly sum1.
            # This is possible only if sum1 is greater than or equal to nums2's minimum possible sum.
            if sum1 >= min_possible_sum2:
                return sum1
            else:
                return -1 # Cannot make nums2's sum equal to sum1

        # Case 4: Neither array has zeros
        elif zeros1 == 0 and zeros2 == 0:
            # Both sums are fixed. They must be equal.
            if sum1 == sum2:
                return sum1
            else:
                return -1 # Cannot make sums equal