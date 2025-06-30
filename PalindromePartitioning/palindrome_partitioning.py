class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        current_partition = []
        n = len(s)

        def is_palindrome(sub_s: str) -> bool:
            return sub_s == sub_s[::-1]

        def backtrack(start_index: int):
            if start_index == n:
                result.append(list(current_partition))
                return

            for i in range(start_index, n):
                substring = s[start_index : i + 1]
                if is_palindrome(substring):
                    current_partition.append(substring)
                    backtrack(i + 1)
                    current_partition.pop()

        backtrack(0)
        return result