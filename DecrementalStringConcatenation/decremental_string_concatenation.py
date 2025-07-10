import collections

class Solution:
    def minimizeLength(self, words: list[str]) -> int:
        n = len(words)

        # dp_prev stores { (first_char, last_char): min_length } for the previous step
        # dp_curr stores { (first_char, last_char): min_length } for the current step
        dp_prev = {}

        # Base case: str0 = words[0]
        first_char_0 = words[0][0]
        last_char_0 = words[0][-1]
        length_0 = len(words[0])
        dp_prev[(first_char_0, last_char_0)] = length_0

        for i in range(1, n):
            dp_curr = collections.defaultdict(lambda: float('inf'))
            current_word = words[i]
            current_word_first = current_word[0]
            current_word_last = current_word[-1]
            current_word_len = len(current_word)

            for (prev_first, prev_last), prev_len in dp_prev.items():
                # Option 1: new_str = join(prev_str, current_word)
                # The first character of the new string is the first character of prev_str
                new_first_1 = prev_first
                # The last character of the new string is the last character of current_word
                new_last_1 = current_word_last
                
                # Calculate length
                new_len_1 = prev_len + current_word_len
                # If last char of prev_str matches first char of current_word, one char is deleted
                if prev_last == current_word_first:
                    new_len_1 -= 1
                
                # Update dp_curr with the minimum length found for this (new_first, new_last) pair
                dp_curr[(new_first_1, new_last_1)] = min(dp_curr[(new_first_1, new_last_1)], new_len_1)

                # Option 2: new_str = join(current_word, prev_str)
                # The first character of the new string is the first character of current_word
                new_first_2 = current_word_first
                # The last character of the new string is the last character of prev_str
                new_last_2 = prev_last
                
                # Calculate length
                new_len_2 = current_word_len + prev_len
                # If last char of current_word matches first char of prev_str, one char is deleted
                if current_word_last == prev_first:
                    new_len_2 -= 1
                
                # Update dp_curr with the minimum length found for this (new_first, new_last) pair
                dp_curr[(new_first_2, new_last_2)] = min(dp_curr[(new_first_2, new_last_2)], new_len_2)
            
            # Move to the next iteration: current dp_curr becomes the previous dp_prev
            dp_prev = dp_curr

        # After processing all words, the minimum length is the minimum value in the final dp_prev
        return min(dp_prev.values())