import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        heap_left = []  # Stores (cost, original_index) for workers from the left
        heap_right = [] # Stores (cost, original_index) for workers from the right
        
        total_cost = 0
        
        left_ptr = 0
        right_ptr = n - 1
        
        # Populate initial heaps with 'candidates' workers from each end
        # Ensure workers are not duplicated if left and right ranges overlap
        while len(heap_left) < candidates and left_ptr <= right_ptr:
            heapq.heappush(heap_left, (costs[left_ptr], left_ptr))
            left_ptr += 1
            
        while len(heap_right) < candidates and left_ptr <= right_ptr:
            heapq.heappush(heap_right, (costs[right_ptr], right_ptr))
            right_ptr -= 1
            
        # Hire k workers
        for _ in range(k):
            # Case 1: Both heaps have workers
            if heap_left and heap_right:
                cost_l, idx_l = heap_left[0]
                cost_r, idx_r = heap_right[0]
                
                # Choose worker with lowest cost, tie-break by smallest index
                if cost_l <= cost_r:
                    chosen_cost, chosen_idx = heapq.heappop(heap_left)
                    total_cost += chosen_cost
                    # Replenish heap_left if there are still workers available
                    if left_ptr <= right_ptr:
                        heapq.heappush(heap_left, (costs[left_ptr], left_ptr))
                        left_ptr += 1
                else: # cost_r < cost_l
                    chosen_cost, chosen_idx = heapq.heappop(heap_right)
                    total_cost += chosen_cost
                    # Replenish heap_right if there are still workers available
                    if left_ptr <= right_ptr:
                        heapq.heappush(heap_right, (costs[right_ptr], right_ptr))
                        right_ptr -= 1
            # Case 2: Only heap_left has workers (heap_right is empty)
            elif heap_left:
                chosen_cost, chosen_idx = heapq.heappop(heap_left)
                total_cost += chosen_cost
                # Replenish heap_left if there are still workers available
                if left_ptr <= right_ptr:
                    heapq.heappush(heap_left, (costs[left_ptr], left_ptr))
                    left_ptr += 1
            # Case 3: Only heap_right has workers (heap_left is empty)
            elif heap_right:
                chosen_cost, chosen_idx = heapq.heappop(heap_right)
                total_cost += chosen_cost
                # Replenish heap_right if there are still workers available
                if left_ptr <= right_ptr:
                    heapq.heappush(heap_right, (costs[right_ptr], right_ptr))
                    right_ptr -= 1
            # Case 4: Both heaps are empty (should not happen based on constraints k <= n)
            else:
                break 

        return total_cost