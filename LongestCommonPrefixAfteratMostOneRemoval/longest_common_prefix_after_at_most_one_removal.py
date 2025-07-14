class Solution:
    def longestCommonPrefixAfterOneRemoval(self, strs: list[str]) -> int:
        def find_lcp_length(string_list):
            if not string_list:
                return 0
            if len(string_list) == 1:
                return len(string_list[0])

            min_len = float('inf')
            for s in string_list:
                min_len = min(min_len, len(s))

            if min_len == 0:
                return 0

            lcp_len = 0
            for i in range(min_len):
                char_at_i = string_list[0][i]
                for j in range(1, len(string_list)):
                    if string_list[j][i] != char_at_i:
                        return lcp_len
                lcp_len += 1
            return lcp_len

        if not strs:
            return 0
        
        max_lcp_len = find_lcp_length(strs)

        num_strings = len(strs)
        
        for i in range(num_strings):
            original_str = strs[i]
            
            if not original_str: 
                continue 

            for j in range(len(original_str)):
                modified_str = original_str[:j] + original_str[j+1:]
                
                temp_strs = list(strs)
                temp_strs[i] = modified_str
                
                current_lcp_len = find_lcp_length(temp_strs)
                max_lcp_len = max(max_lcp_len, current_lcp_len)
                
        return max_lcp_len