class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        all_distinct_ors = set()
        
        prev_ors_ending_at_i_minus_1 = set() 
        
        for num in arr:
            current_ors_ending_at_i = set()
            
            current_ors_ending_at_i.add(num)
            
            for prev_or_val in prev_ors_ending_at_i_minus_1:
                current_ors_ending_at_i.add(prev_or_val | num)
            
            all_distinct_ors.update(current_ors_ending_at_i)
            
            prev_ors_ending_at_i_minus_1 = current_ors_ending_at_i
            
        return len(all_distinct_ors)