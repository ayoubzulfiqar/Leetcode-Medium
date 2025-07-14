class Solution:
    def countAlmostEqualPairs(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)

        def check_swap(s_original: str, s_target_int: int) -> bool:
            s_orig_list = list(s_original)
            len_orig = len(s_orig_list)

            if len_orig < 2:
                return False

            for i in range(len_orig):
                for j in range(i + 1, len_orig):
                    s_orig_list[i], s_orig_list[j] = s_orig_list[j], s_orig_list[i]
                    
                    s_swapped = "".join(s_orig_list)
                    
                    if int(s_swapped) == s_target_int:
                        return True
                    
                    s_orig_list[i], s_orig_list[j] = s_orig_list[j], s_orig_list[i]
            
            return False

        for i in range(n):
            for j in range(i + 1, n):
                num1 = nums[i]
                num2 = nums[j]

                if num1 == num2:
                    count += 1
                    continue

                if check_swap(str(num1), num2) or check_swap(str(num2), num1):
                    count += 1
        
        return count