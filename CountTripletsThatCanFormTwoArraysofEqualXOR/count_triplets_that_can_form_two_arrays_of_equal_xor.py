class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        n = len(arr)
        
        # Calculate prefix XORs.
        # pxor[x] will store the XOR sum of arr[0] ^ arr[1] ^ ... ^ arr[x-1].
        # pxor[0] is initialized to 0, representing the XOR sum of an empty prefix.
        pxor = [0] * (n + 1)
        for i in range(n):
            pxor[i+1] = pxor[i] ^ arr[i]
            
        count = 0
        
        # We are looking for triplets (i, j, k) such that 0 <= i < j <= k < n.
        # Let a = arr[i] ^ ... ^ arr[j-1]
        # Let b = arr[j] ^ ... ^ arr[k]
        # Using prefix XORs:
        # a = pxor[j] ^ pxor[i]
        # b = pxor[k+1] ^ pxor[j]
        
        # The condition a == b becomes:
        # pxor[j] ^ pxor[i] == pxor[k+1] ^ pxor[j]
        
        # XORing both sides with pxor[j]:
        # pxor[i] == pxor[k+1]
        
        # So, for each pair (i, k) where 0 <= i <= k < n, if pxor[i] == pxor[k+1],
        # then any j such that i < j <= k will satisfy the original condition a == b.
        # The number of such valid j's is k - (i+1) + 1 = k - i.
        
        for i in range(n):
            for k in range(i, n): # k must be >= i as per 0 <= i <= k < n
                # Check if the XOR sum from arr[i] to arr[k] is 0.
                # This is equivalent to checking if pxor[i] == pxor[k+1].
                if pxor[k+1] ^ pxor[i] == 0:
                    # If XOR(arr[i]...arr[k]) is 0, then for any j in (i, k],
                    # XOR(arr[i]...arr[j-1]) == XOR(arr[j]...arr[k]).
                    # The number of possible j values is k - i.
                    count += (k - i)
                    
        return count