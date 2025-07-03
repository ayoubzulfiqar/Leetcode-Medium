class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        n = len(arr)
        
        prev_no_del = arr[0]
        prev_with_del = float('-inf')
        
        max_overall_sum = arr[0]
        
        for i in range(1, n):
            current_no_del = max(arr[i], prev_no_del + arr[i])
            
            current_with_del = max(prev_with_del + arr[i], prev_no_del)
            
            max_overall_sum = max(max_overall_sum, current_no_del, current_with_del)
            
            prev_no_del = current_no_del
            prev_with_del = current_with_del
            
        return max_overall_sum