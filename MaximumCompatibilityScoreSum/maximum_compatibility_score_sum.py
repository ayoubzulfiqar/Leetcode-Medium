class Solution:
    def maxCompatibilitySum(self, students: list[list[int]], mentors: list[list[int]]) -> int:
        m = len(students)
        n = len(students[0])

        scores = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                current_score = 0
                for k in range(n):
                    if students[i][k] == mentors[j][k]:
                        current_score += 1
                scores[i][j] = current_score

        memo = {}

        def solve(student_idx, used_mentors_mask):
            if student_idx == m:
                return 0

            if (student_idx, used_mentors_mask) in memo:
                return memo[(student_idx, used_mentors_mask)]

            max_current_score = 0
            for mentor_idx in range(m):
                if not (used_mentors_mask & (1 << mentor_idx)):
                    current_pair_score = scores[student_idx][mentor_idx]
                    
                    remaining_score = solve(student_idx + 1, used_mentors_mask | (1 << mentor_idx))
                    
                    max_current_score = max(max_current_score, current_pair_score + remaining_score)
            
            memo[(student_idx, used_mentors_mask)] = max_current_score
            return max_current_score

        return solve(0, 0)