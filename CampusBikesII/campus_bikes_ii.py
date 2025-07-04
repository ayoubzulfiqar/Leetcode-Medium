import functools

class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> int:
        N = len(workers)
        M = len(bikes)

        @functools.lru_cache(None)
        def dp(worker_idx: int, bikes_mask: int) -> int:
            if worker_idx == N:
                return 0

            min_total_distance = float('inf')

            for bike_idx in range(M):
                if not (bikes_mask & (1 << bike_idx)):
                    dist = abs(workers[worker_idx][0] - bikes[bike_idx][0]) + \
                           abs(workers[worker_idx][1] - bikes[bike_idx][1])

                    current_total_distance = dist + dp(worker_idx + 1, bikes_mask | (1 << bike_idx))
                    
                    min_total_distance = min(min_total_distance, current_total_distance)
            
            return min_total_distance

        return dp(0, 0)