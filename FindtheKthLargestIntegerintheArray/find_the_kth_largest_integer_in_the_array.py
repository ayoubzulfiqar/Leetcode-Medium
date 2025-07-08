class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        int_nums = []
        for s_num in nums:
            int_nums.append(int(s_num))
        
        int_nums.sort()
        
        kth_largest_int = int_nums[len(int_nums) - k]
        
        return str(kth_largest_int)