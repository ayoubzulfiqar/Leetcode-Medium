class Solution:
    def canChoose(self, groups: list[list[int]], nums: list[int]) -> bool:
        
        def find_subarray(arr: list[int], sub: list[int], start_idx: int) -> int:
            len_arr = len(arr)
            len_sub = len(sub)
            
            if len_sub == 0:
                return start_idx 

            for i in range(start_idx, len_arr - len_sub + 1):
                match = True
                for j in range(len_sub):
                    if arr[i + j] != sub[j]:
                        match = False
                        break 
                if match:
                    return i 
            return -1 

        current_nums_search_idx = 0
        
        for group in groups:
            found_match_idx = find_subarray(nums, group, current_nums_search_idx)
            
            if found_match_idx == -1:
                return False
            
            current_nums_search_idx = found_match_idx + len(group)
            
        return True