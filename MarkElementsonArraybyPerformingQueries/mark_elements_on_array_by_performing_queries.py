import heapq

class Solution:
    def unmarkedSumArray(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        marked = [False] * n
        current_sum = sum(nums)
        answer = []

        pq = []
        for i in range(n):
            heapq.heappush(pq, (nums[i], i))

        for query_idx, k_val in queries:
            if not marked[query_idx]:
                marked[query_idx] = True
                current_sum -= nums[query_idx]

            count_marked_by_k = 0
            while count_marked_by_k < k_val and pq:
                val, original_idx = heapq.heappop(pq)
                if not marked[original_idx]:
                    marked[original_idx] = True
                    current_sum -= val
                    count_marked_by_k += 1
            
            answer.append(current_sum)

        return answer