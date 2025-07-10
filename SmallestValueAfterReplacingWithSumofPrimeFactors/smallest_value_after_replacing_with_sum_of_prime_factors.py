import math

class Solution:
    def smallestValue(self, n: int) -> int:
        
        def sum_prime_factors(num):
            s = 0
            d = 2
            temp_num = num
            while d * d <= temp_num:
                while temp_num % d == 0:
                    s += d
                    temp_num //= d
                d += 1
            if temp_num > 1:
                s += temp_num
            return s

        min_val = n
        visited = set()

        current_n = n
        while current_n not in visited:
            visited.add(current_n)
            min_val = min(min_val, current_n)
            
            next_n = sum_prime_factors(current_n)
            
            current_n = next_n
        
        return min_val