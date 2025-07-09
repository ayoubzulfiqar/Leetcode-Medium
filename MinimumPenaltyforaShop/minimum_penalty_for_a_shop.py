class Solution:
    def minPenalty(self, customers: str) -> int:
        n = len(customers)
        
        current_penalty = customers.count('Y')
        
        min_penalty = current_penalty
        best_j = 0
        
        for j in range(1, n + 1):
            if customers[j-1] == 'Y':
                current_penalty -= 1
            else: # customers[j-1] == 'N'
                current_penalty += 1
            
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_j = j
                
        return best_j