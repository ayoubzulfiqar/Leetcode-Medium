import collections

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead_set = set(deadends)
        
        if "0000" in dead_set:
            return -1
        
        if target == "0000":
            return 0

        queue = collections.deque([("0000", 0)])
        visited = {"0000"}
        
        def get_neighbors(s: str) -> list[str]:
            neighbors = []
            for i in range(4):
                digit = int(s[i])
                
                forward_digit = str((digit + 1) % 10)
                neighbors.append(s[:i] + forward_digit + s[i+1:])
                
                backward_digit = str((digit - 1 + 10) % 10)
                neighbors.append(s[:i] + backward_digit + s[i+1:])
            return neighbors

        while queue:
            current_combo, steps = queue.popleft()
            
            for next_combo in get_neighbors(current_combo):
                if next_combo == target:
                    return steps + 1
                
                if next_combo not in visited and next_combo not in dead_set:
                    visited.add(next_combo)
                    queue.append((next_combo, steps + 1))
                    
        return -1