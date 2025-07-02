class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)

        # States for each node:
        # 0: Unvisited
        # 1: Visiting (currently in recursion stack, indicates potential cycle)
        # 2: Safe (all paths from this node lead to terminal nodes or other safe nodes)
        # 3: Unsafe (can reach a cycle or another unsafe node)
        states = [0] * n

        def dfs(node: int) -> bool:
            # If the node's state is already determined
            if states[node] == 2:  # Already determined safe
                return True
            if states[node] == 3:  # Already determined unsafe
                return False
            
            # If we encounter a node that is currently being visited, it means we've found a cycle.
            # This node and all nodes on the current path leading to it are unsafe.
            if states[node] == 1:
                states[node] = 3  # Mark as unsafe
                return False

            # Mark the current node as visiting
            states[node] = 1

            # Recursively check all neighbors
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    # If any neighbor leads to an unsafe path (returns False),
                    # then the current node is also unsafe.
                    states[node] = 3  # Mark as unsafe
                    return False
            
            # If all neighbors lead to safe paths (or are terminal nodes),
            # then the current node is safe.
            states[node] = 2  # Mark as safe
            return True

        safe_nodes = []
        # Iterate through all nodes to ensure all components of the graph are processed.
        # The DFS will mark nodes as safe or unsafe and memoize the results.
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
        
        # The nodes are added to safe_nodes in ascending order because we iterate from 0 to n-1.
        return safe_nodes