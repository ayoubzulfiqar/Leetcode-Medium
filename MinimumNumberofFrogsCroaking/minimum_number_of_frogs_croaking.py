class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        freq = [0] * 5
        
        max_frogs = 0
        current_frogs = 0

        for char in croakOfFrogs:
            if char == 'c':
                freq[0] += 1
                current_frogs += 1
                max_frogs = max(max_frogs, current_frogs)
            elif char == 'r':
                if freq[0] == 0:
                    return -1
                freq[0] -= 1
                freq[1] += 1
            elif char == 'o':
                if freq[1] == 0:
                    return -1
                freq[1] -= 1
                freq[2] += 1
            elif char == 'a':
                if freq[2] == 0:
                    return -1
                freq[2] -= 1
                freq[3] += 1
            elif char == 'k':
                if freq[3] == 0:
                    return -1
                freq[3] -= 1
                freq[4] += 1
                current_frogs -= 1
            
        if current_frogs != 0:
            return -1
        
        return max_frogs