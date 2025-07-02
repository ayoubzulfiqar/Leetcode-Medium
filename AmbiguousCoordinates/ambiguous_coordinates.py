class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        s_digits = s[1:-1]
        n = len(s_digits)
        result = []

        def get_valid_numbers(num_str: str) -> list[str]:
            valid_nums = []
            
            # Case 1: num_str represents an integer
            # An integer cannot have leading zeros unless it is "0" itself.
            # E.g., "01" is invalid, "0" is valid, "123" is valid.
            if len(num_str) == 1 or num_str[0] != '0':
                valid_nums.append(num_str)
            
            # Case 2: num_str represents a decimal number
            # Iterate through all possible positions to insert the decimal point.
            # The decimal point must have at least one digit before it (handled by range(1, len(num_str))).
            # Rules for decimal numbers:
            # 1. The part before the decimal (integer part) cannot start with '0' unless it's just "0".
            # 2. The part after the decimal (fractional part) cannot end with '0'.
            for i in range(1, len(num_str)): 
                left_part = num_str[:i]
                right_part = num_str[i:]

                # Check rule 1: e.g., "01.23" is invalid because "01" is an invalid integer part
                if len(left_part) > 1 and left_part[0] == '0':
                    continue 

                # Check rule 2: e.g., "1.20" is invalid because "20" ends with '0'
                if right_part[-1] == '0':
                    continue

                valid_nums.append(left_part + "." + right_part)
            
            return valid_nums

        # Iterate through all possible split points for the original digit string.
        # 'i' represents the length of the x-coordinate's digit string.
        # x_digits will be s_digits[0...i-1], y_digits will be s_digits[i...n-1].
        # 'i' must be at least 1 (x_digits cannot be empty) and less than n (y_digits cannot be empty).
        for i in range(1, n): 
            x_digits = s_digits[:i]
            y_digits = s_digits[i:]

            x_possibilities = get_valid_numbers(x_digits)
            y_possibilities = get_valid_numbers(y_digits)

            # Combine all valid x and y possibilities to form the final coordinate strings
            for x in x_possibilities:
                for y in y_possibilities:
                    result.append(f"({x}, {y})")
        
        return result