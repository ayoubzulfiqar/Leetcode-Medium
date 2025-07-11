def count_divisible_triplet_sums(nums, k):
    """
    Counts the number of triplets (nums[i], nums[j], nums[l]) from the input list
    such that i < j < l and their sum (nums[i] + nums[j] + nums[l]) is divisible by k.

    Args:
        nums: A list of integers.
        k: An integer divisor.

    Returns:
        The total count of such triplets.
    """
    n = len(nums)
    count = 0

    # Iterate through all possible combinations of three distinct indices (i, j, l)
    # such that i < j < l to ensure unique triplets.
    for i in range(n):
        for j in range(i + 1, n):
            for l in range(j + 1, n):
                # Calculate the sum of the current triplet
                current_sum = nums[i] + nums[j] + nums[l]

                # Check if the sum is divisible by k
                if current_sum % k == 0:
                    count += 1
    return count