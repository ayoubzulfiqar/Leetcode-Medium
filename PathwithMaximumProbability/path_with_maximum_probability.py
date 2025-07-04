import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)
        for i, (u, v) in enumerate(edges):
            prob = succProb[i]
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        probabilities = [0.0] * n
        probabilities[start] = 1.0

        pq = [(-1.0, start)] # Max-heap: stores (-probability, node)

        while pq:
            current_neg_prob, u = heapq.heappop(pq)
            current_prob = -current_neg_prob

            if current_prob < probabilities[u]:
                continue

            for v, edge_prob in adj[u]:
                new_prob = current_prob * edge_prob
                if new_prob > probabilities[v]:
                    probabilities[v] = new_prob
                    heapq.heappush(pq, (-new_prob, v))

        return probabilities[end]