class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
            self.rank[i] = 0
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_j] < self.rank[root_i]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

class Solution:
    def areSentencesSynonymous(self, sentence1: str, sentence2: str, synonyms: list[list[str]]) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        if len(words1) != len(words2):
            return False

        dsu = DSU()
        for s1, s2 in synonyms:
            dsu.union(s1, s2)

        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]

            if word1 == word2:
                continue
            
            root1 = dsu.find(word1)
            root2 = dsu.find(word2)

            if root1 != root2:
                return False
        
        return True