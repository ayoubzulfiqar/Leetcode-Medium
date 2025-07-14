class Solution:
    def calculateScore(self, instructions: list[str], values: list[int]) -> int:
        n = len(instructions)
        score = 0
        current_index = 0
        visited = set()

        while True:
            if current_index < 0 or current_index >= n:
                break

            if current_index in visited:
                break

            visited.add(current_index)

            instruction_type = instructions[current_index]
            instruction_value = values[current_index]

            if instruction_type == "add":
                score += instruction_value
                current_index += 1
            elif instruction_type == "jump":
                current_index += instruction_value

        return score