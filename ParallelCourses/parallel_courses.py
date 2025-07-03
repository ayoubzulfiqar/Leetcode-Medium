import collections

class Solution:
    def minimumMonths(self, n: int, relations: list[list[int]]) -> int:
        adj = collections.defaultdict(list)
        in_degree = [0] * (n + 1)

        for prev_course, next_course in relations:
            adj[prev_course].append(next_course)
            in_degree[next_course] += 1

        time = [1] * (n + 1)
        q = collections.deque()

        for i in range(1, n + 1):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            current_course = q.popleft()

            for next_course in adj[current_course]:
                time[next_course] = max(time[next_course], time[current_course] + 1)
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)

        return max(time)