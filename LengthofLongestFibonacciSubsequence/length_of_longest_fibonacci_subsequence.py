class Solution:
    def lenLongestFibSubsequence(self, arr: list[int]) -> int:
        n = len(arr)
        val_to_idx = {x: i for i, x in enumerate(arr)}

        dp = {}
        max_len = 0

        for j in range(n):
            for i in range(j):
                num1 = arr[i]
                num2 = arr[j]
                
                prev_num = num2 - num1

                if prev_num < num1 and prev_num in val_to_idx:
                    k = val_to_idx[prev_num]
                    
                    current_len = dp.get((k, i), 2) + 1
                    dp[(i, j)] = current_len
                    max_len = max(max_len, current_len)
        
        return max_len