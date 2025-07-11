class Solution:
    def longestSpecialSubstring(self, s: str) -> int:
        n = len(s)

        def count_overlapping(main_string, sub_string):
            count = 0
            start = 0
            while True:
                idx = main_string.find(sub_string, start)
                if idx == -1:
                    break
                count += 1
                start = idx + 1
            return count

        for length in range(n, 0, -1):
            for char_code in range(ord('a'), ord('z') + 1):
                char = chr(char_code)
                
                target_substring = char * length
                
                occurrences = count_overlapping(s, target_substring)
                
                if occurrences >= 3:
                    return length
        
        return -1