class Solution:
    def _get_edit_distance(self, word1: str, word2: str) -> int:
        distance = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                distance += 1
        return distance

    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        result = []
        for query_word in queries:
            for dict_word in dictionary:
                if self._get_edit_distance(query_word, dict_word) <= 2:
                    result.append(query_word)
                    break
        return result