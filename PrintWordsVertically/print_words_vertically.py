class Solution:
    def printVertically(self, s: str) -> list[str]:
        words = s.split()
        
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))
            
        result = [""] * max_len
        
        for word in words:
            for i in range(max_len):
                if i < len(word):
                    result[i] += word[i]
                else:
                    result[i] += ' '
                    
        final_result = []
        for vertical_word in result:
            final_result.append(vertical_word.rstrip())
            
        return final_result