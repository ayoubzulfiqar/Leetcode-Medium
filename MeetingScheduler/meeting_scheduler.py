class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        slots1.sort()
        slots2.sort()

        i, j = 0, 0
        
        while i < len(slots1) and j < len(slots2):
            s1_start, s1_end = slots1[i]
            s2_start, s2_end = slots2[j]

            overlap_start = max(s1_start, s2_start)
            overlap_end = min(s1_end, s2_end)

            if overlap_start < overlap_end and (overlap_end - overlap_start) >= duration:
                return [overlap_start, overlap_start + duration]

            if s1_end < s2_end:
                i += 1
            else:
                j += 1
                
        return []