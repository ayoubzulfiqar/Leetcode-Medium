class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        max_dist = 0
        last_one_idx = -1

        for i in range(n):
            if seats[i] == 1:
                if last_one_idx == -1:
                    # Case 1: First '1' encountered.
                    # The distance from the beginning of the seats (index 0) to this '1'
                    # is a potential maximum distance.
                    max_dist = max(max_dist, i)
                else:
                    # Case 2: Subsequent '1' encountered.
                    # Calculate the length of the empty segment between this '1' and the previous '1'.
                    # The optimal seat in this segment is in the middle, maximizing distance to both sides.
                    # The distance is half of the length of the gap (number of zeros + 1).
                    max_dist = max(max_dist, (i - last_one_idx) // 2)
                last_one_idx = i
        
        # Case 3: Handle the empty segment at the end of the row.
        # The distance from the last '1' found to the very end of the seats (index n-1)
        # is a potential maximum distance.
        max_dist = max(max_dist, (n - 1) - last_one_idx)
        
        return max_dist