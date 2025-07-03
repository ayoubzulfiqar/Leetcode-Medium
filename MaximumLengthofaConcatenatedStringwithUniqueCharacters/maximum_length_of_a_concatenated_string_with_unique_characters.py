class Solution:
    def maxLength(self, arr: list[str]) -> int:
        
        valid_strings_info = []
        for s in arr:
            current_mask = 0
            is_unique_s = True
            for char_code in map(ord, s):
                bit_pos = char_code - ord('a')
                if (current_mask >> bit_pos) & 1:
                    is_unique_s = False
                    break
                current_mask |= (1 << bit_pos)
            
            if is_unique_s:
                valid_strings_info.append((current_mask, len(s)))
        
        self.max_len = 0

        def backtrack(index, current_combined_mask, current_combined_length):
            self.max_len = max(self.max_len, current_combined_length)

            if index == len(valid_strings_info):
                return

            backtrack(index + 1, current_combined_mask, current_combined_length)

            s_mask, s_len = valid_strings_info[index]

            if (current_combined_mask & s_mask) == 0:
                backtrack(index + 1, current_combined_mask | s_mask, current_combined_length + s_len)
        
        backtrack(0, 0, 0)
        
        return self.max_len