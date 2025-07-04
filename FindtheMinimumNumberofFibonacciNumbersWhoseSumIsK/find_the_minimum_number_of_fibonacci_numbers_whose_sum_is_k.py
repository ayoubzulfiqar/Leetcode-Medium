class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_numbers = [1, 1]
        a, b = 1, 1
        while True:
            next_fib = a + b
            if next_fib > k:
                break
            fib_numbers.append(next_fib)
            a, b = b, next_fib
        
        count = 0
        i = len(fib_numbers) - 1
        while k > 0 and i >= 0:
            if fib_numbers[i] <= k:
                k -= fib_numbers[i]
                count += 1
            i -= 1
            
        return count