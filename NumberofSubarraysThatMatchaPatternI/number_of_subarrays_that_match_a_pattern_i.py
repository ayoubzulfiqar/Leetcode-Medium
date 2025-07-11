class Solution:
    def patternMatching(self, nums: list[int], pattern: list[int]) -> int:
        n = len(nums)
        m = len(pattern)
        count = 0

        for i in range(n - m):
            is_match = True
            for k in range(m):
                val1 = nums[i + k]
                val2 = nums[i + k + 1]
                
                if pattern[k] == 1:
                    if not (val2 > val1):
                        is_match = False
                        break
                elif pattern[k] == 0:
                    if not (val2 == val1):
                        is_match = False
                        break
                elif pattern[k] == -1:
                    if not (val2 < val1):
                        is_match = False
                        break
            
            if is_match:
                count += 1
                
        return count