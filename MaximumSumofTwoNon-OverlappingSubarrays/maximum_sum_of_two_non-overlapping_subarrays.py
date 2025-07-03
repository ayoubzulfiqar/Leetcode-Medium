class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        
        P = [0] * (n + 1)
        for i in range(n):
            P[i+1] = P[i] + nums[i]
            
        max_total_sum = 0
        
        # Case 1: Subarray of length firstLen comes before subarray of length secondLen
        # i is the starting index of the firstLen subarray
        # j is the starting index of the secondLen subarray
        for i in range(n - firstLen - secondLen + 1):
            current_first_sum = P[i + firstLen] - P[i]
            for j in range(i + firstLen, n - secondLen + 1):
                current_second_sum = P[j + secondLen] - P[j]
                max_total_sum = max(max_total_sum, current_first_sum + current_second_sum)
                
        # Case 2: Subarray of length secondLen comes before subarray of length firstLen
        # This is symmetric to Case 1, just swap the roles of firstLen and secondLen
        for i in range(n - secondLen - firstLen + 1):
            current_first_sum = P[i + secondLen] - P[i]
            for j in range(i + secondLen, n - firstLen + 1):
                current_second_sum = P[j + firstLen] - P[j]
                max_total_sum = max(max_total_sum, current_first_sum + current_second_sum)
                
        return max_total_sum