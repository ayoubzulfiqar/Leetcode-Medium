import math

class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        n = len(cookies)
        child_sums = [0] * k
        self.min_unfairness = math.inf

        cookies.sort(reverse=True)

        def dfs(bag_idx):
            nonlocal child_sums
            nonlocal self.min_unfairness

            if bag_idx == n:
                self.min_unfairness = min(self.min_unfairness, max(child_sums))
                return

            current_cookie = cookies[bag_idx]

            for i in range(k):
                if child_sums[i] + current_cookie >= self.min_unfairness:
                    continue

                child_sums[i] += current_cookie
                dfs(bag_idx + 1)
                child_sums[i] -= current_cookie

                if child_sums[i] == 0:
                    break

        dfs(0)
        return self.min_unfairness