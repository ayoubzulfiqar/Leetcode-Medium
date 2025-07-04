class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        
        for i in range(n):
            prefix_xor[i+1] = prefix_xor[i] ^ arr[i]
            
        answer = []
        for left, right in queries:
            current_xor_sum = prefix_xor[right + 1] ^ prefix_xor[left]
            answer.append(current_xor_sum)
            
        return answer