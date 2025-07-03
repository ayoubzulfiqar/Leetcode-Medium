class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)

        dp = {}
        max_chain_length = 0

        for word in words:
            current_word_chain_length = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    current_word_chain_length = max(current_word_chain_length, dp[predecessor] + 1)
            
            dp[word] = current_word_chain_length
            max_chain_length = max(max_chain_length, current_word_chain_length)
        
        return max_chain_length