import collections

def max_subtree_same_color(n, parent, colors):
    if n == 0:
        return 0
    if n == 1:
        return 1

    adj = collections.defaultdict(list)
    root = -1
    for i in range(n):
        if parent[i] == -1:
            root = i
        else:
            adj[parent[i]].append(i)

    max_size = [0]

    def dfs(u):
        current_node_uniform_size = 1
        
        for v in adj[u]:
            child_uniform_size = dfs(v)
            
            if colors[v] == colors[u]:
                current_node_uniform_size += child_uniform_size
        
        max_size[0] = max(max_size[0], current_node_uniform_size)
        
        return current_node_uniform_size

    dfs(root)

    return max_size[0]