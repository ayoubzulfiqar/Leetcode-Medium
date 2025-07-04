class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n = len(s1)
        
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)
        
        def can_break_one_way(arr1, arr2):
            for i in range(n):
                if arr1[i] < arr2[i]:
                    return False
            return True
        
        return can_break_one_way(sorted_s1, sorted_s2) or can_break_one_way(sorted_s2, sorted_s1)