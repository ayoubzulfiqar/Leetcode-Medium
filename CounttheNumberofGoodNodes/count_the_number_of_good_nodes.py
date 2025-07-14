class Solution:
    def countGoodNodes(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        good_nodes_count = 0

        def dfs(u, parent):
            nonlocal good_nodes_count
            
            child_subtree_sizes = []
            current_subtree_size = 1

            for v in adj[u]:
                if v == parent:
                    continue
                
                child_size = dfs(v, u)
                current_subtree_size += child_size
                child_subtree_sizes.append(child_size)
            
            if not child_subtree_sizes:
                good_nodes_count += 1
            else:
                if len(set(child_subtree_sizes)) == 1:
                    good_nodes_count += 1
            
            return current_subtree_size

        dfs(0, -1)
        
        return good_nodes_count