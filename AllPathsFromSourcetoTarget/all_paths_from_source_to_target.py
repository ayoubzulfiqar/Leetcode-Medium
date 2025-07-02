class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        n = len(graph)
        target_node = n - 1
        all_paths = []

        def dfs(current_node, current_path):
            if current_node == target_node:
                all_paths.append(list(current_path))
                return

            for neighbor in graph[current_node]:
                current_path.append(neighbor)
                dfs(neighbor, current_path)
                current_path.pop()

        dfs(0, [0])
        return all_paths