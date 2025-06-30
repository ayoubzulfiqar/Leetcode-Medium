import math

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_so_far = nums[0]
        current_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current_max = max(num, current_max + num)
            max_so_far = max(max_so_far, current_max)
        return max_so_far

    def maxSubArray_divide_conquer(self, nums: list[int]) -> int:
        def find_max_crossing_subarray(arr, low, mid, high):
            left_sum = -math.inf
            current_sum = 0
            for i in range(mid, low - 1, -1):
                current_sum += arr[i]
                if current_sum > left_sum:
                    left_sum = current_sum

            right_sum = -math.inf
            current_sum = 0
            for i in range(mid + 1, high + 1):
                current_sum += arr[i]
                if current_sum > right_sum:
                    right_sum = current_sum
            
            return left_sum + right_sum

        def find_max_subarray_recursive(arr, low, high):
            if low == high:
                return arr[low]
            
            mid = (low + high) // 2
            
            left_max = find_max_subarray_recursive(arr, low, mid)
            right_max = find_max_subarray_recursive(arr, mid + 1, high)
            cross_max = find_max_crossing_subarray(arr, low, mid, high)
            
            return max(left_max, right_max, cross_max)
        
        return find_max_subarray_recursive(nums, 0, len(nums) - 1)