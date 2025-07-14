import collections

class Solution:
    def longestSubset(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        
        # Initialize max_len to 1, as any single element can form a valid subset [x].
        max_len = 1 
        
        # Handle the special case of '1'.
        # If '1' is present, any number of '1's can form a sequence like [1, 1, ..., 1].
        # The length of such a sequence is simply the count of '1's available.
        if 1 in counts:
            max_len = max(max_len, counts[1])
            
        # Iterate through each unique number in the counts dictionary.
        # We don't need to sort or use a visited set because the max_len will correctly
        # capture the longest chain regardless of the starting point, and the number
        # of unique elements is manageable.
        for num in counts:
            # '1' has already been handled, so skip it here.
            if num == 1:
                continue 