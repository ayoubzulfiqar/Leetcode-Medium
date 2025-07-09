import bisect

class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        
        plate_prefix_sum = [0] * n
        current_plates = 0
        for i in range(n):
            if s[i] == '*':
                current_plates += 1
            plate_prefix_sum[i] = current_plates
            
        candle_indices = []
        for i in range(n):
            if s[i] == '|':
                candle_indices.append(i)
                
        results = []
        for left, right in queries:
            idx1 = bisect.bisect_left(candle_indices, left)
            idx2 = bisect.bisect_right(candle_indices, right) - 1
            
            if idx1 >= len(candle_indices) or idx2 < 0 or idx1 >= idx2:
                results.append(0)
            else:
                first_candle_actual_idx = candle_indices[idx1]
                last_candle_actual_idx = candle_indices[idx2]
                
                start_plate_range = first_candle_actual_idx + 1
                end_plate_range = last_candle_actual_idx - 1
                
                count = plate_prefix_sum