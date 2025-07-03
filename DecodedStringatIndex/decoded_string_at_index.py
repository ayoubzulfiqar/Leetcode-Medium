class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for char in s:
            if char.isdigit():
                length *= int(char)
            else:
                length += 1

        for i in range(len(s) - 1, -1, -1):
            char = s[i]

            if char.isdigit():
                length //= int(char)
                k %= length
                if k == 0:
                    k = length
            else:
                if k == length:
                    return char
                length -= 1