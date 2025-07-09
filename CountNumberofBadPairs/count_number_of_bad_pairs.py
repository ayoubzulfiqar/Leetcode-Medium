class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Total possible pairs (i, j) where i < j
        # This is the sum of integers from 1 to n-1, which is (n-1)*n/2
        total_pairs = n * (n - 1) // 2
        
        # A pair (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
        # This inequality can be rewritten as:
        # j - nums[j] != i - nums[i]
        
        # Conversely, a pair (i, j) is a "good pair" if i < j and j - i == nums[j] - nums[i].
        # This equality can be rewritten as:
        # j - nums[j] == i - nums[i]
        
        # We will count the number of good pairs and subtract it from the total number of pairs.
        
        good_pairs_count = 0
        
        # Use a dictionary to store the frequency of (k - nums[k]) values.
        # For each index k, we calculate 'val_k = k - nums[k]'.
        # If 'val_k' has appeared 'm' times before (at indices i < k),
        # then 'm' good pairs (i, k) are formed with the current k.
        val_counts = {} 
        
        for k in range(n):
            current_val = k - nums[k]
            
            # If current_val has been seen before, add its count to good_pairs_count.
            # If not seen, val_counts.get(current_val, 0) will return 0, adding nothing.
            good_pairs_count += val_counts.get(current_val, 0)
            
            # Increment the count for the current_val.
            val_counts[current_val] = val_counts.get(current_val, 0) + 1
            
        # The number of bad pairs is the total possible pairs minus the good pairs.
        bad_pairs = total_pairs - good_pairs_count
        
        return bad_pairs