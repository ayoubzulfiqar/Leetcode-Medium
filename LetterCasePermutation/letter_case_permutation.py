class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        n = len(s)

        def backtrack(index, current_chars):
            if index == n:
                result.append("".join(current_chars))
                return

            char = s[index]
            
            if '0' <= char <= '9':  # It's a digit
                current_chars.append(char)
                backtrack(index + 1, current_chars)
                current_chars.pop()  # Backtrack
            else:  # It's a letter
                # Option 1: Append lowercase version
                current_chars.append(char.lower())
                backtrack(index + 1, current_chars)
                current_chars.pop()  # Backtrack

                # Option 2: Append uppercase version
                current_chars.append(char.upper())
                backtrack(index + 1, current_chars)
                current_chars.pop()  # Backtrack

        backtrack(0, [])
        return result