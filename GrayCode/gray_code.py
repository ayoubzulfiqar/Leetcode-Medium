class Solution:
    def grayCode(self, n: int) -> list[int]:
        num_elements = 1 << n
        result = []
        for i in range(num_elements):
            gray_code_value = i ^ (i >> 1)
            result.append(gray_code_value)
        return result