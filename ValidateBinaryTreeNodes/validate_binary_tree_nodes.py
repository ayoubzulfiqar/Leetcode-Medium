import collections

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        indegree = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1

        root = -1
        for i in range(n):
            if indegree[i] == 0:
                if root != -1:
                    return False
                root = i
            elif indegree[i] > 1:
                return False
        
        if root == -1:
            return False

        q = collections.deque([root])
        visited_count = 0
        visited = [False] * n

        visited[root] = True
        visited_count += 1

        while q:
            node = q.popleft()
            
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if visited[child]:
                        return False
                    
                    visited[child] = True
                    visited_count += 1
                    q.append(child)
        
        return visited_count == n