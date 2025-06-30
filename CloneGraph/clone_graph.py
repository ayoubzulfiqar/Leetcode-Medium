import collections

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visited = {}
        q = collections.deque()

        cloned_head = Node(node.val)
        visited[node] = cloned_head
        q.append(node)

        while q:
            original_curr = q.popleft()
            cloned_curr = visited[original_curr]

            for original_neighbor in original_curr.neighbors:
                if original_neighbor not in visited:
                    cloned_neighbor = Node(original_neighbor.val)
                    visited[original_neighbor] = cloned_neighbor
                    cloned_curr.neighbors.append(cloned_neighbor)
                    q.append(original_neighbor)
                else:
                    cloned_curr.neighbors.append(visited[original_neighbor])
        
        return cloned_head