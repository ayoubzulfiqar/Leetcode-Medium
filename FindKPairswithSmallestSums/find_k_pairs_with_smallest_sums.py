import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        m, n = len(nums1), len(nums2)
        
        result = []
        min_heap = []
        
        for i in range(min(m, k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
            
        while k > 0 and min_heap:
            current_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1
            
            if j + 1 < n:
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j + 1))
                
        return result