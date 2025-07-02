class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.visited = [False] * (n + 1)

        def backtrack(current_pos):
            if current_pos > n:
                self.count += 1
                return

            for num in range(1, n + 1):
                if not self.visited[num]:
                    if num % current_pos == 0 or current_pos % num == 0:
                        self.visited[num] = True
                        backtrack(current_pos + 1)
                        self.visited[num] = False

        backtrack(1)
        return self.count