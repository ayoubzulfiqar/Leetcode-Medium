class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        if num % 3 == 0:
            x = (num - 3) // 3
            return [x, x + 1, x + 2]
        else:
            return []