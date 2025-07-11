class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)

        def count_pairs_less_than_or_equal(target: int) -> int:
            count = 0
            right = n - 1
            
            for left in range(n):
                while right > left and nums[left] + nums[right] > target:
                    right -= 1
                
                if right <= left:
                    break
                
                count += (right - left)
            return count

        count_upper = count_pairs_less_than_or_equal(upper)
        count_lower_minus_1 = count_pairs_less_than_or_equal(lower - 1)
        
        return count_upper - count_lower_minus_1