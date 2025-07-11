def count_divisible_subarrays(nums, k):
    remainder_counts = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        remainder = current_sum % k
        
        count += remainder_counts.get(remainder, 0)
        remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1
        
    return count