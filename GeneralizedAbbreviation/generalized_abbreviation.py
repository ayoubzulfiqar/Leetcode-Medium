class Solution:
    def generateAbbreviations(self, word: str) -> list[str]:
        res = []
        n = len(word)

        def backtrack(index, current_abbr_parts, count):
            if index == n:
                if count > 0:
                    res.append("".join(current_abbr_parts) + str(count))
                else:
                    res.append("".join(current_abbr_parts))
                return

            # Option 1: Abbreviate the current character (or continue an existing abbreviation)
            backtrack(index + 1, current_abbr_parts, count + 1)

            # Option 2: Keep the current character (end any ongoing abbreviation and then append the character)
            # If there's an ongoing abbreviation, first append its count to current_abbr_parts
            if count > 0:
                current_abbr_parts.append(str(count))
            
            # Append the current character from the word
            current_abbr_parts.append(word[index])
            
            # Recurse with count reset to 0 (since we just kept a character)
            backtrack(index + 1, current_abbr_parts, 0)
            
            # Backtrack: remove the appended character(s) to restore state for other branches
            current_abbr_parts.pop() # Remove the character word[index]
            if count > 0:
                current_abbr_parts.pop() # Remove the count string if it was added

        backtrack(0, [], 0)
        return res