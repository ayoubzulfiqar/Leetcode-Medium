import heapq
import sys

# Precompute primes using Sieve of Eratosthenes
MAX_NUM = 10000
is_prime = [True] * (MAX_NUM + 1)
is_prime[0] = is_prime[1] = False 

for p in range(2, int(MAX_NUM**0.5) + 1):
    if is_prime[p]:
        for multiple in range(p*p, MAX_NUM + 1, p):
            is_prime[multiple] = False

def solve():
    n, m = map(int, input().split())

    # Initial check: n must not be prime
    if is_prime[n]:
        return -1
    
    # Target m cannot be reached if it's prime, as n cannot become prime
    if is_prime[m]:
        return -1 

    # If n is already m and not prime, the cost is n (itself)
    if n == m:
        return n

    # Dijkstra's algorithm
    # dist[num] stores the minimum cost to reach 'num' from 'n'
    dist = {n: n} 
    # Priority queue stores (current_total_cost, current_number)
    pq = [(n, n)] 

    while pq:
        current_cost, current_num = heapq.heappop(pq)

        # If we found a shorter path to current_num already, skip
        if current_cost > dist.get(current_num, sys.maxsize):
            continue

        # If current_num is the target m, we found the minimum cost
        if current_num == m:
            return current_cost

        s_curr = str(current_num)
        num_digits = len(s_curr)

        # Explore neighbors by changing one digit
        for i in range(num_digits):
            digit = int(s_curr[i])
            
            # Try increasing the digit
            if digit < 9:
                next_s_list = list(s_curr)
                next_s_list[i] = str(digit + 1)
                next_num_str = "".join(next_s_list)
                
                # Ensure the number of digits doesn't change and it's within range
                if len(next_num_str) == num_digits: 
                    next_num = int(next_num_str)
                    # Check if the next number is valid (within bounds and not prime)
                    if 1 <= next_num <= MAX_NUM and not is_prime[next_num]:
                        new_cost = current_cost + next_num
                        if new_cost < dist.get(next_num, sys.maxsize):
                            dist[next_num] = new_cost
                            heapq.heappush(pq, (new_cost, next_num))

            # Try decreasing the digit
            if digit > 0:
                next_s_list = list(s_curr)
                next_s_list[i] = str(digit - 1)
                next_num_str = "".join(next_s_list)
                
                # Ensure the number of digits doesn't change and it's within range
                # (e.g., 10 -> 00 is invalid because 00 is 0, which is 1 digit, not 2)
                if len(next_num_str) == num_digits: 
                    next_num = int(next_num_str)
                    # Check if the next number is valid (>=1 and not prime)
                    if 1 <= next_num <= MAX_NUM and not is_prime[next_num]:
                        new_cost = current_cost + next_num
                        if new_cost < dist.get(next_num, sys.maxsize):
                            dist[next_num] = new_cost
                            heapq.heappush(pq, (new_cost, next_num))
    
    # If the priority queue becomes empty and m was not reached
    return -1

print(solve())