class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        MOD = 10**9 + 7

        prev_smaller = [-1] * n
        stack = [] 

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        next_smaller = [n] * n
        stack = [] 

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)

        total_sum = 0
        for i in range(n):
            left_count = i - prev_smaller[i]
            right_count = next_smaller[i] - i
            
            contribution = (arr[i] * left_count * right_count) % MOD
            total_sum = (total_sum + contribution) % MOD

        return total_sum