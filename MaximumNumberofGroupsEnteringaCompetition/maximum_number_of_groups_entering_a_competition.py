class Solution:
    def maxNumberOfGroups(self, grades: list[int]) -> int:
        N = len(grades)
        
        k = 0
        students_used = 0
        while True:
            next_group_size = k + 1
            if students_used + next_group_size <= N:
                k = next_group_size
                students_used += k
            else:
                break
        
        return k