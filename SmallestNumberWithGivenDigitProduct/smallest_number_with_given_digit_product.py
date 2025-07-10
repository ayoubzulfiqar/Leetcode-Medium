class Solution:
    def smallestNumber(self, product: int) -> int:
        if product == 0:
            return 0
        if product == 1:
            return 1

        digits = []
        # Iterate from largest possible digit (9) down to 2.
        # This greedy approach ensures we use larger factors first,
        # which minimizes the number of digits.
        for d in range(9, 1, -1):
            while product % d == 0:
                digits.append(d)
                product //= d
        
        # If after trying all digits from 9 down to 2, the product is still
        # greater than 1, it means the original product contains prime factors
        # greater than 9 (e.g., 11, 13, 17, etc.) or is itself such a prime.
        # In this case, it's impossible to form the number using single digits.
        if product > 1:
            return -1
        
        # To form the smallest possible number from the collected digits,
        # they must be sorted in ascending order.
        digits.sort()
        
        # Join the sorted digits to form a string and convert it to an integer.
        return int("".join(map(str, digits)))