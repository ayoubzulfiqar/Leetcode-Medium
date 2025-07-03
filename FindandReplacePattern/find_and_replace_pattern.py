class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        
        def matches(word: str, pattern: str) -> bool:
            p_to_w = {}
            w_to_p = {}

            for i in range(len(word)):
                p_char = pattern[i]
                w_char = word[i]

                if p_char in p_to_w:
                    if p_to_w[p_char] != w_char:
                        return False
                else:
                    p_to_w[p_char] = w_char
                
                if w_char in w_to_p:
                    if w_to_p[w_char] != p_char:
                        return False
                else:
                    w_to_p[w_char] = p_char
            
            return True

        result = []
        for word in words:
            if matches(word, pattern):
                result.append(word)
        
        return result