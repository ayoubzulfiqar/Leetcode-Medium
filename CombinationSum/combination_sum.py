class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        
        candidates.sort() 
        
        def backtrack(remaining_target, current_combination, start_index):
            if remaining_target == 0:
                results.append(list(current_combination))
                return
            
            if remaining_target < 0:
                return
            
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                if candidate > remaining_target:
                    break 
                
                current_combination.append(candidate)
                backtrack(remaining_target - candidate, current_combination, i)
                current_combination.pop() 
                
        backtrack(target, [], 0)
        return results