class Solution:
    def maxProduct(self, words: list[str]) -> int:
        masks = {} 
        
        for word in words:
            mask = 0
            for char in word:
                mask |= (1 << (ord(char) - ord('a')))
            
            masks[mask] = max(masks.get(mask, 0), len(word))
            
        max_product = 0
        
        unique_words_data = list(masks.items())
        
        n = len(unique_words_data)
        
        for i in range(n):
            mask1, len1 = unique_words_data[i]
            for j in range(i + 1, n):
                mask2, len2 = unique_words_data[j]
                
                if (mask1 & mask2) == 0:
                    max_product = max(max_product, len1 * len2)
                    
        return max_product