from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minOperationsToSort(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total_swaps = 0
        q = deque([root])

        while q:
            level_size = len(q)
            current_level_values = []
            for _ in range(level_size):
                node = q.popleft()
                current_level_values.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if len(current_level_values) > 1:
                total_swaps += self._min_swaps_to_sort(current_level_values)

        return total_swaps

    def _min_swaps_to_sort(self, arr: list[int]) -> int:
        n = len(arr)
        
        if n <= 1:
            return 0

        val_to_idx = {val: i for i, val in enumerate(arr)}
        
        sorted_arr = sorted(arr)

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i] == sorted_arr[i]:
                continue

            cycle_size = 0
            current_idx = i

            while not visited[current_idx]:
                visited[current_idx] = True
                cycle_size += 1
                
                correct_value_for_current_idx = sorted_arr[current_idx]
                
                next_idx = val_to_idx[correct_value_for_current_idx]
                
                current_idx = next_idx

            swaps += (cycle_size - 1)
        
        return swaps