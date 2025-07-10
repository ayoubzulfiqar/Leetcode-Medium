class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        min_ops = n  # Initialize with the maximum possible operations (delete all digits to get 0)

        # Helper function to calculate operations for a specific two-digit suffix (d1, d2)
        # We need to find the rightmost d2, then the rightmost d1 before it.
        def calculate_ops_for_suffix(d1: str, d2: str) -> int:
            idx2 = -1
            # Find the rightmost occurrence of d2
            for i in range(n - 1, -1, -1):
                if num[i] == d2:
                    idx2 = i
                    break
            
            if idx2 == -1:
                return float('inf') # d2 not found, this suffix cannot be formed

            idx1 = -1
            # Find the rightmost occurrence of d1 before idx2
            for i in range(idx2 - 1, -1, -1):
                if num[i] == d1:
                    idx1 = i
                    break
            
            if idx1 == -1:
                return float('inf') # d1 not found before idx2, this suffix cannot be formed
            
            # Number of operations:
            # (digits to delete after idx2) + (digits to delete between idx1 and idx2)
            # = (n - 1 - idx2) + (idx2 - 1 - idx1)
            # This simplifies to n - 2 - idx1
            return (n - 1 - idx2) + (idx2 - 1 - idx1)

        # Consider all target two-digit suffixes that are divisible by 25
        # "00", "25", "50", "75"
        min_ops = min(min_ops, calculate_ops_for_suffix('0', '0'))
        min_ops = min(min_ops, calculate_ops_for_suffix('2', '5'))
        min_ops = min(min_ops, calculate_ops_for_suffix('5', '0'))
        min_ops = min(min_ops, calculate_ops_for_suffix('7', '5'))

        # Also consider the case where the number becomes '0'
        # This is possible if 'num' contains at least one '0'.
        # To make it '0', we keep one '0' and delete all other n-1 digits.
        # This requires n-1 operations.
        found_zero = False
        for char_digit in num:
            if char_digit == '0':
                found_zero = True
                break
        
        if found_zero:
            min_ops = min(min_ops, n - 1)
        
        return min_ops