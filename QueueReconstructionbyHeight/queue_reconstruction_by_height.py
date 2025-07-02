class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        
        result = []
        
        for p in people:
            result.insert(p[1], p)
            
        return result