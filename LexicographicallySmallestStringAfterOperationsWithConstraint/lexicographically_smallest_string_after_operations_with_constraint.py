class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        n = len(s)
        result_chars = [''] * n

        for i in range(n):
            char_val = ord(s[i]) - ord('a')
            
            # Calculate the cost to change s[i] to 'a'
            # This is the minimum cyclic distance between s[i] and 'a'
            cost_to_a = min(char_val, 26 - char_val)

            if k >= cost_to_a:
                # If we have enough 'k' to change s[i] to 'a', do it.
                result_chars[i] = 'a'
                k -= cost_to_a
            else:
                # If we don't have enough 'k' to change s[i] to 'a',
                # we must use all remaining 'k' to change s[i] to the
                # lexicographically smallest character possible.
                # This means finding a character 't_char' such that
                # min_cyclic_dist(s[i], t_char) == k, and t_char is minimized.
                
                # There are two characters at a distance 'k' from s[i]:
                # 1. Moving 'k' steps forward (clockwise)
                target_val1 = (char_val + k) % 26
                # 2. Moving 'k' steps backward (counter-clockwise)
                #    Adding 26 before modulo ensures a positive result for negative differences
                target_val2 = (char_val - k + 26) % 26 

                # Convert the numerical values back to characters
                char1 = chr(ord('a') + target_val1)
                char2 = chr(ord('a') + target_val2)
                
                # Choose the lexicographically smaller of the two possible characters
                result_chars[i] = min(char1, char2)
                k = 0 # All remaining 'k' is used up

            # If 'k' becomes 0, no further changes are possible for subsequent characters.
            # Copy the rest of the original string and break the loop.
            if k == 0:
                for j in range(i + 1, n):
                    result_chars[j] = s[j]
                break 

        return "".join(result_chars)