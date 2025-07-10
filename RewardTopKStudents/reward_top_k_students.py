class Solution:
    def rewardStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)

        student_scores = {}

        for i in range(len(report)):
            current_student_id = student_id[i]
            feedback_report = report[i]
            
            # Get current score for the student, default to 0 if not present
            current_score = student_scores.get(current_student_id, 0)
            
            words = feedback_report.split()
            for word in words:
                if word in positive_set:
                    current_score += 3
                elif word in negative_set:
                    current_score -= 1
            
            student_scores[current_student_id] = current_score
        
        # Prepare for sorting: list of (negative_score, student_id) tuples
        # Negative score ensures non-increasing order for points
        # Positive student_id ensures increasing order for ties
        student_ranking_data = []
        for sid, score in student_scores.items():
            student_ranking_data.append((-score, sid))
            
        # Sort the list based on the tuple elements
        student_ranking_data.sort()
        
        # Extract the top k student IDs
        result = []
        for i in range(k):
            result.append(student_ranking_data[i][1]) # student_ranking_data[i][1] is the original student_id
            
        return result