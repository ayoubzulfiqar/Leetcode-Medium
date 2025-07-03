class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        n = len(arr1)
        
        max_overall_diff = 0
        
        # Iterate through all 8 combinations of signs for the three terms:
        # s1 for arr1[k], s2 for arr2[k], s3 for k
        # The expression |A-B| + |C-D| + |E-F| can be rewritten as
        # max_s1,s2,s3 (s1*(A-B) + s2*(C-D) + s3*(E-F))
        # which is max_s1,s2,s3 ( (s1*A + s2*C + s3*E) - (s1*B + s2*D + s3*F) )
        # For a fixed set of signs (s1, s2, s3), we want to maximize
        # (s1*arr1[i] + s2*arr2[i] + s3*i) - (s1*arr1[j] + s2*arr2[j] + s3*j)
        # This is equivalent to finding the maximum difference between any two values
        # of the transformed expression (s1*arr1[k] + s2*arr2[k] + s3*k) over all k.
        # This maximum difference is simply max_k(transformed_val_k) - min_k(transformed_val_k).
        
        for s1 in [-1, 1]:
            for s2 in [-1, 1]:
                for s3 in [-1, 1]:
                    
                    current_min_transformed_val = float('inf')
                    current_max_transformed_val = float('-inf')
                    
                    for k in range(n):
                        # Calculate the transformed value for the current index k
                        transformed_val = s1 * arr1[k] + s2 * arr2[k] + s3 * k
                        
                        # Update the minimum and maximum transformed values
                        # for this specific sign combination (s1, s2, s3)
                        current_min_transformed_val = min(current_min_transformed_val, transformed_val)
                        current_max_transformed_val = max(current_max_transformed_val, transformed_val)
                    
                    # The difference between the max and min transformed values
                    # for this sign combination is a candidate for the overall maximum.
                    max_overall_diff = max(max_overall_diff, current_max_transformed_val - current_min_transformed_val)
                    
        return max_overall_diff