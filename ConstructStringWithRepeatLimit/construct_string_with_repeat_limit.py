class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = [0] * 26
        for char_code in s:
            counts[ord(char_code) - ord('a')] += 1

        result = []
        
        for i in range(25, -1, -1):
            while counts[i] > 0:
                num_to_append = min(counts[i], repeatLimit)
                for _ in range(num_to_append):
                    result.append(chr(ord('a') + i))
                counts[i] -= num_to_append

                if counts[i] > 0:
                    found_next_char = False
                    for j in range(i - 1, -1, -1):
                        if counts[j] > 0:
                            result.append(chr(ord('a') + j))
                            counts[j] -= 1
                            found_next_char = True
                            break
                    
                    if not found_next_char:
                        break
                else:
                    break
        
        return "".join(result)