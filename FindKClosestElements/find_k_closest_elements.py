def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    """
    Finds the k closest integers to x in a sorted integer array arr.

    Args:
        arr: A sorted list of integers.
        k: The number of closest integers to return.
        x: The integer to find closest elements to.

    Returns:
        A list of k closest integers to x, sorted in ascending order.
    """
    left = 0
    right = len(arr) - 1

    # Use a two-pointer approach to shrink the window until only k elements remain.
    # The elements to be removed are those further from x.
    # If distances are equal, the tie-breaking rule is to keep the smaller element.
    while right - left + 1 > k:
        dist_left = abs(arr[left] - x)
        dist_right = abs(arr[right] - x)

        # Compare distances to x
        if dist_left <= dist_right:
            # If arr[left] is closer or equally close (and smaller value due to array being sorted),
            # then arr[right] is the one to discard as it's either further or equally close but larger.
            right -= 1
        else:
            # arr[right] is strictly closer than arr[left].
            # Discard arr[left].
            left += 1

    # The remaining window arr[left:right+1] contains the k closest elements.
    # Since the original array was sorted and we only removed elements from the ends,
    # the remaining sub-array is also sorted.
    return arr[left : right + 1]