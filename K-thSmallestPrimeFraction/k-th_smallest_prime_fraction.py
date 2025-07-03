class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        
        left, right = 0.0, 1.0
        
        ans_num = 0
        ans_den = 1
        
        for _ in range(100): 
            mid = (left + right) / 2
            
            count = 0
            current_max_num = 0
            current_max_den = 1
            
            i = 0 
            for j in range(1, n):
                while i < j and arr[i] <= mid * arr[j]:
                    if arr[i] * current_max_den > current_max_num * arr[j]:
                        current_max_num = arr[i]
                        current_max_den = arr[j]
                    i += 1
                
                count += i
            
            if count < k:
                left = mid
            else:
                ans_num = current_max_num
                ans_den = current_max_den
                right = mid
                
        return [ans_num, ans_den]