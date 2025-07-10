import itertools

class Solution:
    def shortestStringThatContainsThreeStrings(self, a: str, b: str, c: str) -> str:
        
        def combine(s1, s2):
            if s2 in s1:
                return s1
            if s1 in s2:
                return s2

            best_overlap_len_12 = 0
            for i in range(min(len(s1), len(s2)), 0, -1):
                if s1[-i:] == s2[:i]:
                    best_overlap_len_12 = i
                    break
            res12 = s1 + s2[best_overlap_len_12:]

            best_overlap_len_21 = 0
            for i in range(min(len(s1), len(s2)), 0, -1):
                if s2[-i:] == s1[:i]:
                    best_overlap_len_21 = i
                    break
            res21 = s2 + s1[best_overlap_len_21:]

            if len(res12) < len(res21):
                return res12
            elif len(res21) < len(res12):
                return res21
            else:
                return min(res12, res21)

        strings = [a, b, c]
        
        min_len = float('inf')
        result_str = ""

        for p in itertools.permutations(strings):
            s1, s2, s3 = p
            
            temp_combined = combine(s1, s2)
            final_combined_str = combine(temp_combined, s3)
            
            if len(final_combined_str) < min_len:
                min_len = len(final_combined_str)
                result_str = final_combined_str
            elif len(final_combined_str) == min_len:
                result_str = min(result_str, final_combined_str)
                
        return result_str