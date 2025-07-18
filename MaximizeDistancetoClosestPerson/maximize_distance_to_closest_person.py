class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        max_dist = 0
        last_person_idx = -1

        for i in range(n):
            if seats[i] == 1:
                if last_person_idx == -1:
                    max_dist = max(max_dist, i)
                else:
                    max_dist = max(max_dist, (i - last_person_idx) // 2)
                last_person_idx = i

        max_dist = max(max_dist, (n - 1) - last_person_idx)

        return max_dist