class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        results = []

        def dfs(current_num, length):
            if length == n:
                results.append(current_num)
                return

            last_digit = current_num % 10

            next_digit_plus = last_digit + k
            if 0 <= next_digit_plus <= 9:
                dfs(current_num * 10 + next_digit_plus, length + 1)

            if k > 0:
                next_digit_minus = last_digit - k
                if 0 <= next_digit_minus <= 9:
                    dfs(current_num * 10 + next_digit_minus, length + 1)

        for first_digit in range(1, 10):
            dfs(first_digit, 1)

        return results