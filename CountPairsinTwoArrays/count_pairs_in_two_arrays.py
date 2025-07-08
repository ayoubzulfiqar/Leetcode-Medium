import bisect

def countPairs(nums1, nums2):
    if not nums1 or not nums2:
        return 0

    nums2.sort()

    count = 0
    for x in nums1:
        count += bisect.bisect_left(nums2, x)
    
    return count