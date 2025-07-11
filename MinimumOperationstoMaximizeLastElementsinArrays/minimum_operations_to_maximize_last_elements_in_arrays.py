import math

class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)

        def calculate_ops(target1_n_1: int, target2_n_1: int, initial_ops: int) -> int:
            current_ops = initial_ops
            for i in range(n - 1):
                val1_i = nums1[i]
                val2_i = nums2[i]

                can_no_swap = (val1_i <= target1_n_1) and (val2_i <= target2_n_1)
                can_swap = (val2_i <= target1_n_1) and (val1_i <= target2_n_1)

                if can_no_swap:
                    pass
                elif can_swap:
                    current_ops += 1
                else:
                    return math.inf
            return current_ops

        min_ops = math.inf

        # Case 1: No swap at index n-1
        ops_case1 = calculate_ops(nums1[n-1], nums2[n-1], 0)
        min_ops = min(min_ops, ops_case1)

        # Case 2: Swap at index n-1
        ops_case2 = calculate_ops(nums2[n-1], nums1[n-1], 1)
        min_ops = min(min_ops, ops_case2)

        if min_ops == math.inf:
            return -1
        else:
            return min_ops