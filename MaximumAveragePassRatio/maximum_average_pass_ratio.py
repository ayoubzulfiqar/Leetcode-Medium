import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        pq = [] # Min-heap to store (-gain, current_pass, current_total)

        # Calculate initial gain for each class and push to heap
        # Gain for adding one student to [p, t] is (t - p) / (t * (t + 1))
        for p, t in classes:
            gain = (t - p) / (t * (t + 1))
            heapq.heappush(pq, (-gain, p, t))
            
        # Distribute extra students by repeatedly picking the class with the maximum gain
        for _ in range(extraStudents):
            if not pq:
                break # Should not happen based on constraints, but for robustness
            
            # Pop the class with the highest gain (smallest negative gain)
            neg_gain, current_p, current_t = heapq.heappop(pq)
            
            # Add one student to this class
            new_p = current_p + 1
            new_t = current_t + 1
            
            # Calculate the new gain for the updated class
            # If new_p == new_t, the ratio is 1.0, and no further gain is possible (gain is 0)
            if new_p == new_t:
                new_gain = 0.0
            else:
                new_gain = (new_t - new_p) / (new_t * (new_t + 1))
            
            # Push the updated class back to the heap with its new gain
            heapq.heappush(pq, (-new_gain, new_p, new_t))
            
        # Calculate the final average pass ratio
        total_pass_ratio_sum = 0.0
        num_classes = len(classes)
        
        # Iterate through the heap to sum up the final pass ratios
        while pq:
            _, final_p, final_t = heapq.heappop(pq)
            total_pass_ratio_sum += final_p / final_t
            
        return total_pass_ratio_sum / num_classes