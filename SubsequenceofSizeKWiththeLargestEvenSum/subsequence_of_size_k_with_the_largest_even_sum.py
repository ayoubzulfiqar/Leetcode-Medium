class Solution:
    def largestEvenSum(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        
        # If the initial sum of the k largest elements is even, it's the maximum possible.
        if current_sum % 2 == 0:
            return current_sum
        
        # If the sum is odd, we need to modify it to make it even.
        # We have two options to change an odd sum to an even sum:
        # 1. Replace an odd number in the top k with an even number from outside the top k.
        #    To maximize, remove the smallest odd from top k, add largest even from outside top k.
        # 2. Replace an even number in the top k with an odd number from outside the top k.
        #    To maximize, remove the smallest even from top k, add largest odd from outside top k.
        
        max_even_sum = -1
        
        min_odd_in_k = -1
        min_even_in_k = -1
        
        # Find smallest odd and smallest even in the top k elements (nums[0]...nums[k-1])
        # Since nums is sorted descending, the smallest values are at higher indices.
        for i in range(k - 1, -1, -1):
            if nums[i] % 2 != 0: # Odd
                min_odd_in_k = nums[i]
                break
        
        for i in range(k - 1, -1, -1):
            if nums[i] % 2 == 0: # Even
                min_even_in_k = nums[i]
                break

        max_even_out_k = -1
        max_odd_out_k = -1
        
        # Find largest even and largest odd outside the top k elements (nums[k]...nums[len(nums)-1])
        # Since nums is sorted descending, the largest values are at lower indices.
        for i in range(k, len(nums)):
            if nums[i] % 2 == 0: # Even
                max_even_out_k = nums[i]
                break
        
        for i in range(k, len(nums)):
            if nums[i] % 2 != 0: # Odd
                max_odd_out_k = nums[i]
                break

        # Option 1: Replace smallest odd from top k with largest even from outside top k
        if min_odd_in_k != -1 and max_even_out_k != -1:
            max_even_sum = max(max_even_sum, current_sum - min_odd_in_k + max_even_out_k)
            
        # Option 2: Replace smallest even from top k with largest odd from outside top k
        if min_even_in_k != -1 and max_odd_out_k != -1:
            max_even_sum = max(max_even_sum, current_sum - min_even_in_k + max_odd_out_k)
            
        return max_even_sum