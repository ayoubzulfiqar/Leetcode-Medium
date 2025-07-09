import heapq

class Solution:
    def halveArray(self, nums: list[int]) -> int:
        initial_sum = sum(nums)
        target_sum = initial_sum / 2.0
        
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
            
        current_sum = initial_sum
        operations = 0
        
        while current_sum > target_sum:
            largest_num = -heapq.heappop(max_heap)
            
            reduced_num = largest_num / 2.0
            
            current_sum -= reduced_num
            
            heapq.heappush(max_heap, -reduced_num)
            
            operations += 1
            
        return operations