class Solution:
    def check_arithmetic_subarray(self, arr):
        n = len(arr)
        if n < 2:
            return False 
        if n == 2:
            return True

        min_val = float('inf')
        max_val = float('-inf')
        num_set = set()

        for x in arr:
            min_val = min(min_val, x)
            max_val = max(max_val, x)
            num_set.add(x)
        
        if min_val == max_val:
            return True

        if len(num_set) != n:
            return False

        if (max_val - min_val) % (n - 1) != 0:
            return False

        common_diff = (max_val - min_val) // (n - 1)

        current_val = min_val + common_diff
        while current_val < max_val:
            if current_val not in num_set:
                return False
            current_val += common_diff
        
        return True

    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        m = len(l)
        answer = []

        for i in range(m):
            start = l[i]
            end = r[i]
            sub_array = nums[start : end + 1]
            answer.append(self.check_arithmetic_subarray(sub_array))
        
        return answer