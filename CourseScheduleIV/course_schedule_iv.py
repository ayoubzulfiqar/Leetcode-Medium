class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            is_prerequisite[pre][course] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    is_prerequisite[i][j] = is_prerequisite[i][j] or \
                                            (is_prerequisite[i][k] and is_prerequisite[k][j])
        
        results = []
        for u, v in queries:
            results.append(is_prerequisite[u][v])
        
        return results