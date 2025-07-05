class Solution:
    def decode(self, encoded: list[int]) -> list[int]:
        n = len(encoded) + 1

        # Calculate the XOR sum of all numbers from 1 to n.
        # This is total_xor_perm = 1 ^ 2 ^ ... ^ n
        total_xor_perm = 0
        for i in range(1, n + 1):
            total_xor_perm ^= i

        # Calculate the XOR sum of S_k for k from 1 to n-1,
        # where S_k = encoded[0] ^ encoded[1] ^ ... ^ encoded[k-1].
        # This is xor_sum_of_S_k = S_1 ^ S_2 ^ ... ^ S_{n-1}.
        #
        # We know p_k = p_0 ^ S_k.
        # total_xor_perm = p_0 ^ p_1 ^ ... ^ p_{n-1}
        #                = p_0 ^ (p_0 ^ S_1) ^ (p_0 ^ S_2) ^ ... ^ (p_0 ^ S_{n-1})
        # Since n is odd, p_0 appears n times, so p_0 ^ ... ^ p_0 (n times) = p_0.
        # total_xor_perm = p_0 ^ S_1 ^ S_2 ^ ... ^ S_{n-1}
        # Therefore, p_0 = total_xor_perm ^ (S_1 ^ S_2 ^ ... ^ S_{n-1})
        
        xor_sum_of_S_k = 0
        current_xor_prefix = 0
        # Iterate through encoded to compute S_k and their XOR sum
        # encoded has length n-1, so indices go from 0 to n-2
        for i in range(n - 1):
            current_xor_prefix ^= encoded[i] # current_xor_prefix becomes S_{i+1}
            xor_sum_of_S_k ^= current_xor_prefix

        # Calculate p_0
        p0 = total_xor_perm ^ xor_sum_of_S_k

        # Reconstruct the original permutation array
        perm = [0] * n
        perm[0] = p0
        for i in range(1, n):
            # perm[i] = perm[i-1] XOR encoded[i-1]
            perm[i] = perm[i-1] ^ encoded[i-1]
        
        return perm