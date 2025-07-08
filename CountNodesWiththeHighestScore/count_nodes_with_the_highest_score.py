class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        n = len(parents)
        
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
            
        subtree_size = [0] * n
        
        def dfs_calculate_size(node: int) -> int:
            current_size = 1
            for child in children[node]:
                current_size += dfs_calculate_size(child)
            subtree_size[node] = current_size
            return current_size
            
        dfs_calculate_size(0)
        
        max_score = 0
        count_max_score = 0
        
        for i in range(n):
            current_score = 1
            
            for child in children[i]:
                current_score *= subtree_size[child]
            
            size_above = n - subtree_size[i]
            if size_above > 0:
                current_score *= size_above
            
            if current_score > max_score:
                max_score = current_score
                count_max_score = 1
            elif current_score == max_score:
                count_max_score += 1
                
        return count_max_score