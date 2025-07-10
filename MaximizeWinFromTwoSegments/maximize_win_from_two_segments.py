class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        n = len(prizePositions)
        
        # left_max_prizes[i] stores the maximum number of prizes obtainable by
        # a single segment of length k, where the segment ends at or before prizePositions[i].
        left_max_prizes = [0] * n
        
        left_ptr = 0
        current_max_prizes_for_prefix = 0
        
        for right_ptr in range(n):
            # Shrink window from the left if its length exceeds k
            while prizePositions[right_ptr] - prizePositions[left_ptr] > k: