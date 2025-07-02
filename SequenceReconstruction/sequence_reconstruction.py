import collections

class Solution:
    def sequenceReconstruction(self, org: list[int], seqs: list[list[int]]) -> bool:
        if not org:
            return not seqs or all(not s for s in seqs)

        adj = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)

        org_set = set(org)
        
        for seq in seqs:
            for i in range(len(seq)):
                num = seq[i]
                if num not in org_set:
                    return False

                in_degree[num] 

                if i > 0:
                    prev_num = seq[i-1]
                    adj[prev_num].append(num)
                    in_degree[num] += 1

        q = collections.deque()
        for num in in_degree:
            if in_degree[num] == 0:
                q.append(num)

        reconstructed_sequence = []

        while q:
            if len(q) > 1:
                return False

            u = q.popleft()
            reconstructed_sequence.append(u)

            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        
        return reconstructed_sequence == org