class MagicDictionary:

    def __init__(self):
        self.dictionary = []

    def buildDict(self, dictionary: list[str]) -> None:
        self.dictionary = dictionary

    def search(self, searchWord: str) -> bool:
        for dict_word in self.dictionary:
            if len(dict_word) != len(searchWord):
                continue

            diff_count = 0
            for i in range(len(searchWord)):
                if dict_word[i] != searchWord[i]:
                    diff_count += 1
                if diff_count > 1:
                    break

            if diff_count == 1:
                return True
        return False