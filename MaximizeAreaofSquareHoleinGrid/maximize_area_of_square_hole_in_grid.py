class Solution:
    def maximizeSquareHole(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        
        def get_max_consecutive_length(bars: list[int]) -> int:
            if not bars:
                return 0
            
            bars.sort()
            
            max_consecutive = 1
            current_consecutive = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_consecutive += 1
                else:
                    current_consecutive = 1
                max_consecutive = max(max_consecutive, current_consecutive)
            
            return max_consecutive
        
        # The side length of a square hole is determined by the number of consecutive bars that can be removed.
        # If 'k' consecutive bars can be removed (e.g., bars x, x+1, ..., x+k-1),
        # these removed bars create an open space between bar x-1 and bar x+k.
        # The width of this open space is (x+k) - (x-1) = k+1 units.
        # So, if we can remove 'k' consecutive bars, we can form a hole of side length 'k+1'.
        # If no bars can be removed (or bars list is empty), k=0, leading to a side length of 1 (a 1x1 cell).
        
        max_h_removable_consecutive = get_max_consecutive_length(hBars)
        max_v_removable_consecutive = get_max_consecutive_length(vBars)
        
        max_h_side = max_h_removable_consecutive + 1
        max_v_side = max_v_removable_consecutive + 1
        
        # The side of the largest square hole is limited by the minimum of the maximum possible horizontal
        # and vertical side lengths.
        side = min(max_h_side, max_v_side)
        
        return side * side