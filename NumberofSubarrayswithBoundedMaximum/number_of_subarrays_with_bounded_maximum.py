class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        def count_less_equal(bound: int) -> int:
            total_count = 0
            current_segment_length = 0
            for num in nums:
                if num <= bound:
                    current_segment_length += 1
                    total_count += current_segment_length
                else:
                    current_segment_length = 0
            return total_count

        return count_less_equal(right) - count_less_equal(left - 1)