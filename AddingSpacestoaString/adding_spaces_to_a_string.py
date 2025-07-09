class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = []
        space_ptr = 0
        s_ptr = 0

        while s_ptr < len(s):
            if space_ptr < len(spaces) and s_ptr == spaces[space_ptr]:
                result.append(' ')
                space_ptr += 1
            result.append(s[s_ptr])
            s_ptr += 1

        return "".join(result)