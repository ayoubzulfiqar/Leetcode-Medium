def countSelfDivisiblePermutations(n: int) -> int:
    count = 0
    visited = [False] * (n + 1)

    def backtrack(k):
        nonlocal count
        if k > n:
            count += 1
            return

        for num in range(1, n + 1):
            if not visited[num]:
                if num % k == 0 or k % num == 0:
                    visited[num] = True
                    backtrack(k + 1)
                    visited[num] = False

    backtrack(1)
    return count