import bisect

class Solution:
    def mostBeautifulItem(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort()

        processed_items = []
        current_max_beauty = 0
        for price, beauty in items:
            current_max_beauty = max(current_max_beauty, beauty)
            
            if not processed_items or price > processed_items[-1][0]:
                processed_items.append([price, current_max_beauty])
            else:
                processed_items[-1][1] = current_max_beauty

        answers = []
        for query_val in queries:
            idx = bisect.bisect_right(processed_items, [query_val, float('inf')])
            
            if idx == 0:
                answers.append(0)
            else:
                answers.append(processed_items[idx-1][1])
                
        return answers