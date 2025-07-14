import collections

class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # dp[i] will store the maximum score to reach index i
        dp = [0] * n
        
        # Base case: The score to reach index 0 is nums[0]
        dp[0] = nums[0]
        
        # Deque to store indices. The indices are stored in increasing order,
        # and their corresponding dp values (dp[index]) are in decreasing order.
        # This ensures that the front of the deque (dq[0]) always holds the index
        # with the maximum dp value within the current sliding window [i - k, i - 1].
        dq = collections.deque()
        dq.append(0) # Add the starting index 0 to the deque
        
        # Iterate from index 1 to n-1
        for i in range(1, n):
            # Remove indices from the front of the deque that are no longer
            # reachable from the current index i (i.e., they are outside the k-range).
            # An index j is out of range if j < i - k.
            while dq and dq[0] < i - k:
                dq.popleft()
            
            # The maximum score to reach index i is nums[i] plus the maximum score
            # from a reachable previous index. The index with the maximum score
            # is at the front of the deque (dq[0]).
            dp[i] = nums[i] + dp[dq[0]]
            
            # Remove indices from the back of the deque if their dp value is
            # less than or equal to dp[i]. This maintains the decreasing order
            # of dp values in the deque, ensuring that dq[0] always points to the maximum.
            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            
            # Add the current index i to the back of the deque.
            dq.append(i)
            
        # The maximum score to reach the last index n-1 is our result.
        return dp[n-1]