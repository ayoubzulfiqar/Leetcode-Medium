def placeWordInCrossword(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def can_place(segment_str: str, target_word: str) -> bool:
        """
        Checks if target_word can be placed in segment_str.
        segment_str must be exactly the length of target_word.
        Each char in segment_str must be ' ' or match the char in target_word.
        """
        L = len(segment_str)
        W = len(target_word)

        if L != W:
            return False

        for i in range(L):
            if segment_str[i] != ' ' and segment_str[i] != target_word[i]:
                return False
        return True

    words_to_check = [word, word[::-1]]

    # Check rows (horizontal placement)
    for r in range(m):
        row_str = "".join(board[r])
        segments = row_str.split('#')
        for segment in segments:
            for w in words_to_check:
                if can_place(segment, w):
                    return True

    # Check columns (vertical placement)
    for c in range(n):
        col_chars = [board[r][c] for r in range(m)]
        col_str = "".join(col_chars)
        segments = col_str.split('#')
        for segment in segments:
            for w in words_to_check:
                if can_place(segment, w):
                    return True

    return False