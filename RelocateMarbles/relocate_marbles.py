class Solution:
    def relocateMarbles(self, nums: list[int], moveFrom: list[int], moveTo: list[int]) -> list[int]:
        occupied_positions = set(nums)

        for i in range(len(moveFrom)):
            from_pos = moveFrom[i]
            to_pos = moveTo[i]
            
            # The problem guarantees there is at least one marble at moveFrom[i]
            # at the moment of the move, so from_pos will always be in the set.
            occupied_positions.remove(from_pos)
            occupied_positions.add(to_pos)
        
        result = list(occupied_positions)
        result.sort()
        
        return result