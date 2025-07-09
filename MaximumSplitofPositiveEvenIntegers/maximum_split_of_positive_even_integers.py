class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        if finalSum % 2 != 0:
            return []

        result = []
        current_num = 2
        
        while finalSum >= current_num:
            result.append(current_num)
            finalSum -= current_num
            current_num += 2
        
        if finalSum > 0:
            result[-1] += finalSum
            
        return result