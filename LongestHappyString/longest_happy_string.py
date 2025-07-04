class Solution:
    def longestHappyString(self, a: int, b: int, c: int) -> str:
        counts = {'a': a, 'b': b, 'c': c}
        res = []

        while True:
            available_chars = []
            if counts['a'] > 0:
                available_chars.append(('a', counts['a']))
            if counts['b'] > 0:
                available_chars.append(('b', counts['b']))
            if counts['c'] > 0:
                available_chars.append(('c', counts['c']))
            
            available_chars.sort(key=lambda x: x[1], reverse=True)

            appended_this_iter = False
            for char, count in available_chars:
                if len(res) >= 2 and res[-1] == char and res[-2] == char:
                    continue 
                
                res.append(char)
                counts[char] -= 1
                appended_this_iter = True
                break                   
            
            if not appended_this_iter:
                break
        
        return "".join(res)