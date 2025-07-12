import collections
import math

class Solution:
    def numberOfGoodPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        total_good_pairs = 0
        
        freq2 = collections.Counter(nums2)
        
        for num1_val in nums1:
            if num1_val % k == 0:
                target_quotient = num1_val // k
                
                limit = int(math.sqrt(target_quotient))
                
                for d in range(1, limit + 1):
                    if target_quotient % d == 0:
                        divisor1 = d
                        total_good_pairs += freq2[divisor1]
                        
                        divisor2 = target_quotient // d
                        
                        if divisor1 != divisor2:
                            total_good_pairs += freq2[divisor2]
                                
        return total_good_pairs