import collections

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n = len(amount)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Determine Bob's path and arrival times
        # parent_map[node] stores the parent of 'node' when traversing from 'bob' towards '0'.
        # This is used to reconstruct the unique path from '0' to 'bob'.
        parent_map = {} 
        q_bob = collections.deque([(bob, 0)]) # (node, distance_from_bob)
        visited_bob = {bob}
        
        path_from_bob_to_0 = []
        
        # BFS to find the path from bob to 0 and store parent pointers
        while q_bob:
            curr, dist = q_bob.popleft()
            
            if curr == 0:
                # Reconstruct path from 0 back to bob using parent_map
                temp_path = []
                node = 0
                while node != bob:
                    temp_path.append(node)
                    node = parent_map[node]
                temp_path.append(bob)
                path_from_bob_to_0 = temp_path[::-1] # Reverse to get bob -> ... -> 0
                break
            
            for neighbor in adj[curr]:
                if neighbor not in visited_bob:
                    visited_bob.add(neighbor)
                    parent_map[neighbor] = curr # Store parent for path reconstruction
                    q_bob.append((neighbor, dist + 1))
        
        # Populate bob_path_info: node -> time Bob arrives at that node
        bob_path_info = {} 
        for i, node in enumerate(path_from_bob_to_0):
            bob_path_info[node] = i

        # 2. Alice's DFS to find maximum income
        max_alice_income = -float('inf')

        def dfs(u, p, alice_time, current_income):
            nonlocal max_alice_income

            # Calculate income for current node u
            node_income = amount[u]
            if u in bob_path_info:
                bob_arrival_time = bob_path_info[u]
                if alice_time < bob_arrival_time:
                    # Alice arrives first, gets full amount
                    pass 
                elif alice_time == bob_arrival_time:
                    # Alice and Bob arrive simultaneously, share
                    node_income //= 2 
                else: # alice_time > bob_arrival_time
                    # Bob arrives first, Alice gets nothing
                    node_income = 0
            
            current_income += node_income

            # Check if u is a leaf node for Alice's path (i.e., no unvisited children)
            is_leaf = True
            for v in adj[u]:
                if v != p: # If v is not the parent, it's a child
                    is_leaf = False
                    dfs(v, u, alice_time + 1, current_income)
            
            # If no children were found (other than the parent), u is a leaf
            if is_leaf:
                max_alice_income = max(max_alice_income, current_income)

        # Start Alice's journey from node 0
        # Initial call: dfs(current_node, parent_node, current_time, current_income)
        dfs(0, -1, 0, 0) 

        return max_alice_income