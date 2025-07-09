class Solution:
    def executeInstructions(self, n: int, startPos: list[int], s: str) -> list[int]:
        m = len(s)
        answer = [0] * m

        for i in range(m):
            current_row, current_col = startPos[0], startPos[1]
            executed_count = 0

            for j in range(i, m):
                instruction = s[j]
                
                next_row, next_col = current_row, current_col

                if instruction == 'L':
                    next_col -= 1
                elif instruction == 'R':
                    next_col += 1
                elif instruction == 'U':
                    next_row -= 1
                elif instruction == 'D':
                    next_row += 1
                
                if 0 <= next_row < n and 0 <= next_col < n:
                    current_row, current_col = next_row, next_col
                    executed_count += 1
                else:
                    break
            
            answer[i] = executed_count
        
        return answer