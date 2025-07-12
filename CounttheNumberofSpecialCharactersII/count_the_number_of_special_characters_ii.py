class Solution:
    def countSpecialCharacters(self, word: str) -> int:
        # Initialize arrays to store the first and last occurrence index for each character.
        # Indices 0-25 map to 'a'-'z', and 26-51 map to 'A'-'Z'.
        first_occurrence = [-1] * 52
        last_occurrence = [-1] * 52

        # Populate first_occurrence and last_occurrence arrays
        for i, char in enumerate(word):
            if 'a' <= char <= 'z':
                # Calculate index for lowercase characters (0-25)
                idx = ord(char) - ord('a')
            else:  # 'A' <= char <= 'Z'
                # Calculate index for uppercase characters (26-51)
                idx = ord(char) - ord('A') + 26
            
            # If this is the first time we see this character, record its index
            if first_occurrence[idx] == -1:
                first_occurrence[idx] = i
            
            # Always update the last occurrence index
            last_occurrence[idx] = i
        
        special_count = 0
        # Iterate through each possible letter 'a' through 'z'
        for i in range(26):
            # Get the indices for the lowercase and uppercase versions of the current letter
            lower_char_map_idx = i         # e.g., 'a' maps to 0
            upper_char_map_idx = i + 26    # e.g., 'A' maps to 26
            
            # Check if both the lowercase and uppercase versions of the letter exist in the word
            if last_occurrence[lower_char_map_idx] != -1 and first_occurrence[upper_char_map_idx] != -1:
                # If both exist, check the condition:
                # Every lowercase occurrence must appear before the first uppercase occurrence.
                # This is equivalent to checking if the last lowercase occurrence is before the first uppercase occurrence.
                if last_occurrence[lower_char_map_idx] < first_occurrence[upper_char_map_idx]:
                    special_count += 1
                    
        return special_count