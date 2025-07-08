class FenwickTree:
    def __init__(self, size):
        # Fenwick tree (BIT) is 1-indexed internally
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, idx, val):
        # Convert 0-based index to 1-based
        idx += 1
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & (-idx)

    def query(self, idx):
        # Query sum from 0-based index 0 up to idx (inclusive)
        # Convert 0-based index to 1-based
        idx += 1
        s = 0
        # Handle cases where idx becomes 0 or negative after conversion
        # The loop condition `idx > 0` correctly handles this.
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s

class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Transform the problem:
        # Replace 0s with -1s. Now we need to count subarrays where the sum is > 0.
        # Let prefix_sum[i] be the sum of the transformed array up to index i-1.
        # We are looking for pairs (i, j) such that prefix_sum[j+1] - prefix_sum[i] > 0
        # which means prefix_sum[j+1] > prefix_sum[i].
        
        # The range of prefix sums can be from -n to n.
        # To use a Fenwick Tree, we need to map these sums to non-negative indices.
        # We use an offset: map sum_val to sum_val + offset.
        # A good offset is 'n' itself, so -n maps to 0, 0 maps to n, and n maps to 2n.
        offset = n
        
        # The Fenwick Tree size needs to cover the range [0, 2n].
        # So, size is 2n + 1.
        ft_size = 2 * n + 1
        ft = FenwickTree(ft_size)
        
        count = 0
        current_sum = 0 # Represents the prefix sum up to the current element being processed.
                        # This is equivalent to prefix_sum[j+1] in the explanation above.
        
        # Initialize the Fenwick Tree with the sum before any elements, which is 0.
        # This corresponds to prefix_sum[0] = 0.
        # We add 1 to the frequency of this sum.
        ft.update(current_sum + offset, 1)
        
        for num in nums:
            # Update current_sum based on the transformed value of num
            if num == 0:
                current_sum -= 1
            else: # num == 1
                current_sum += 1
            
            # We need to count how many previous prefix sums 'P' satisfy current_sum > P.
            # This is equivalent to counting previous 'P' such that P <= current_sum - 1.
            # We query the Fenwick Tree for the sum of frequencies up to the mapped index of (current_sum - 1).
            count += ft.query(current_sum - 1 + offset)
            
            # Add the current_sum to the Fenwick Tree, incrementing its frequency.
            ft.update(current_sum + offset, 1)
            
        return count