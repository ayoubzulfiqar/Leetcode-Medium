class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        length = 2 * n - 1
        ans = [0] * length
        visited = [False] * (n + 1)

        def backtrack(idx: int) -> bool:
            if idx == length:
                return True

            if ans[idx] != 0:
                return backtrack(idx + 1)

            for num in range(n, 0, -1):
                if not visited[num]:
                    if num == 1:
                        ans[idx] = 1
                        visited[1] = True
                        if backtrack(idx + 1):
                            return True
                        visited[1] = False
                        ans[idx] = 0
                    else:
                        if idx + num < length and ans[idx + num] == 0:
                            ans[idx] = num
                            ans[idx + num] = num
                            visited[num] = True
                            if backtrack(idx + 1):
                                return True
                            visited[num] = False
                            ans[idx] = 0
                            ans[idx + num] = 0
            return False

        backtrack(0)
        return ans