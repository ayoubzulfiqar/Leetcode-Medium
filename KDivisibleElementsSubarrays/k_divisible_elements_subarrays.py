class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        distinct_subarrays = set()
        n = len(nums)

        for i in range(n):
            current_divisible_count = 0
            current_subarray_elements = [] 
            for j in range(i, n):
                current_subarray_elements.append(nums[j])
                if nums[j] % p == 0:
                    current_divisible_count += 1
                
                if current_divisible_count <= k:
                    distinct_subarrays.add(tuple(current_subarray_elements))
                else:
                    break
        
        return len(distinct_subarrays)