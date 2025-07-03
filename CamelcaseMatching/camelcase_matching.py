class Solution:
    def camelMatch(self, queries: list[str], pattern: str) -> list[bool]:
        def _matches(query: str, pattern: str) -> bool:
            p_ptr = 0
            q_ptr = 0

            while q_ptr < len(query):
                if p_ptr < len(pattern) and query[q_ptr] == pattern[p_ptr]:
                    p_ptr += 1
                    q_ptr += 1
                elif query[q_ptr].isupper():
                    return False
                else:
                    q_ptr += 1
            
            return p_ptr == len(pattern)

        result = []
        for query_word in queries:
            result.append(_matches(query_word, pattern))
        
        return result