import collections

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        counts = collections.Counter(nums)
        operations = 0

        for num in list(counts.keys()): # Iterate over a copy of keys to avoid modification issues
            if counts[num] == 0:
                continue

            complement = k - num

            if complement not in counts or counts[complement] == 0:
                continue

            if num == complement:
                # If the number is its own complement (e.g., k=6, num=3)
                # We can form pairs using two instances of this number.
                operations += counts[num] // 2
                counts[num] = 0 # All instances of this number are now used or cannot form pairs
            else:
                # If num and complement are different
                # We can form min(counts[num], counts[complement]) pairs
                pairs_to_form = min(counts[num], counts[complement])
                operations += pairs_to_form
                counts[num] -= pairs_to_form
                counts[complement] -= pairs_to_form
        
        return operations