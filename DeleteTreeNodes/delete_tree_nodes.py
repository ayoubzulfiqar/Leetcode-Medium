class Solution:
    def deleteTreeNodes(self, n: int, parent: list[int], value: list[int]) -> int:
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        def dfs(node_idx: int) -> tuple[int, int]:
            current_sum = value[node_idx]
            current_count = 1

            for child_idx in adj[node_idx]:
                child_sum, child_count = dfs(child_idx)
                current_sum += child_sum
                current_count += child_count
            
            if current_sum == 0:
                return (0, 0)
            else:
                return (current_sum, current_count)

        _, total_kept_nodes = dfs(0)
        
        return total_kept_nodes