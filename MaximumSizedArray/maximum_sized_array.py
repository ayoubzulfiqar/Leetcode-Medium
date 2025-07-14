def max_sized_subarray_sum_le_k(nums, k):
    left = 0
    current_sum = 0
    max_length = 0
    n = len(nums)

    for right in range(n):
        current_sum += nums[right]
        while current_sum > k:
            current_sum -= nums[left]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

if __name__ == '__main__':
    nums1 = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    k1 = 8
    result1 = max_sized_subarray_sum_le_k(nums1, k1)

    nums2 = [1, 1, 1, 1, 1]
    k2 = 3
    result2 = max_sized_subarray_sum_le_k(nums2, k2)

    nums3 = []
    k3 = 10
    result3 = max_sized_subarray_sum_le_k(nums3, k3)

    nums4 = [5]
    k4 = 5
    result4 = max_sized_subarray_sum_le_k(nums4, k4)

    nums5 = [10]
    k5 = 5
    result5 = max_sized_subarray_sum_le_k(nums5, k5)

    nums6 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    k6 = 3
    result6 = max_sized_subarray_sum_le_k(nums6, k6)