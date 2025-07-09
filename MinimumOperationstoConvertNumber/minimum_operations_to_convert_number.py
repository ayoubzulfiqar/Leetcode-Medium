import collections

class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        queue = collections.deque([(start, 0)])
        visited = set()

        if 0 <= start <= 1000:
            visited.add(start)

        while queue:
            current_x, steps = queue.popleft()

            if current_x == goal:
                return steps
            
            if not (0 <= current_x <= 1000):
                continue

            for num in nums:
                next_states = [
                    current_x + num,
                    current_x - num,
                    current_x ^ num
                ]

                for next_x in next_states:
                    if next_x == goal:
                        return steps + 1

                    if 0 <= next_x <= 1000:
                        if next_x not in visited:
                            visited.add(next_x)
                            queue.append((next_x, steps + 1))
        
        return -1