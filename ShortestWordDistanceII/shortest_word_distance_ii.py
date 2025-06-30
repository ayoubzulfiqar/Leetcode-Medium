from typing import List
from collections import defaultdict
import math

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_indices = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.word_indices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        list1 = self.word_indices[word1]
        list2 = self.word_indices[word2]

        p1 = 0
        p2 = 0
        min_dist = math.inf

        while p1 < len(list1) and p2 < len(list2):
            idx1 = list1[p1]
            idx2 = list2[p2]

            min_dist = min(min_dist, abs(idx1 - idx2))

            if idx1 < idx2:
                p1 += 1
            else:
                p2 += 1
        return min_dist