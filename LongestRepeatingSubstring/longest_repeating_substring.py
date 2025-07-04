def longestRepeatingSubstring(s: str) -> int:
    """
    Finds the length of the longest repeating substring in a given string.
    A repeating substring is a substring that appears at least twice in the string.
    The occurrences can overlap.

    This solution uses the Suffix Array and Longest Common Prefix (LCP) array concept.
    It constructs all suffixes, sorts them, and then finds the maximum LCP
    between adjacent suffixes in the sorted list.

    Time Complexity: O(N^2 log N) due to sorting N suffixes, each of length up to N.
                     String slicing and LCP calculation also contribute to O(N^2).
    Space Complexity: O(N^2) due to storing N copies of suffixes.
    """

    n = len(s)
    if n == 0:
        return 0

    # Helper function to compute the Longest Common Prefix (LCP) of two strings
    def _lcp(s1: str, s2: str) -> int:
        i = 0
        # Iterate while characters match and within bounds of both strings
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1
        return i

    # 1. Generate all suffixes of the string.
    # This creates N substrings, each taking up to O(N) time and space for copying.
    # Total O(N^2) time and space for this step.
    suffixes = [s[i:] for i in range(n)]

    # 2. Sort the suffixes lexicographically.
    # Python's list.sort() uses Timsort, which is O(K log K) comparisons for K items.
    # For strings, each comparison can take up to O(L) time, where L is the length
    # of the strings being compared (up to N).
    # So, this step is O(N * N log N) = O(N^2 log N).
    suffixes.sort()

    max_lcp_len = 0

    # 3. Iterate through adjacent sorted suffixes to find the maximum LCP.
    # The longest repeating substring will be the longest common prefix
    # between any two adjacent suffixes in the sorted suffix array.
    # There are N-1 pairs of adjacent suffixes.
    # Each _lcp call can take up to O(N) time in the worst case.
    # Total O(N * N) = O(N^2) for this step.
    for i in range(n - 1):
        current_lcp = _lcp(suffixes[i], suffixes[i+1])
        if current_lcp > max_lcp_len:
            max_lcp_len = current_lcp

    return max_lcp_len