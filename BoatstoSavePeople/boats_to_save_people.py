class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= right:
            boats += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            
        return boats