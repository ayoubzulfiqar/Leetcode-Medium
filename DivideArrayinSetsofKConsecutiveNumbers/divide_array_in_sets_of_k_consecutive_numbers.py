import collections

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        if n % k != 0:
            return False

        counts = collections.Counter(nums)

        sorted_unique_nums = sorted(counts.keys())

        for num in sorted_unique_nums:
            if counts[num] == 0:
                continue

            required_count = counts[num]

            for i in range(k):
                current_val = num + i
                
                if counts[current_val] < required_count:
                    return False

                counts[current_val] -= required_count
        
        return True