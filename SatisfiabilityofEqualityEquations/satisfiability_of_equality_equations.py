class DSU:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def equationsPossible(equations: list[str]) -> bool:
    dsu = DSU(26) # 26 lowercase letters 'a' through 'z'

    # Process all equality equations first
    for eq in equations:
        if eq[1:3] == "==":
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            dsu.union(x, y)

    # Then process all inequality equations
    for eq in equations:
        if eq[1:3] == "!=":
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            # If x and y are in the same set, it means they must be equal,
            # which contradicts the inequality.
            if dsu.find(x) == dsu.find(y):
                return False

    return True