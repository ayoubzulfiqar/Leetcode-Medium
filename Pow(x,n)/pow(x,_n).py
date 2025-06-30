class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        # Handle negative exponent
        # If n is negative, we calculate x^(-n) and then take its reciprocal (1/x)^(-n)
        if n < 0:
            x = 1 / x
            n = -n # Convert n to its positive equivalent

        result = 1.0
        current_x = x # This variable will be squared in each iteration (x, x^2, x^4, x^8, ...)

        # Binary exponentiation (exponentiation by squaring)
        # We iterate while n is greater than 0
        while n > 0:
            # If the current bit of n is 1 (i.e., n is odd),
            # it means this power of x contributes to the final result.
            if n % 2 == 1:
                result *= current_x
            
            # Square current_x for the next iteration.
            # This effectively calculates x^(2^k) for increasing k.
            current_x *= current_x
            
            # Right shift n by 1 (integer division by 2).
            # This moves to the next bit of n.
            n //= 2
            
        return result