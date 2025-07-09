class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        def check(current_time: int) -> bool:
            trips_completed = 0
            for t_val in time:
                trips_completed += current_time // t_val
            return trips_completed >= totalTrips

        left = 1
        right = max(time) * totalTrips
        
        ans = right

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans