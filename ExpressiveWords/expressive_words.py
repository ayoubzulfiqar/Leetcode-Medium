class Solution:
    def _get_groups(self, text: str):
        if not text:
            return []
        groups = []
        i = 0
        while i < len(text):
            char = text[i]
            count = 0
            j = i
            while j < len(text) and text[j] == char:
                count += 1
                j += 1
            groups.append((char, count))
            i = j
        return groups

    def expressiveWords(self, s: str, words: list[str]) -> int:
        s_groups = self._get_groups(s)
        
        stretchy_count = 0
        for word in words:
            w_groups = self._get_groups(word)
            
            if len(s_groups) != len(w_groups):
                continue
                
            is_current_word_stretchy = True
            for i in range(len(s_groups)):
                char_s, count_s = s_groups[i]
                char_w, count_w = w_groups[i]
                
                if char_s != char_w:
                    is_current_word_stretchy = False
                    break
                
                if count_s < count_w:
                    is_current_word_stretchy = False
                    break
                
                if count_s > count_w:
                    if count_s < 3:
                        is_current_word_stretchy = False
                        break
                
            if is_current_word_stretchy:
                stretchy_count += 1
                
        return stretchy_count