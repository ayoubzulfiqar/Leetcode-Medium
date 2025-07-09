class Solution:
    def edgeScore(self, edges: list[int]) -> int:
        n = len(edges)
        scores = [0] * n

        for i in range(n):
            target_node = edges[i]
            scores[target_node] += i
        
        max_score = -1
        best_node = -1

        for i in range(n):
            if scores[i] > max_score:
                max_score = scores[i]
                best_node = i
            elif scores[i] == max_score:
                # If scores are equal, we want the node with the smallest index.
                # Since we iterate from i=0 upwards, best_node will naturally
                # hold the smallest index for a given max_score.
                # No action needed here as i will be greater than current best_node
                # if it's a different node with the same score.
                pass
        
        return best_node