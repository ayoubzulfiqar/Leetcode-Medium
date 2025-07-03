import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = collections.Counter(s)
        visited = set()
        stack = []

        for char in s:
            counts[char] -= 1

            if char in visited:
                continue

            while stack and char < stack[-1] and counts[stack[-1]] > 0:
                popped_char = stack.pop()
                visited.remove(popped_char)
            
            stack.append(char)
            visited.add(char)
        
        return "".join(stack)