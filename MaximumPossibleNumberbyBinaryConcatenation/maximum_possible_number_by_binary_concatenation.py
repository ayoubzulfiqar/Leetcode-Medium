import itertools

class Solution:
    def max_concatenated_binary_number(self, nums: list[int]) -> int:
        binary_strings = [bin(n)[2:] for n in nums]
        
        max_val = 0
        
        for p in itertools.permutations(binary_strings):
            concatenated_binary_str = "".join(p)
            current_val = int(concatenated_binary_str, 2)
            max_val = max(max_val, current_val)
            
        return max_val