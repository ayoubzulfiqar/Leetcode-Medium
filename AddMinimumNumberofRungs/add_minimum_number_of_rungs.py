class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        added_rungs = 0
        current_height = 0

        for rung in rungs:
            gap = rung - current_height
            if gap > dist:
                num_needed = (gap - 1) // dist
                added_rungs += num_needed
            current_height = rung
        
        return added_rungs