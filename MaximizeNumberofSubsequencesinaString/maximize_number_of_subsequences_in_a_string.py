class Solution:
    def maximizeSubsequences(self, text: str, pattern: str) -> int:
        p0 = pattern[0]
        p1 = pattern[1]

        original_subsequence_count = 0
        
        # current_p0_prefix_count tracks the number of p0s encountered so far
        # before the current character being processed.
        current_p0_prefix_count = 0 
        
        # total_p0_count and total_p1_count store the total occurrences
        # of p0 and p1 in the original text, respectively.
        total_p0_count = 0
        total_p1_count = 0

        for char in text:
            # If the current character is p1, it forms subsequences with all p0s
            # encountered before it.
            if char == p1:
                original_subsequence_count += current_p0_prefix_count
                total_p1_count += 1
            
            # If the current character is p0, increment the count of p0s seen so far.
            if char == p0:
                current_p0_prefix_count += 1
                total_p0_count += 1
        
        # Scenario 1: Add pattern[0] (p0) to the text.
        # To maximize subsequences, we should add p0 at the beginning of the text.
        # This new p0 will form a subsequence with every p1 in the original text.
        # The existing subsequences (original_subsequence_count) remain.
        res1 = original_subsequence_count + total_p1_count

        # Scenario 2: Add pattern[1] (p1) to the text.
        # To maximize subsequences, we should add p1 at the end of the text.
        # This new p1 will form a subsequence with every p0 in the original text.
        # The existing subsequences (original_subsequence_count) remain.
        res2 = original_subsequence_count + total_p0_count

        # Return the maximum of the two scenarios.
        return max(res1, res2)