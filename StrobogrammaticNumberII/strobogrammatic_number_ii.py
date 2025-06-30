class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        result = []
        chars = [''] * n
        
        # Strobogrammatic pairs: (left_char, right_char)
        # Note: '0' cannot be a leading digit for numbers longer than 1.
        # For the middle digit of odd-length numbers, only '0', '1', '8' are valid.
        pairs = [
            ('0', '0'),
            ('1', '1'),
            ('6', '9'),
            ('8', '8'),
            ('9', '6')
        ]
        
        def backtrack(left, right):
            # Base case: If the left pointer has crossed the right pointer,
            # a complete strobogrammatic number has been formed.
            if left > right:
                result.append("".join(chars))
                return
            
            # Base case: If left and right pointers meet, it's the middle digit for odd length numbers.
            # Only '0', '1', '8' are valid middle digits.
            if left == right:
                for mid_char in ['0', '1', '8']:
                    chars[left] = mid_char
                    result.append("".join(chars))
                return
            
            # Recursive step: Try all valid strobogrammatic pairs for the current left and right positions.
            for l_char, r_char in pairs:
                # Constraint: '0' cannot be the leading digit for numbers longer than 1.
                if left == 0 and l_char == '0' and n > 1:
                    continue
                
                chars[left] = l_char
                chars[right] = r_char
                
                # Recurse for the next inner pair of positions
                backtrack(left + 1, right - 1)
        
        # Start the backtracking process from the outermost positions
        backtrack(0, n - 1)
        
        return result