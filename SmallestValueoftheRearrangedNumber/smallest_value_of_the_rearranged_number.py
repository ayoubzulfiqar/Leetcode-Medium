class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        is_negative = num < 0
        s_num = str(abs(num))
        digits = sorted(list(s_num))

        if not is_negative:
            # For positive numbers, we want the smallest number.
            # This means putting the smallest non-zero digit first,
            # followed by all zeros, and then the rest of the digits in ascending order.
            
            if digits[0] == '0':
                # Find the first non-zero digit to place at the beginning
                first_non_zero_idx = -1
                for i in range(len(digits)):
                    if digits[i] != '0':
                        first_non_zero_idx = i
                        break
                
                # Construct the string:
                # 1. The smallest non-zero digit
                # 2. All the zeros
                # 3. The remaining non-zero digits, sorted
                
                # Swap the first non-zero digit to the front
                digits[0], digits[first_non_zero_idx] = digits[first_non_zero_idx], digits[0]
                
                # Now, digits[0] is the smallest non-zero.
                # The rest of the digits (from index 1 onwards) need to be sorted
                # to ensure all zeros come before other larger digits.
                # Example: ['5', '0', '7', '8', '0'] after initial swap for 80705
                # We need ['5', '0', '0', '7', '8']
                
                # A simpler way is to count zeros and separate non-zero digits
                num_zeros = digits.count('0')
                non_zero_digits = [d for d in digits if d != '0']
                
                # The smallest non-zero digit is non_zero_digits[0]
                # The remaining non-zero digits are non_zero_digits[1:]
                result_str = non_zero_digits[0] + '0' * num_zeros + ''.join(non_zero_digits[1:])
            else:
                # If there are no leading zeros (i.e., digits[0] is not '0'),
                # just join the sorted digits directly.
                result_str = ''.join(digits)
            
            return int(result_str)
        else:
            # For negative numbers, to get the smallest value, we need the largest absolute value.
            # This means arranging the digits in descending order.
            digits.sort(reverse=True)
            result_str = ''.join(digits)
            return -int(result_str)