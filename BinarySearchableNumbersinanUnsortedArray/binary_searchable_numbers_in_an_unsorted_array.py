class Solution:
    def count_binary_searchable_numbers(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        
        left_max = [0] * n
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], arr[i])

        right_min = [0] * n
        right_min[n-1] = arr[n-1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i+1], arr[i])

        count = 0
        for i in range(n):
            is_left_ok = (i == 0) or (left_max[i-1] <= arr[i])
            is_right_ok = (i == n - 1) or (arr[i] <= right_min[i+1])
            
            if is_left_ok and is_right_ok:
                count += 1
        
        return count