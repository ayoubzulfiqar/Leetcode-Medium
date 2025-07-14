class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        n = len(colors)
        
        # Step 1: Create a boolean array indicating if colors[i] != colors[i+1] (circularly).
        # alt_flags[i] is True if colors[i] and colors[(i+1)%n] are different.
        # This array will have length n.
        alt_flags = [False] * n
        for i in range(n):
            alt_flags[i] = (colors[i] != colors[(i + 1) % n])
            
        # Step 2: Pad alt_flags to handle circularity easily for the sliding window.
        # A group of k tiles requires k-1 alternating conditions.
        # For a group starting at colors[i], we check alt_flags[i], alt_flags[(i+1)%n], ..., alt_flags[(i+k-2)%n].
        # To avoid explicit modulo operations in the sliding window, we append the first k-2 elements
        # of alt_flags to its end. This ensures that for any starting index `i` from 0 to n-1,
        # the window of `k-1` elements (from `i` to `i+k-2`) can be accessed directly from `alt_flags_padded`.
        alt_flags_padded = alt_flags + alt_flags[:k-2]
        
        false_count = 0
        ans = 0
        
        # Step 3: Calculate false_count for the initial window (corresponding to the group starting at colors[0]).
        # This window covers alt_flags_padded[0] to alt_flags_padded[k-2].
        for j in range(k - 1): # This loop runs k-1 times
            if not alt_flags_padded[j]:
                false_count += 1
                
        # If false_count is 0, the first group is alternating.
        if false_count == 0:
            ans += 1
            
        # Step 4: Slide the window for subsequent starting positions.
        # Iterate `i` from 1 to n-1.
        # In each iteration, we remove the leftmost element of the previous window
        # and add the rightmost element of the new window.
        for i in range(1, n):
            # Remove the leftmost element's contribution from the previous window.
            # This element is alt_flags_padded[i-1].
            if not alt_flags_padded[i - 1]:
                false_count -= 1
            
            # Add the rightmost element's contribution to the new window.
            # The new window's indices are [i, ..., i + k - 2].
            # So, the new element to add is alt_flags_padded[i + k - 2].
            if not alt_flags_padded[i + k - 2]:
                false_count += 1
                
            # If false_count is 0, the current group is alternating.
            if false_count == 0:
                ans += 1
                
        return ans