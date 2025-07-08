class Solution:
    def maximumInvitations(self, qualifications: list[list[int]]) -> int:
        num_people = len(qualifications)
        if num_people == 0:
            return 0
        num_invitations = len(qualifications[0])
        if num_invitations == 0:
            return 0

        # Build the graph where graph[i] contains a list of invitation indices
        # that person i is qualified for.
        graph = [[] for _ in range(num_people)]
        for i in range(num_people):
            for j in range(num_invitations):
                if qualifications[i][j] == 1:
                    graph[i].append(j)

        # match_R[j] stores the person 'i' who accepted invitation 'j'.
        # Initialize with -1, indicating no invitation is accepted yet.
        match_R = [-1] * num_invitations

        # Stores the maximum number of accepted invitations.
        result = 0

        # Iterate through each person to find an augmenting path.
        # If an augmenting path is found for a person, it means we can increase
        # the number of accepted invitations by 1.
        for person_idx in range(num_people):
            # visited array to keep track of people visited in the current DFS path
            # to avoid cycles and redundant work within a single path search.
            visited = [False] * num_people
            if self._dfs_match(person_idx, graph, match_R, visited):
                result += 1
        
        return result

    # Helper function for DFS-based bipartite matching.
    # It attempts to find an augmenting path starting from person 'u'.
    # u: current person index
    # graph: adjacency list representing qualifications
    # match_R: current matching state (invitation index -> person index)
    # visited: boolean array to track visited people in the current DFS path
    def _dfs_match(self, u: int, graph: list[list[int]], match_R: list[int], visited: list[bool]) -> bool:
        # Mark the current person as visited in this DFS path.
        visited[u] = True

        # Try to match person 'u' with an invitation 'v'.
        for v in graph[u]:
            # If invitation 'v' is not matched (match_R[v] == -1) OR
            # If 'v' is matched to 'prev_u' (match_R[v] != -1) AND
            # 'prev_u' has not been visited in the current DFS path AND
            # 'prev_u' can find an alternative match (by recursively calling _dfs_match).
            if match_R[v] == -1 or (not visited[match_R[v]] and self._dfs_match(match_R[v], graph, match_R, visited)):
                match_R[v] = u  # Match 'u' with 'v'
                return True     # An augmenting path is found
        
        # No augmenting path found for person 'u' from any of their qualified invitations.
        return False