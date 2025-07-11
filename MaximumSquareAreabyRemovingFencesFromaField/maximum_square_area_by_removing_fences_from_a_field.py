class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7

        h_coords = sorted(list(set([1, m] + hFences)))
        v_coords = sorted(list(set([1, n] + vFences)))

        h_distances = set()
        for i in range(len(h_coords)):
            for j in range(i + 1, len(h_coords)):
                h_distances.add(h_coords[j] - h_coords[i])

        v_distances = set()
        for i in range(len(v_coords)):
            for j in range(i + 1, len(v_coords)):
                v_distances.add(v_coords[j] - v_coords[i])

        max_side = 0
        for d in h_distances:
            if d in v_distances:
                max_side = max(max_side, d)

        if max_side == 0:
            return -1
        else:
            return (max_side * max_side) % MOD