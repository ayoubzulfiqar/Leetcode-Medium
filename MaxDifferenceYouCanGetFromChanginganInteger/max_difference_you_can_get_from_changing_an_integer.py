class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        n = len(s)

        # Calculate 'a' (maximum number)
        # To maximize, find the first digit that is not '9' and change all its occurrences to '9'.
        # If all digits are '9', 'a' will be num itself.
        a_str_list = list(s)
        x_for_max = ''
        for char in a_str_list:
            if char != '9':
                x_for_max = char
                break
        
        if x_for_max != '': 
            for i in range(n):
                if a_str_list[i] == x_for_max:
                    a_str_list[i] = '9'
        a = int("".join(a_str_list))

        # Calculate 'b' (minimum number)
        # To minimize, we have two cases:
        # 1. If the first digit is not '1', change all its occurrences to '1'.
        # 2. If the first digit is '1', find the first subsequent digit that is not '0' or '1'
        #    and change all its occurrences to '0'.
        # If no such digit is found (e.g., "100", "111"), 'b' will be num itself.
        b_str_list = list(s)
        x_for_min = ''
        y_for_min = ''

        if b_str_list[0] != '1':
            x_for_min = b_str_list[0]
            y_for_min = '1'
        else: 
            for i in range(1, n):
                if b_str_list[i] != '0' and b_str_list[i] != '1':
                    x_for_min = b_str_list[i]
                    y_for_min = '0'
                    break

        if x_for_min != '':
            for i in range(n):
                if b_str_list[i] == x_for_min:
                    b_str_list[i] = y_for_min
        
        b = int("".join(b_str_list))
        
        return a - b