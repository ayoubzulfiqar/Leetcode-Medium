class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, word):
        if word not in self.parent:
            self.parent[word] = word
            return word
        
        if self.parent[word] == word:
            return word
        self.parent[word] = self.find(self.parent[word])
        return self.parent[word]

    def union(self, word1, word2):
        root1 = self.find(word1)
        root2 = self.find(word2)

        if root1 != root2:
            self.parent[root1] = root2
            return True
        return False

def areSentencesSimilarTwo(words1, words2, pairs):
    if len(words1) != len(words2):
        return False

    dsu = DSU()

    for w1, w2 in pairs:
        dsu.union(w1, w2)

    for i in range(len(words1)):
        word1 = words1[i]
        word2 = words2[i]

        if word1 == word2:
            continue
        
        if dsu.find(word1) != dsu.find(word2):
            return False
            
    return True