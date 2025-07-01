class ValidWordAbbr:
    def __init__(self, dictionary: list[str]):
        self.abbr_map = {}
        for word in dictionary:
            ab = self._get_abbr(word)
            if ab not in self.abbr_map:
                self.abbr_map[ab] = set()
            self.abbr_map[ab].add(word)

    def isUnique(self, word: str) -> bool:
        ab = self._get_abbr(word)
        if ab not in self.abbr_map:
            return True
        else:
            return self.abbr_map[ab] == {word}

    def _get_abbr(self, word: str) -> str:
        n = len(word)
        if n <= 2:
            return word
        return word[0] + str(n - 2) + word[-1]