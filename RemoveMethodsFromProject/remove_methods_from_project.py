import collections

class Solution:
    def removeMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        adj = collections.defaultdict(list)
        rev_adj = collections.defaultdict(list)

        for u, v in invocations:
            adj[u].append(v)
            rev_adj[v].append(u)

        suspicious_methods = set()
        q = collections.deque()

        suspicious_methods.add(k)
        q.append(k)

        while q:
            current_method = q.popleft()
            for invoked_method in adj[current_method]:
                if invoked_method not in suspicious_methods:
                    suspicious_methods.add(invoked_method)
                    q.append(invoked_method)

        can_remove = True
        for sm in suspicious_methods:
            for invoker in rev_adj[sm]:
                if invoker not in suspicious_methods:
                    can_remove = False
                    break
            if not can_remove:
                break

        if not can_remove:
            return list(range(n))
        else:
            remaining_methods = []
            for i in range(n):
                if i not in suspicious_methods:
                    remaining_methods.append(i)
            return remaining_methods

