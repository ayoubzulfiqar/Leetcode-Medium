import collections

class Solution:
    def countPairs(self, s: str) -> int:
        n = len(s)
        
        substring_indices = collections.defaultdict(list)
        
        for i in range(n):
            for j in range(i, n):
                substring = s[i : j + 1]
                substring_indices[substring].append(i)
        
        min_overall_diff = float('inf')
        
        for indices_list in substring_indices.values():
            if len(indices_list) < 2:
                continue 
            
            indices_list.sort() 
            
            min_diff_for_sub = float('inf')
            for k in range(len(indices_list) - 1):
                current_diff = indices_list[k+1] - indices_list[k]
                min_diff_for_sub = min(min_diff_for_sub, current_diff)
            
            min_overall_diff = min(min_overall_diff, min_diff_for_sub)
            
        if min_overall_diff == float('inf'):
            return 0
            
        count = 0
        for indices_list in substring_indices.values():
            if len(indices_list) < 2:
                continue
            
            for k in range(len(indices_list) - 1):
                current_diff = indices_list[k+1] - indices_list[k]
                if current_diff == min_overall_diff:
                    count += 1
                    
        return count