class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> list[int]:
        num_workers = len(workers)
        num_bikes = len(bikes)

        all_distances = []

        for i in range(num_workers):
            for j in range(num_bikes):
                dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                all_distances.append((dist, i, j))

        all_distances.sort()

        assignments = [-1] * num_workers
        bikes_assigned = [False] * num_bikes
        assigned_workers_count = 0

        for dist, worker_idx, bike_idx in all_distances:
            if assignments[worker_idx] == -1 and not bikes_assigned[bike_idx]:
                assignments[worker_idx] = bike_idx
                bikes_assigned[bike_idx] = True
                assigned_workers_count += 1

            if assigned_workers_count == num_workers:
                break

        return assignments