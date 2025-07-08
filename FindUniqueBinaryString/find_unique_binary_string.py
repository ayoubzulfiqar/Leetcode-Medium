class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        
        result_chars = []
        for i in range(n):
            if nums[i][i] == '0':
                result_chars.append('1')
            else:
                result_chars.append('0')
                
        return "".join(result_chars)