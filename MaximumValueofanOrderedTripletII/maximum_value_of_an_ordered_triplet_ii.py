class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        
        # max_right[j] stores the maximum value in nums from index j to n-1 (inclusive).
        # When calculating for a triplet (i, j, k), we need max(nums[k]) for k > j.
        # This corresponds to max_right[j+1].
        max_right = [0] * n
        max_right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], nums[i])
            
        max_val = 0
        
        # max_i_so_far stores the maximum value of nums[x] for x < j.
        # It is updated as we iterate through j.
        # Initialize with nums[0] as it's the first possible 'i' for j=1.
        max_i_so_far = nums[0] 
        
        # Iterate j from 1 to n-2 (inclusive).
        # For a triplet (i, j, k), we must have i < j < k.
        # The smallest possible j is 1 (when i=0).
        # The largest possible j is n-2 (when k=n-1).
        for j in range(1, n - 1):
            # Get the maximum value for nums[k] where k > j.
            # This is available from the precomputed max_right array at index j+1.
            max_k = max_right[j + 1]
            
            # Calculate the value of the current triplet (max_i_so_far, nums[j], max_k).
            # The term (max_i_so_far - nums[j]) can be negative.
            # Since nums[k] is always positive (1 <= nums[i] <= 10^6),
            # the product will be negative if (max_i_so_far - nums[j]) is negative.
            # max_val is initialized to 0 to correctly handle the problem requirement:
            # "If all such triplets have a negative value, return 0."
            current_triplet_value = (max_i_so_far - nums[j]) * max_k
            
            # Update the overall maximum value found so far.
            max_val = max(max_val, current_triplet_value)
            
            # Update max_i_so_far for the next iteration (for j+1).
            # max_i_so_far should always represent the maximum value among nums[0]...nums[j].
            max_i_so_far = max(max_i_so_far, nums[j])
            
        return max_val