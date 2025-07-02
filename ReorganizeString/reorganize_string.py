import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counts = collections.Counter(s)

        pq = []
        for char, freq in counts.items():
            if freq > (n + 1) // 2:
                return ""
            heapq.heappush(pq, (-freq, char))

        res_list = []

        while len(pq) >= 2:
            freq1, char1 = heapq.heappop(pq)
            freq2, char2 = heapq.heappop(pq)

            res_list.append(char1)
            res_list.append(char2)

            freq1 += 1
            freq2 += 1

            if freq1 < 0:
                heapq.heappush(pq, (freq1, char1))
            if freq2 < 0:
                heapq.heappush(pq, (freq2, char2))
        
        if pq:
            freq, char = heapq.heappop(pq)
            if freq == -1:
                res_list.append(char)
            else:
                return "" # Should not be reached if initial check is correct

        return "".join(res_list)