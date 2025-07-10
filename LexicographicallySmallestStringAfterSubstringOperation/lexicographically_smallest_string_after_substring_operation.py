class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        char_list = list(s)

        # Find the index of the first character that is not 'a'
        start_idx = -1
        for i in range(n):
            if char_list[i] != 'a':
                start_idx = i
                break

        if start_idx == -1:
            # If all characters are 'a', convert the last 'a' to 'z'
            char_list[n - 1] = 'z'
        else:
            # Apply the operation from start_idx until an 'a' is encountered
            # or the end of the string is reached.
            for j in range(start_idx, n):
                if char_list[j] == 'a':
                    # Stop if 'a' is encountered, as 'a' becomes 'z' which is undesirable
                    break
                else:
                    # Convert the character to its preceding letter
                    char_list[j] = chr(ord(char_list[j]) - 1)
        
        return "".join(char_list)