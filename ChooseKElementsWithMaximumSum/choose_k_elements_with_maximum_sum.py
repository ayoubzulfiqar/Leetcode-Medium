import heapq

class Solution:
    def chooseKElementsWithMaximumSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        n = len(nums1)
        
        items = []
        for i in range(n):
            items.append((nums1[i], nums2[i], i))
        
        items.sort()
        
        answer = [0] * n
        
        min_heap = []
        current_sum = 0
        
        i = 0
        while i < n:
            current_val1 = items[i][0]
            
            j = i
            while j < n and items[j][0] == current_val1:
                original_idx = items[j][2]
                answer[original_idx] = current_sum
                j += 1
            
            for k_idx in range(i, j):
                val2_to_add = items[k_idx][1]
                
                if len(min_heap) < k:
                    heapq.heappush(min_heap, val2_to_add)
                    current_sum += val2_to_add
                elif val2_to_add > min_heap[0]:
                    current_sum -= heapq.heappop(min_heap)
                    heapq.heappush(min_heap, val2_to_add)
                    current_sum += val2_to_add
            
            i = j
            
        return answer