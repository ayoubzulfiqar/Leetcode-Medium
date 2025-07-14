def findMirrorScore(s: str) -> int:
    def get_mirror(char_c):
        return chr(ord('a') + (ord('z') - ord(char_c)))

    score = 0
    # available_indices is a dictionary where keys are characters ('a' through 'z')
    # and values are lists of indices.
    # Each list stores the indices where that character appeared and is currently unmarked
    # and available for a match.
    # We append indices to the end of the list and pop from the end to get the
    # largest (closest) available index.
    available_indices = {chr(ord('a') + i): [] for i in range(26)}

    for i in range(len(s)):
        current_char = s[i]
        mirror_char = get_mirror(current_char)

        # Check if there's an available unmarked index for the mirror character
        if available_indices[mirror_char]:
            # Found a match! Get the closest available index j (largest j < i)
            j = available_indices[mirror_char].pop()
            score += (i - j)
        else:
            # No match found for current_char's mirror.
            # So, current_char at index i becomes available for future matches.
            available_indices[current_char].append(i)

    return score