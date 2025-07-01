class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        min_val = float('inf')
        max_val = float('-inf')
        for num in nums:
            min_val = min(min_val, num)
            max_val = max(max_val, num)

        if min_val == max_val:
            return 0

        bucket_size = max(1, (max_val - min_val) // (n - 1))
        num_buckets = (max_val - min_val) // bucket_size + 1

        buckets_min = [float('inf')] * num_buckets
        buckets_max = [float('-inf')] * num_buckets
        has_element = [False] * num_buckets

        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)
            has_element[idx] = True

        max_gap = 0
        prev_max = min_val

        for i in range(num_buckets):
            if has_element[i]:
                max_gap = max(max_gap, buckets_min[i] - prev_max)
                prev_max = buckets_max[i]
        
        return max_gap