class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if k == 0:
            return 0
        if n == 1:
            return k
        
        # same_ways represents the number of ways to paint 'i' posts
        # such that the i-th post has the same color as the (i-1)-th post.
        # For n=2: The first post can be any of k colors. The second must be the same.
        # This implies the (i-1)th post (which is the first post here) must be different from a non-existent (i-2)th post.
        # This corresponds to diff_ways from n=1, which is k.
        same_ways = k 
        
        # diff_ways represents the number of ways to paint 'i' posts
        # such that the i-th post has a different color than the (i-1)-th post.
        # For n=2: The first post can be any of k colors. The second can be any of k-1 different colors.
        # So, k * (k-1) ways.
        diff_ways = k * (k - 1)
        
        # Iterate from n=3 up to the given n
        for i in range(3, n + 1):
            # Store the values from the previous step (i-1)
            prev_same_ways = same_ways
            prev_diff_ways = diff_ways
            
            # Calculate same_ways for current 'i':
            # If the current post is the same color as the previous (i-1) post,
            # then the (i-1) post must have been a different color from the (i-2) post
            # to avoid three consecutive posts of the same color.
            # So, same_ways for 'i' equals diff_ways for 'i-1'.
            same_ways = prev_diff_ways
            
            # Calculate diff_ways for current 'i':
            # If the current post is a different color from the previous (i-1) post,
            # the (i-1) post could have been either the same color or a different color
            # from the (i-2) post.
            # The total number of ways to paint (i-1) posts is (prev_same_ways + prev_diff_ways).
            # For the current 'i' post, there are (k-1) color choices (any color except the one used for (i-1)).
            diff_ways = (prev_same_ways + prev_diff_ways) * (k - 1)
            
        # The total number of ways to paint 'n' posts is the sum of ways ending with
        # the same color as the previous, and ways ending with a different color.
        return same_ways + diff_ways