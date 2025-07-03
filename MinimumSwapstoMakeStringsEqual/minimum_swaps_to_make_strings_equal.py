def minSwaps(s1: str, s2: str) -> int:
    """
    Calculates the minimum number of swaps required to make two strings s1 and s2 equal.
    A swap involves exchanging a character s1[i] with s2[j].

    Args:
        s1: The first string consisting of 'x' and 'y'.
        s2: The second string consisting of 'x' and 'y'.

    Returns:
        The minimum number of swaps, or -1 if it's impossible.
    """
    count_xy = 0  # Number of positions where s1[i] = 'x' and s2[i] = 'y'
    count_yx = 0  # Number of positions where s1[i] = 'y' and s2[i] = 'x'

    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            if s1[i] == 'x':
                count_xy += 1
            else:  # s1[i] == 'y'
                count_yx += 1

    # If the total number of differing characters is odd, it's impossible to make them equal.
    # This is because each swap changes the parity of 'x's and 'y's in s1 and s2 by an even number.
    # For s1 and s2 to become equal, the total count of 'x's across both strings must be even,
    # and similarly for 'y's. This implies (count_xy + count_yx) must be even.
    if (count_xy + count_yx) % 2 != 0:
        return -1

    swaps = 0

    # Each pair of 'xy' mismatches can be resolved in 1 swap.
    # Example: s1="xx", s2="yy". Swap s1[0] and s2[1] -> s1="yx", s2="yx".
    swaps += count_xy // 2

    # Each pair of 'yx' mismatches can be resolved in 1 swap.
    # Example: s1="yy", s2="xx". Swap s1[0] and s2[1] -> s1="xy", s2="xy".
    swaps += count_yx // 2

    # If there's an odd number of 'xy' mismatches, there must also be an odd number of 'yx' mismatches
    # (because the total count_xy + count_yx is even).
    # These remaining single 'xy' and 'yx' mismatches require 2 swaps to resolve.
    # Example: s1="xy", s2="yx".
    # 1. Swap s1[0] and s2[0] -> s1="yy", s2="xx". (Now two 'yx' mismatches)
    # 2. Swap s1[0] and s2[1] -> s1="xy", s2="xy". (Resolved)
    if count_xy % 2 != 0:  # This implies count_yx % 2 != 0 as well
        swaps += 2

    return swaps