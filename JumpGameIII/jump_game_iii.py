import collections

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        
        queue = collections.deque()
        queue.append(start)
        
        visited = {start}
        
        while queue:
            current_idx = queue.popleft()
            
            if arr[current_idx] == 0:
                return True
            
            next_idx_plus = current_idx + arr[current_idx]
            next_idx_minus = current_idx - arr[current_idx]
            
            if 0 <= next_idx_plus < n and next_idx_plus not in visited:
                visited.add(next_idx_plus)
                queue.append(next_idx_plus)
            
            if 0 <= next_idx_minus < n and next_idx_minus not in visited:
                visited.add(next_idx_minus)
                queue.append(next_idx_minus)
                
        return False