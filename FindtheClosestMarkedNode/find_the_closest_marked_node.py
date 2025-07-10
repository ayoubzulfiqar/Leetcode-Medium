import collections

def find_closest_marked_node(graph, start_node, marked_nodes):
    if not graph:
        return -1
    if start_node not in graph:
        return -1
    
    marked_nodes_set = set(marked_nodes)

    if start_node in marked_nodes_set:
        return 0

    queue = collections.deque([(start_node, 0)])
    visited = {start_node}

    while queue:
        current_node, distance = queue.popleft()

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                if neighbor in marked_nodes_set:
                    return distance + 1
                queue.append((neighbor, distance + 1))
    
    return -1