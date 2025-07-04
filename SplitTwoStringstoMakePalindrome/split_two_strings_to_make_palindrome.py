class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)

        def is_palindrome(s: str, i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def check(s1: str, s2: str, length: int) -> bool:
            left = 0
            right = length - 1

            while left < right and s1[left] == s2[right]:
                left += 1
                right -= 1
            
            return is_palindrome(s1, left, right) or is_palindrome(s2, left, right)

        return check(a, b, n) or check(b, a, n)