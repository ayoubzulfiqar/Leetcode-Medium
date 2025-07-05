class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        max_len = 0
        pos_len = 0  # length of the longest subarray ending at current index with positive product
        neg_len = 0  # length of the longest subarray ending at current index with negative product

        for num in nums:
            if num == 0:
                pos_len = 0
                neg_len = 0
            elif num > 0:
                pos_len += 1
                if neg_len > 0:
                    neg_len += 1
                else:
                    neg_len = 0
            else:  # num < 0
                # To calculate new pos_len, we need to use old neg_len
                # To calculate new neg_len, we need to use old pos_len
                # So, store old pos_len before it's potentially overwritten
                temp_pos_len = pos_len 
                
                if neg_len > 0:
                    pos_len = neg_len + 1
                else:
                    pos_len = 0 
                
                neg_len = temp_pos_len + 1
            
            max_len = max(max_len, pos_len)
            
        return max_len