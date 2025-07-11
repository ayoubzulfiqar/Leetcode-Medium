class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        num_chars = 26
        infinity = float('inf')
        
        dist = [[infinity] * num_chars for _ in range(num_chars)]
        
        for i in range(num_chars):
            dist[i][i] = 0
            
        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            c = cost[i]
            dist[u][v] = min(dist[u][v], c)
            
        for k in range(num_chars):
            for i in range(num_chars):
                for j in range(num_chars):
                    if dist[i][k] != infinity and dist[k][j] != infinity:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                        
        total_cost = 0
        for i in range(len(source)):
            s_char_idx = ord(source[i]) - ord('a')
            t_char_idx = ord(target[i]) - ord('a')
            
            if s_char_idx == t_char_idx:
                continue
            
            conversion_cost = dist[s_char_idx][t_char_idx]
            
            if conversion_cost == infinity:
                return -1
            
            total_cost += conversion_cost
            
        return total_cost