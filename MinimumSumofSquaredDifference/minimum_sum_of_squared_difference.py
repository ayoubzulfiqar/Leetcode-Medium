class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k_total = k1 + k2

        max_diff_val = 0
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            if d > max_diff_val:
                max_diff_val = d
        
        counts = [0] * (max_diff_val + 1)
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            counts[d] += 1

        for d_val in range(max_diff_val, 0, -1):
            if k_total == 0:
                break
            
            if counts[d_val] > 0:
                num_elements_at_d = counts[d_val]

                if k_total >= num_elements_at_d:
                    k_total -= num_elements_at_d
                    counts[d_val - 1] += num_elements_at_d
                    counts[d_val] = 0
                else:
                    counts[d_val - 1] += k_total
                    counts[d_val] -= k_total
                    k_total = 0
                    break 

        min_sum_sq_diff = 0
        for d_val in range(max_diff_val + 1):
            if counts[d_val] > 0:
                min_sum_sq_diff += counts[d_val] * (d_val * d_val)

        return min_sum_sq_diff