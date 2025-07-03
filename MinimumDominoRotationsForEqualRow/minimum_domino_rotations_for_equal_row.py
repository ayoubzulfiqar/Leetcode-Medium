import math

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)

        def check(target_val: int) -> int:
            rotations_for_tops = 0
            rotations_for_bottoms = 0

            for i in range(n):
                if tops[i] != target_val and bottoms[i] != target_val:
                    return float('inf')

                if tops[i] != target_val:
                    rotations_for_tops += 1

                if bottoms[i] != target_val:
                    rotations_for_bottoms += 1
            
            return min(rotations_for_tops, rotations_for_bottoms)

        min_overall_rotations = float('inf')
        
        # A valid target value must be present in the first domino.
        # So, we only need to check tops[0] and bottoms[0] as potential target values.
        candidates = {tops[0], bottoms[0]}

        for target_val in candidates:
            min_overall_rotations = min(min_overall_rotations, check(target_val))

        if min_overall_rotations == float('inf'):
            return -1
        else:
            return min_overall_rotations