def findPowerOfKSizeSubarrays(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    results = []

    if k == 1:
        return nums[:]

    is_consecutive_flags = [False] * (n - 1)
    for j in range(n - 1):
        if nums[j+1] == nums[j] + 1:
            is_consecutive_flags[j] = True

    bad_pairs_count = 0
    for j in range(k - 1):
        if not is_consecutive_flags[j]:
            bad_pairs_count += 1

    if bad_pairs_count == 0:
        results.append(nums[k-1])
    else:
        results.append(-1)

    for i in range(1, n - k + 1):
        if not is_consecutive_flags[i-1]:
            bad_pairs_count -= 1

        if not is_consecutive_flags[i+k-2]:
            bad_pairs_count += 1

        if bad_pairs_count == 0:
            results.append(nums[i+k-1])
        else:
            results.append(-1)

    return results