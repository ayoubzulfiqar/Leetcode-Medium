class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Use a stack to store pairs of [character, count]
        # This allows efficient tracking of adjacent characters and their counts.
        stack = []

        for char in s:
            # If the stack is not empty and the current character is the same as the top of the stack
            if stack and stack[-1][0] == char:
                # Increment the count of the character at the top of the stack
                stack[-1][1] += 1
                # If the count reaches k, remove (pop) this character from the stack
                # This simulates the removal of k adjacent duplicates
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # If the stack is empty or the current character is different from the top
                # Push the new character onto the stack with a count of 1
                stack.append([char, 1])

        # After processing all characters, construct the result string
        # by repeating each character in the stack its corresponding count times
        result = []
        for char, count in stack:
            result.append(char * count)

        return "".join(result)