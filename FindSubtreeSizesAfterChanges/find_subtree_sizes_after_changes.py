import sys

class Solution:
    def getSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        sys.setrecursionlimit(n + 100)

        adj_initial = [[] for _ in range(n)]
        for i in range(1, n):
            adj_initial[parent[i]].append(i)

        new_parents = list(parent)

        last_ancestor_with_char = [-1] * 26

        def dfs_find_new_parents(u):
            char_u_idx = ord(s[u]) - ord('a')

            if last_ancestor_with_char[char_u_idx] != -1:
                new_parents[u] = last_ancestor_with_char[char_u_idx]

            prev_ancestor_for_char_u = last_ancestor_with_char[char_u_idx]

            last_ancestor_with_char[char_u_idx] = u

            for v in adj_initial[u]:
                dfs_find_new_parents(v)

            last_ancestor_with_char[char_u_idx] = prev_ancestor_for_char_u

        dfs_find_new_parents(0)

        adj_final = [[] for _ in range(n)]
        for i in range(1, n):
            adj_final[new_parents[i]].append(i)

        answer = [0] * n

        def dfs_calculate_sizes(u):
            current_subtree_size = 1
            for v in adj_final[u]:
                current_subtree_size += dfs_calculate_sizes(v)
            answer[u] = current_subtree_size
            return current_subtree_size

        dfs_calculate_sizes(0)

        return answer