class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_length_for_char(target_char: str) -> int:
            n = len(answerKey)
            left = 0
            count_other = 0 
            max_len = 0

            for right in range(n):
                if answerKey[right] != target_char:
                    count_other += 1
                
                while count_other > k:
                    if answerKey[left] != target_char:
                        count_other -= 1
                    left += 1
                
                max_len = max(max_len, right - left + 1)
            
            return max_len

        max_t = max_length_for_char('T')
        max_f = max_length_for_char('F')
        
        return max(max_t, max_f)