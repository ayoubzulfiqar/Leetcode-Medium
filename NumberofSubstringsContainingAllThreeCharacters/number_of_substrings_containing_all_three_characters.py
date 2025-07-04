class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        # last_seen stores the most recent index where 'a', 'b', or 'c' was encountered.
        # Initialize with -1 to indicate they haven't been seen yet.
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        n = len(s)

        # Iterate through the string with the right pointer 'i'
        for i in range(n):
            char = s[i]
            # Update the last seen index for the current character
            last_seen[char] = i

            # Check if all three characters ('a', 'b', 'c') have been seen at least once.
            # This is true if none of their last_seen indices are -1.
            if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
                # If all three characters are present in the current window ending at 'i',
                # we need to find the earliest possible starting index 'left' for such a substring.
                # This 'left' will be the minimum of the last seen indices of 'a', 'b', and 'c'.
                min_last_seen_idx = min(last_seen['a'], last_seen['b'], last_seen['c'])
                
                # Any substring starting from an index from 0 up to min_last_seen_idx (inclusive)
                # and ending at the current index 'i' will contain all three characters.
                # For example, if min_last_seen_idx is 2, it means s[2...i] contains all three.
                # Then s[1...i] and s[0...i] will also contain all three because they are longer
                # and include s[2...i].
                # The number of such valid starting positions is min_last_seen_idx + 1.
                count += (min_last_seen_idx + 1)
        
        return count