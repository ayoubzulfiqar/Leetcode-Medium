class Solution:
    def minAbsoluteDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        N = len(nums)
        MAX_VAL = 100 

        # prefix_counts[i][j] stores the count of number j in nums[0...i-1]
        # The size is (N+1) x (MAX_VAL + 1) to handle 0-based indexing for nums
        # and 1-based indexing for values (1 to MAX_VAL).
        prefix_counts = [[0] * (MAX_VAL + 1) for _ in range(N + 1)]

        # Build prefix_counts array
        for i in range(N):
            # Copy counts from the previous prefix
            for j in range(1, MAX_VAL + 1): 
                prefix_counts[i+1][j] = prefix_counts[i][j]
            # Increment count for the current number nums[i]
            prefix_counts[i+1][nums[i]] += 1

        results = []
        for li, ri in queries:
            # current_counts will store frequencies for the subarray nums[li...ri]
            current_counts = [0] * (MAX_VAL + 1)
            for val in range(1, MAX_VAL + 1):
                # Count of 'val' in nums[li...ri] = count in nums[0...ri] - count in nums[0...li-1]
                current_counts[val] = prefix_counts[ri+1][val] - prefix_counts[li][val]

            min_diff = float('inf')
            last_seen_val = -1 # To keep track of the last distinct value encountered

            # Iterate through possible values from 1 to MAX_VAL
            for val in range(1, MAX_VAL + 1):
                if current_counts[val] > 0: # If 'val' is present in the subarray
                    if last_seen_val != -1: # If there was a previous distinct value
                        min_diff = min(min_diff, val - last_seen_val)
                    last_seen_val = val # Update last_seen_val to the current 'val'
            
            # If min_diff is still infinity, it means no two distinct numbers were found
            # (i.e., all numbers in the subarray were the same or there was only one number).
            if min_diff == float('inf'):
                results.append(-1)
            else:
                results.append(min_diff)
        
        return results