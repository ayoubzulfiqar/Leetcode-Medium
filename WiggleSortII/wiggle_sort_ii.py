class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        n = len(nums)
        
        sorted_nums = sorted(nums)
        
        ans = [0] * n
        
        mid_idx = (n - 1) // 2 
        
        small_ptr = mid_idx
        large_ptr = n - 1   
        
        for i in range(1, n, 2):
            ans[i] = sorted_nums[large_ptr]
            large_ptr -= 1
            
        for i in range(0, n, 2):
            ans[i] = sorted_nums[small_ptr]
            small_ptr -= 1
            
        nums[:] = ans