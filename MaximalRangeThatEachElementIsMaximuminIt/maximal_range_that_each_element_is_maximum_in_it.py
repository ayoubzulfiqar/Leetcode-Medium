class Solution:
    def maximalRange(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        ngel = [-1] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                ngel[i] = stack[-1]
            stack.append(i)

        nger = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack