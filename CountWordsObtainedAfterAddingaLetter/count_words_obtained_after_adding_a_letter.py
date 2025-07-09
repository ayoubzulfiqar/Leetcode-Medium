class Solution:
    def wordCount(self, startWords: list[str], targetWords: list[str]) -> int:
        def word_to_mask(word: str) -> int:
            mask = 0
            for char_code in map(ord, word):
                mask |= (1 << (char_code - ord('a')))
            return mask

        start_masks = set()
        for s_word in startWords:
            start_masks.add(word_to_mask(s_word))

        count = 0
        for t_word in targetWords:
            target_mask = word_to_mask(t_word)
            
            for i in range(26):
                char_bit = (1 << i) 
                
                if (target_mask & char_bit):
                    potential_start_mask = target_mask ^ char_bit
                    
                    if potential_start_mask in start_masks:
                        count += 1
                        break
        
        return count