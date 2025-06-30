class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        
        # If the array has only one element, we are already at the last index.
        if n == 1:
            return True
        
        # max_reach keeps track of the maximum index we can reach so far.
        # Initially, we are at index 0, so the maximum reach is 0.
        max_reach = 0
        
        # Iterate through the array up to the point we can reach.
        # We only need to check indices that are reachable.
        for i in range(n):
            # If the current index 'i' is beyond the maximum reach we've found so far,
            # it means we cannot reach this index, and therefore cannot reach the end.
            if i > max_reach:
                return False
            
            # Update the maximum reach possible.
            # max_reach is the furthest index we can reach from any position up to 'i'.
            max_reach = max(max_reach, i + nums[i])
            
            # If the maximum reach covers or exceeds the last index,
            # it means we can reach the end.
            if max_reach >= n - 1:
                return True
        
        # This line should theoretically not be reached if the logic is correct,
        # as the function would have returned True or False inside the loop.
        # However, it's a fallback and indicates failure if the loop completes
        # without reaching the last index.
        return False