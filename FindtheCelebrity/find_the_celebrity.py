_knows_matrix_global = []

def knows(a: int, b: int) -> bool:
    return _knows_matrix_global[a][b]

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        
        return candidate

# Example usage (for testing, not part of the strict output, but to make it runnable)
# To make the solution self-contained and runnable for a specific test case,
# the _knows_matrix_global must be set.
# In a typical competitive programming environment, the 'knows' function
# would be provided externally and would query a hidden graph.

# Example 1: Celebrity exists (person 1 is the celebrity)
# N = 4
# _knows_matrix_global = [
#     [0, 1, 0, 0],  # 0 knows 1
#     [0, 0, 0, 0],  # 1 knows nobody
#     [0, 1, 0, 0],  # 2 knows 1
#     [0, 1, 0, 0]   # 3 knows 1
# ]
# sol = Solution()
# print(sol.findCelebrity(N)) # Expected output: 1

# Example 2: No celebrity
# N = 3
# _knows_matrix_global = [
#     [0, 1, 0], # 0 knows 1
#     [0, 0, 1], # 1 knows 2
#     [0, 0, 0]  # 2 knows nobody
# ]
# sol = Solution()
# print(sol.findCelebrity(N)) # Expected output: -1

# Example 3: Single person (always a celebrity)
# N = 1
# _knows_matrix_global = [
#     [0]
# ]
# sol = Solution()
# print(sol.findCelebrity(N)) # Expected output: 0
