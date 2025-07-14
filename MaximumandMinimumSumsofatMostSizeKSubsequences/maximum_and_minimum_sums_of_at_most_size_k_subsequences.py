class Solution:
    def sumsOfSubsequences(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()

        # Precompute modular inverses for numbers up to k-1
        # inv[i] stores i^(-1) % MOD
        inv = [0] * k
        if k > 1:
            inv[1] = 1
            for i in range(2, k):
                inv[i] = (MOD - (MOD // i) * inv[MOD % i] % MOD) % MOD

        total_sum = 0

        for i in range(n):
            current_num = nums[i]

            # Calculate count_min_contribution
            # Number of elements to the right of nums[i] is (n - 1 - i)
            # We need to choose j elements from these, where 0 <= j <= k-1
            # The number of such subsequences is sum(C(n - 1 - i, j) for j from 0 to min(n - 1 - i, k - 1))
            
            n_right = n - 1 - i
            r_max_min = min(n_right, k - 1)
            
            sum_C_min = 0
            C_val = 1  # C(n_right, 0)
            
            sum_C_min = (sum_C_min + C_val) % MOD
            
            for j in range(1, r_max_min + 1):
                # C(N, j) = C(N, j-1) * (N - j + 1) / j
                C_val = C_val * (n_right - j + 1) % MOD * inv[j] % MOD
                sum_C_min = (sum_C_min + C_val) % MOD

            # Calculate count_max_contribution
            # Number of elements to the left of nums[i] is i
            # We need to choose j elements from these, where 0 <= j <= k-1
            # The number of such subsequences is sum(C(i, j) for j from 0 to min(i, k - 1))

            n_left = i
            r_max_max = min(n_left, k - 1)

            sum_C_max = 0
            C_val = 1  # C(n_left, 0)

            sum_C_max = (sum_C_max + C_val) % MOD
            
            for j in range(1, r_max_max + 1):
                # C(N, j) = C(N, j-1) * (N - j + 1) / j
                C_val = C_val * (n_left - j + 1) % MOD * inv[j] % MOD
                sum_C_max = (sum_C_max + C_val) % MOD
            
            total_sum = (total_sum + current_num * (sum_C_min + sum_C_max)) % MOD
        
        return total_sum