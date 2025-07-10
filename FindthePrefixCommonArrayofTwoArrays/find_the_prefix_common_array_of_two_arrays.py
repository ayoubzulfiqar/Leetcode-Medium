class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        C = []
        
        seen_A = set()
        seen_B = set()
        
        for i in range(n):
            seen_A.add(A[i])
            seen_B.add(B[i])
            
            common_elements_count = len(seen_A.intersection(seen_B))
            C.append(common_elements_count)
            
        return C