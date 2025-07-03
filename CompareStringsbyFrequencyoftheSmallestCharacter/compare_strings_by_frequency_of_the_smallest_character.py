import bisect

class Solution:
    def f(self, s: str) -> int:
        smallest_char = min(s)
        return s.count(smallest_char)

    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        word_frequencies = []
        for word in words:
            word_frequencies.append(self.f(word))
        
        word_frequencies.sort()
        
        result = []
        for query_str in queries:
            query_freq = self.f(query_str)
            
            idx = bisect.bisect_right(word_frequencies, query_freq)
            count_greater = len(word_frequencies) - idx
            result.append(count_greater)
            
        return result