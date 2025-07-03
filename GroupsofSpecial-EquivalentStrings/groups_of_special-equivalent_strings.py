class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        groups = set()
        for word in words:
            even_chars = []
            odd_chars = []
            for i, char in enumerate(word):
                if i % 2 == 0:
                    even_chars.append(char)
                else:
                    odd_chars.append(char)
            
            even_chars.sort()
            odd_chars.sort()
            
            signature = (tuple(even_chars), tuple(odd_chars))
            groups.add(signature)
            
        return len(groups)