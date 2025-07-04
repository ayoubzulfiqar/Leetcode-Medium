class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        P = list(range(1, m + 1))
        results = []

        for query_val in queries:
            # Find the position of queries[i] in P
            pos = P.index(query_val)
            results.append(pos)

            # Move queries[i] to the beginning of P
            # Remove from current position
            val_to_move = P.pop(pos)
            # Insert at the beginning
            P.insert(0, val_to_move)
            
        return results