class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(sx - fx)
        dy = abs(sy - fy)

        min_time = max(dx, dy)

        if min_time == 0:
            # If start and end cells are the same
            # If t is 0, we are already there, so True.
            # If t is 1, we must move, so we cannot be at the same cell, False.
            # If t >= 2, we can move away and come back, but only if t is even.
            # (e.g., (sx,sy) -> (sx+1,sy) -> (sx,sy) takes 2 seconds)
            return t == 0 or (t >= 2 and t % 2 == 0)
        else:
            # If start and end cells are different
            # We need at least min_time seconds to reach the target.
            # If t is less than min_time, it's impossible.
            # If t is greater than or equal to min_time, it's always possible.
            # This is because we can always "waste" time by taking a non-optimal path
            # (e.g., converting a single optimal diagonal move into two cardinal moves,
            # which adds 1 second to the path length, or taking a detour and returning to path).
            return t >= min_time