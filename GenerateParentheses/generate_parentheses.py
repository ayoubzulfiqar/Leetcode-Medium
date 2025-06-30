class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current_string, open_count, close_count):
            # Base case: If we have used all n open and n close parentheses
            if open_count == n and close_count == n:
                result.append(current_string)
                return

            # Option 1: Add an opening parenthesis
            # We can add an opening parenthesis if we haven't used all n yet
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)

            # Option 2: Add a closing parenthesis
            # We can add a closing parenthesis only if it would result in a well-formed string
            # This means the number of closing parentheses must be less than the number of opening ones
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)

        # Start the backtracking process with an empty string and zero counts
        backtrack("", 0, 0)
        return result