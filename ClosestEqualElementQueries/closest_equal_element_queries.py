import collections
import bisect

class Solution:
    def getClosestEqualElement(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        
        val_indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            val_indices[num].append(i)
            
        answer = []
        for query_idx in queries:
            target_val = nums[query_idx]
            
            indices_list = val_indices[target_val]
            
            if len(indices_list) <= 1:
                answer.append(-1)
                continue
            
            pos = bisect.bisect_left(indices_list, query_idx)
            
            min_dist = float('inf')
            
            prev_idx_in_list = indices_list[(pos - 1 + len(indices_list)) % len(indices_list)]
            next_idx_in_list = indices_list[(pos + 1) % len(indices_list)]
            
            dist_prev = abs(query_idx - prev_idx_in_list)
            min_dist = min(min_dist, min(dist_prev, n - dist_prev))
            
            dist_next = abs(query_idx - next_idx_in_list)
            min_dist = min(min_dist, min(dist_next, n - dist_next))
            
            answer.append(min_dist)
            
        return answer