class Solution:
    def findKLengthSubstrings(self, s: str, k: int) -> list[str]:
        n = len(s)
        if k <= 0 or k > n:
            return []

        result_substrings = set()

        for i in range(n - k + 1):
            current_substring = s[i : i + k]
            
            if len(set(current_substring)) == k:
                result_substrings.add(current_substring)
        
        return list(result_substrings)