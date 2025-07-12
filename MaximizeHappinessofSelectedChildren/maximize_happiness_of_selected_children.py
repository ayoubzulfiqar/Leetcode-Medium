class Solution:
    def maximizeHappiness(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        
        total_happiness = 0
        
        for i in range(k):
            current_child_happiness = happiness[i] - i
            
            if current_child_happiness < 0:
                current_child_happiness = 0
            
            total_happiness += current_child_happiness
            
        return total_happiness