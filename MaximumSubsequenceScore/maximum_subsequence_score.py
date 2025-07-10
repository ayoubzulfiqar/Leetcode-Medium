import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = []
        for i in range(len(nums1)):
            pairs.append((nums2[i], nums1[i]))

        pairs.sort(key=lambda x: x[0], reverse=True)

        current_sum_nums1 = 0
        min_heap = []
        max_score = 0

        for v, u in pairs:
            current_sum_nums1 += u
            heapq.heappush(min_heap, u)

            if len(min_heap) > k:
                smallest_u = heapq.heappop(min_heap)
                current_sum_nums1 -= smallest_u
            
            if len(min_heap) == k:
                score = current_sum_nums1 * v
                max_score = max(max_score, score)

        return max_score