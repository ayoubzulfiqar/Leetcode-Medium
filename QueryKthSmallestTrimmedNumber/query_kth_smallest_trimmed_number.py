class Solution:
    def kthSmallestTrimmedNumber(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        N = len(nums)
        L = len(nums[0]) 

        current_sorted_list = [(nums[i], i) for i in range(N)]
        
        results_by_trim_length = [None] * (L + 1)
        
        for k in range(L): 
            current_sorted_list = self._counting_sort(current_sorted_list, k, L)
            
            results_by_trim_length[k + 1] = list(current_sorted_list) 

        answer = []
        for ki, trimi in queries:
            answer.append(results_by_trim_length[trimi][ki - 1][1])
            
        return answer

    def _counting_sort(self, arr: list[tuple[str, int]], digit_idx_from_right: int, num_length: int) -> list[tuple[str, int]]:
        counts = [0] * 10 
        output = [None] * len(arr)

        for item_str, _ in arr:
            digit_char = item_str[num_length - 1 - digit_idx_from_right]
            digit = int(digit_char)
            counts[digit] += 1

        for i in range(1, 10):
            counts[i] += counts[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            item_str, original_idx = arr[i]
            digit_char = item_str[num_length - 1 - digit_idx_from_right]
            digit = int(digit_char)
            
            counts[digit] -= 1
            output[counts[digit]] = (item_str, original_idx)
        
        return output