class Solution:
    def getImportance(self, employees: list[list[int]], id: int) -> int:
        id_to_info = {}
        for emp_id, importance, subordinates in employees:
            id_to_info[emp_id] = (importance, subordinates)

        total_importance = 0
        
        stack = [id]
        
        while stack:
            current_id = stack.pop()
            
            importance, subordinates = id_to_info[current_id]
            
            total_importance += importance
            
            for sub_id in subordinates:
                stack.append(sub_id)
        
        return total_importance