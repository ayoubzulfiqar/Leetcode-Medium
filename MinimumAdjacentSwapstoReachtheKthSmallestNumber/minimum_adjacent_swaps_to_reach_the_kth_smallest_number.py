class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:

        def next_permutation(s_list):
            n = len(s_list)
            i = n - 2
            while i >= 0 and s_list[i] >= s_list[i+1]:
                i -= 1

            if i == -1:
                return False 

            j = n - 1
            while s_list[j] <= s_list[i]:
                j -= 1

            s_list[i], s_list[j] = s_list[j], s_list[i]

            left = i + 1
            right = n - 1
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            return True

        def min_swaps_calc(s1_str, s2_str):
            s1 = list(s1_str)
            s2 = list(s2_str)
            n = len(s1)
            swaps = 0

            for i in range(n):
                if s1[i] != s2[i]:
                    j = i + 1
                    while j < n and s1[j] != s2[i]:
                        j += 1
                    
                    temp = s1[j]
                    for x in range(j, i, -1):
                        s1[x] = s1[x-1]
                    s1[i] = temp
                    
                    swaps += (j - i)
            return swaps

        target_num_list = list(num) 

        for _ in range(k):
            next_permutation(target_num_list)
        
        target_num_str = "".join(target_num_list)

        return min_swaps_calc(num, target_num_str)