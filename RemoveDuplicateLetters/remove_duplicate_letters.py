class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        stack = []
        in_stack = set()

        for i, char in enumerate(s):
            if char in in_stack:
                continue

            while stack and char < stack[-1] and last_occurrence[stack[-1]] > i:
                popped_char = stack.pop()
                in_stack.remove(popped_char)

            stack.append(char)
            in_stack.add(char)

        return "".join(stack)