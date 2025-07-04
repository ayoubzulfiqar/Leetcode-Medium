class Solution:
    def minFlips(self, target: str) -> int:
        current_flip_state = False
        operations = 0

        for char_target in target:
            current_s_char = '1' if current_flip_state else '0'

            if current_s_char != char_target:
                operations += 1
                current_flip_state = not current_flip_state
        
        return operations