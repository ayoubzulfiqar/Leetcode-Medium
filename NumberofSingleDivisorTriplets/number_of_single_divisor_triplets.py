def count_single_divisor_triplets(N: int) -> int:
    if N <= 0:
        return 0
    
    # Precompute Mobius function values up to N using a sieve
    mu = [0] * (N + 1)
    is_prime = [True] * (N + 1)
    primes = []

    mu[1] = 1
    is_prime[0] = is_prime[1] = False

    for i in range(2, N + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        
        for p in primes:
            if i * p > N:
                break
            is_prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            else:
                mu[i * p] = -mu[i]

    # Calculate the sum using the Mobius inversion formula:
    # Ans = sum_{d=1 to N} mu(d) * (floor(N/d))^3
    total_count = 0
    for d in range(1, N + 1):
        # N // d is equivalent to floor(N/d) for positive N and d
        term = mu[d] * (N // d)**3
        total_count += term
    
    return total_count