import collections

class Solution:
    def uniqueSubstringsWithEqualDigitFrequency(self, s: str) -> int:
        n = len(s)
        unique_valid_substrings = set()

        for i in range(n):
            # current_counts will store the frequency of each character in the substring s[i...j]
            current_counts = collections.Counter()
            
            for j in range(i, n):
                char = s[j]
                current_counts[char] += 1
                
                # Check if the current substring s[i...j] satisfies the condition
                # Collect all non-zero frequencies for digits '0' through '9'
                frequencies_of_present_digits = []
                
                # Iterate through all possible digit characters ('0' to '9')
                for digit_code in range(ord('0'), ord('9') + 1):
                    digit_char = chr(digit_code)
                    if current_counts[digit_char] > 0:
                        frequencies_of_present_digits.append(current_counts[digit_char])
                
                is_current_substring_valid = False
                if frequencies_of_present_digits: # Ensure there is at least one digit in the substring
                    # Get the frequency of the first present digit
                    first_freq = frequencies_of_present_digits[0]
                    
                    # Check if all other present digits have the same frequency as the first
                    all_frequencies_are_equal = True
                    for freq in frequencies_of_present_digits:
                        if freq != first_freq:
                            all_frequencies_are_equal = False
                            break
                    
                    if all_frequencies_are_equal:
                        is_current_substring_valid = True
                
                # If the current substring is valid, add it to the set of unique valid substrings
                if is_current_substring_valid:
                    unique_valid_substrings.add(s[i:j+1])
        
        return len(unique_valid_substrings)

```