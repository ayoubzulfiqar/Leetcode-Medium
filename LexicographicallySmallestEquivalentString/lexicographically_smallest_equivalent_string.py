class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]

        def find(char_code: int) -> int:
            if parent[char_code] == char_code:
                return char_code
            parent[char_code] = find(parent[char_code])
            return parent[char_code]

        def union(char1_code: int, char2_code: int):
            root1 = find(char1_code)
            root2 = find(char2_code)

            if root1 != root2:
                if root1 < root2:
                    parent[root2] = root1
                else:
                    parent[root1] = root2

        for i in range(len(s1)):
            char1_code = ord(s1[i]) - ord('a')
            char2_code = ord(s2[i]) - ord('a')
            union(char1_code, char2_code)

        result = []
        for char_b in baseStr:
            char_b_code = ord(char_b) - ord('a')
            smallest_equivalent_code = find(char_b_code)
            result.append(chr(ord('a') + smallest_equivalent_code))

        return "".join(result)