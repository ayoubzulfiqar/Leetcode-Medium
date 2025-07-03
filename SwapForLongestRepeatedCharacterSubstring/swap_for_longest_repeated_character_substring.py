import collections

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        if n == 0:
            return 0

        counts = collections.Counter(text)

        blocks = []
        if n > 0:
            current_char = text[0]
            current_len = 0
            for i in range(n):
                if text[i] == current_char:
                    current_len += 1
                else:
                    blocks.append((current_char, current_len))
                    current_char = text[i]
                    current_len = 1
            blocks.append((current_char, current_len))

        max_len = 0
        if n > 0:
            max_len = 1 

        for char, length in blocks:
            if counts[char] > length:
                max_len = max(max_len, length + 1)
            else:
                max_len = max(max_len, length)

        for i in range(len(blocks) - 2):
            block1_char, block1_len = blocks[i]
            block_middle_char, block_middle_len = blocks[i+1]
            block2_char, block2_len = blocks[i+2]

            if block1_char == block2_char and block_middle_len == 1:
                char_to_merge = block1_char
                
                if counts[char_to_merge] > (block1_len + block2_len):
                    max_len = max(max_len, block1_len + block2_len + 1)
                else:
                    max_len = max(max_len, block1_len + block2_len)
        
        return max_len