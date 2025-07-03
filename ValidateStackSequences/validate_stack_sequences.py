class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        j = 0  # Pointer for the popped array

        for x in pushed:
            stack.append(x)
            # While the stack is not empty and the top of the stack matches the current element in popped
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        # If all elements in popped were successfully matched and popped from the stack,
        # the stack should be empty at the end.
        return len(stack) == 0