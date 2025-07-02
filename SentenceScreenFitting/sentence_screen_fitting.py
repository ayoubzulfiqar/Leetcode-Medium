class Solution:
    def wordsFitting(self, sentence: list[str], rows: int, cols: int) -> int:
        n = len(sentence)
        
        # next_word_idx_after_row[i] stores the index of the word that will start the next row,
        # if the current row started with sentence[i].
        next_word_idx_after_row = [0] * n
        
        # sentences_completed_on_row[i] stores the number of full sentences completed on the current row,
        # if the current row started with sentence[i].
        sentences_completed_on_row = [0] * n
        
        # Precomputation: For each possible starting word, calculate what happens on one row.
        # This loop iterates N times, where N is the number of words in the sentence.
        for start_idx in range(n):
            current_col = 0
            current_word_ptr = start_idx
            sentences_on_this_row = 0
            
            # Simulate filling one row starting with sentence[start_idx]
            while True:
                word_len = len(sentence[current_word_ptr])
                
                # Check if the current word fits on the current line
                # We need space for the word itself.
                if current_col + word_len <= cols:
                    current_col += word_len
                    
                    # Add space after the word. This space will be used if another word follows on the same line.
                    # If no word follows, this space is effectively at the end of the line and not used by text.
                    current_col += 1 
                    
                    current_word_ptr = (current_word_ptr + 1) % n
                    
                    if current_word_ptr == 0: # A full sentence has been completed
                        sentences_on_this_row += 1
                else:
                    # Current word does not fit, so this row is complete.
                    break
            
            next_word_idx_after_row[start_idx] = current_word_ptr
            sentences_completed_on_row[start_idx] = sentences_on_this_row
            
        # Simulate filling the entire screen using the precomputed values.
        # This loop iterates 'rows' times.
        total_sentences = 0
        current_word_idx = 0 # Start with the first word of the sentence (index 0)
        
        for _ in range(rows):
            total_sentences += sentences_completed_on_row[current_word_idx]
            current_word_idx = next_word_idx_after_row[current_word_idx]
            
        return total_sentences

```