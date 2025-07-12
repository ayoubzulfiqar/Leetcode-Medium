class Solution:
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        total_count = 0
        current_length = 0
        n = len(nums)

        for i in range(n):
            if i == 0:
                # The first element always starts an alternating subarray of length 1
                current_length = 1
            elif nums[i] != nums[i-1]:
                # If the current element is different from the previous,
                # it extends the current alternating sequence
                current_length += 1
            else: # nums[i] == nums[i-1]
                # If the current element is the same as the previous,
                # the alternating sequence is broken.
                # A new alternating sequence starts with the current element, so length is 1.
                current_length = 1
            
            # All subarrays ending at 'i' that are alternating contribute to the count.
            # There are 'current_length' such subarrays:
            # [nums[i]], [nums[i-1], nums[i]], ..., [nums[i-current_length+1], ..., nums[i]]
            total_count += current_length
            
        return total_count