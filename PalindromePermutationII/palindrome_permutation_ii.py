import collections

class Solution:
    def generatePalindromes(self, s: str) -> list[str]:
        char_counts = collections.Counter(s)
        
        odd_char = ''
        odd_count = 0
        
        half_counts = collections.Counter()
        for char, count in char_counts.items():
            if count % 2 == 1:
                odd_count += 1
                odd_char = char
            
            if odd_count > 1:
                return []
            
            half_counts[char] = count // 2
            
        results = set()
        
        def backtrack(current_half_str, remaining_half_counts):
            if sum(remaining_half_counts.values()) == 0:
                full_palindrome = current_half_str + odd_char + current_half_str[::-1]
                results.add(full_palindrome)
                return
            
            for char in sorted(remaining_half_counts.keys()):
                if remaining_half_counts[char] > 0:
                    remaining_half_counts[char] -= 1
                    backtrack(current_half_str + char, remaining_half_counts)
                    remaining_half_counts[char] += 1
        
        backtrack("", half_counts)
        
        return list(results)