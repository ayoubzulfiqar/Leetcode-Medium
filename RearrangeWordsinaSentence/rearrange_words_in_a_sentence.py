class Solution:
    def arrangeWords(self, text: str) -> str:
        words_lower = text.lower().split(' ')
        sorted_words = sorted(words_lower, key=len)
        if sorted_words:
            sorted_words[0] = sorted_words[0].capitalize()
        return ' '.join(sorted_words)