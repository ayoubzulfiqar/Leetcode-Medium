class Solution:
    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        answer = []
        half_len = (intLength + 1) // 2
        start_num = 10**(half_len - 1)
        end_num = 10**half_len - 1
        suffix_len = intLength // 2

        for q in queries:
            prefix_val = start_num + q - 1
            if prefix_val > end_num:
                answer.append(-1)
            else:
                s_prefix = str(prefix_val)
                s_suffix = s_prefix[:suffix_len][::-1]
                s_palindrome = s_prefix + s_suffix
                answer.append(int(s_palindrome))
        return answer