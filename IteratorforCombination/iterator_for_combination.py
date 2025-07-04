class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.index = 0
        self._generate_combinations(characters, combinationLength, 0, [], self.combinations)

    def _generate_combinations(self, characters, length, start_index, current_combo, result_list):
        if len(current_combo) == length:
            result_list.append("".join(current_combo))
            return

        for i in range(start_index, len(characters)):
            current_combo.append(characters[i])
            self._generate_combinations(characters, length, i + 1, current_combo, result_list)
            current_combo.pop()

    def next(self) -> str:
        if self.hasNext():
            combo = self.combinations[self.index]
            self.index += 1
            return combo
        

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)