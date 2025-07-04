class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        char_to_coords = {}
        board_layout = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for r, row_str in enumerate(board_layout):
            for c, char in enumerate(row_str):
                char_to_coords[char] = (r, c)

        current_r, current_c = 0, 0
        result = []

        for char_to_reach in target:
            target_r, target_c = char_to_coords[char_to_reach]

            if char_to_reach == 'z':
                while current_c > target_c:
                    result.append('L')
                    current_c -= 1
                while current_r < target_r:
                    result.append('D')
                    current_r += 1
            else:
                while current_r < target_r:
                    result.append('D')
                    current_r += 1
                while current_r > target_r:
                    result.append('U')
                    current_r -= 1
                while current_c < target_c:
                    result.append('R')
                    current_c += 1
                while current_c > target_c:
                    result.append('L')
                    current_c -= 1
            
            result.append('!')
        
        return "".join(result)