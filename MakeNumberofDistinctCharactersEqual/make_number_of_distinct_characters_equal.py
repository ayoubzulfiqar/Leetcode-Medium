class Solution:
    def checkDistinct(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for char_code in map(ord, word1):
            freq1[char_code - ord('a')] += 1
        
        for char_code in map(ord, word2):
            freq2[char_code - ord('a')] += 1

        for i in range(26): # Index for character to be swapped from word1 (c1_idx)
            for j in range(26): # Index for character to be swapped from word2 (c2_idx)

                # Skip if the character to be swapped from word1 does not exist in word1,
                # or if the character to be swapped from word2 does not exist in word2.
                if freq1[i] == 0 or freq2[j] == 0:
                    continue

                # Create temporary copies of frequency arrays to simulate the swap
                temp_freq1 = list(freq1)
                temp_freq2 = list(freq2)

                # Simulate removing char i from word1 and adding char j to word1
                temp_freq1[i] -= 1
                temp_freq1[j] += 1

                # Simulate removing char j from word2 and adding char i to word2
                temp_freq2[j] -= 1
                temp_freq2[i] += 1

                # Calculate distinct characters for the modified word1
                distinct_count1 = 0
                for k in range(26):
                    if temp_freq1[k] > 0:
                        distinct_count1 += 1

                # Calculate distinct characters for the modified word2
                distinct_count2 = 0
                for k in range(26):
                    if temp_freq2[k] > 0:
                        distinct_count2 += 1

                # If distinct counts are equal, a valid swap is found
                if distinct_count1 == distinct_count2:
                    return True
        
        # If no valid swap is found after checking all possibilities
        return False