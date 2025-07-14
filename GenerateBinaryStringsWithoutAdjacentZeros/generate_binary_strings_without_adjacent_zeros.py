class Solution:
    def generateBinaryStrings(self, n: int) -> list[str]:
        results = []

        def backtrack(current_idx, current_string):
            if current_idx == n:
                results.append(current_string)
                return

            # Option 1: Append '1'
            # '1' can always be appended
            backtrack(current_idx + 1, current_string + '1')

            # Option 2: Append '0'
            # '0' can only be appended if the previous character was '1'
            # or if it's the very first character (current_idx == 0)
            if current_idx == 0 or current_string[-1] == '1':
                backtrack(current_idx + 1, current_string + '0')

        backtrack(0, "")
        return results