class Solution:
    def compressString(self, word: str) -> str:
        comp = []
        n = len(word)
        i = 0
        
        while i < n:
            char = word[i]
            count = 0
            j = i
            
            while j < n and word[j] == char:
                count += 1
                j += 1
            
            while count > 0:
                length = min(count, 9)
                comp.append(str(length))
                comp.append(char)
                count -= length
            
            i = j
            
        return "".join(comp)