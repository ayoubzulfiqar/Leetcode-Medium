class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x_char = str(x)
        n_len = len(n)

        if n[0] != '-':
            for i in range(n_len):
                if x_char > n[i]:
                    return n[:i] + x_char + n[i:]
            return n + x_char
        else:
            for i in range(1, n_len):
                if x_char < n[i]:
                    return n[:i] + x_char + n[i:]
            return n + x_char