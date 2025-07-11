import collections

class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        prime_counts = collections.Counter()

        directions = [
            (0, 1),   # East
            (1, 1),   # South-East
            (1, 0),   # South
            (1, -1),  # South-West
            (0, -1),  # West
            (-1, -1), # North-West
            (-1, 0),  # North
            (-1, 1)   # North-East
        ]

        for r in range(m):
            for c in range(n):
                for dr, dc in directions:
                    current_num = 0
                    nr, nc = r, c
                    
                    while 0 <= nr < m and 0 <= nc < n:
                        digit = mat[nr][nc]
                        current_num = current_num * 10 + digit
                        
                        if current_num > 10 and self.is_prime(current_num):
                            prime_counts[current_num] += 1
                        
                        nr += dr
                        nc += dc
        
        if not prime_counts:
            return -1
        
        max_freq = 0
        result = -1

        for prime, freq in prime_counts.items():
            if freq > max_freq:
                max_freq = freq
                result = prime
            elif freq == max_freq:
                result = max(result, prime)
                
        return result