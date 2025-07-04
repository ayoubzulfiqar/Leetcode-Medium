class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        max_val_flipped = 0
        count = 0
        for k in range(len(flips)):
            current_flip_index = flips[k]
            max_val_flipped = max(max_val_flipped, current_flip_index)
            if max_val_flipped == (k + 1):
                count += 1
        return count