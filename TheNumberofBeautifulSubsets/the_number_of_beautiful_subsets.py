import collections

class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        nums.sort()

        freq = collections.Counter()
        
        self.count = 0

        def backtrack(index):
            if index == len(nums):
                self.count += 1
                return

            backtrack(index + 1)

            current_num = nums[index]
            
            can_include = (freq.get(current_num - k, 0) == 0) and \
                           (freq.get(current_num + k, 0) == 0)

            if can_include:
                freq[current_num] += 1
                
                backtrack(index + 1)
                
                freq[current_num] -= 1
                
                if freq[current_num] == 0:
                    del freq[current_num]

        backtrack(0)

        return self.count - 1