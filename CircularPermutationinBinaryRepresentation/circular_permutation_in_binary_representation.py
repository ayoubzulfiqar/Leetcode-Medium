class Solution:
    def circularPermutation(self, n: int, start: int) -> list[int]:
        size = 1 << n
        gray_code_sequence = []
        for i in range(size):
            gray_code_sequence.append(i ^ (i >> 1))
            
        start_index = -1
        for i in range(size):
            if gray_code_sequence[i] == start:
                start_index = i
                break
        
        result = gray_code_sequence[start_index:] + gray_code_sequence[:start_index]
        
        return result