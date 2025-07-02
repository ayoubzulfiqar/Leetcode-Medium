class Solution:
    def countSubstrings(self, s: str) -> int:
        total_palindromes = 0
        n = len(s)

        # Iterate through all possible centers
        # There are 2*n - 1 potential centers:
        # n centers for odd-length palindromes (each character itself)
        # n-1 centers for even-length palindromes (between two characters)
        for i in range(n):
            # Case 1: Odd length palindromes
            # The center is a single character s[i]
            left = i
            right = i
            # Expand outwards from the center
            while left >= 0 and right < n and s[left] == s[right]:
                total_palindromes += 1  # Found a palindrome
                left -= 1
                right += 1

            # Case 2: Even length palindromes
            # The center is between s[i] and s[i+1]
            left = i
            right = i + 1
            # Expand outwards from the center
            while left >= 0 and right < n and s[left] == s[right]:
                total_palindromes += 1  # Found a palindrome
                left -= 1
                right += 1
        
        return total_palindromes