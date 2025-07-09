class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positives = []
        negatives = []
        
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        
        rearranged_nums = []
        # Since nums has an equal number of positive and negative integers,
        # len(positives) will be equal to len(negatives).
        # And nums.length is even, so len(positives) = nums.length / 2.
        n = len(positives) 
        
        for i in range(n):
            rearranged_nums.append(positives[i])
            rearranged_nums.append(negatives[i])
            
        return rearranged_nums