import collections

def tree_diameter(n, edges):
    if n == 0:
        return 0
    if n == 1:
        return 0

    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def bfs(start_node):
        queue = collections.deque([(start_node, 0)])
        visited = {start_node}
        farthest_node = start_node
        max_dist = 0

        while queue:
            curr_node, curr_dist = queue.popleft()

            if curr_dist > max_dist:
                max_dist = curr_dist
                farthest_node = curr_node

            for neighbor in adj[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, curr_dist + 1))
        return farthest_node, max_dist

    node_A, _ = bfs(0)
    _, diameter = bfs(node_A)

    return diameter