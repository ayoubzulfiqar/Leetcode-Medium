class Solution:
    def equalizeWater(self, buckets: list[int], loss: int) -> float:
        n = len(buckets)
        if n == 0:
            return 0.0

        low = 0.0
        high = float(max(buckets))
        
        if sum(buckets) == 0:
            return 0.0

        loss_factor = (100.0 - loss) / 100.0

        for _ in range(100):
            mid = (low + high) / 2.0
            
            water_from_sources = 0.0
            water_needed_by_sinks = 0.0

            for b in buckets:
                if b > mid:
                    water_from_sources += (b - mid)
                else:
                    water_needed_by_sinks += (mid - b)
            
            if water_from_sources * loss_factor >= water_needed_by_sinks:
                low = mid
            else:
                high = mid
        
        return low