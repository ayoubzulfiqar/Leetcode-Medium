import collections

class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        
        counts = collections.Counter(s)
        count0 = counts['0']
        count1 = counts['1']
        
        if abs(count0 - count1) > 1:
            return -1
            
        def calculate_mismatches(target_start_char):
            mismatches = 0
            for i in range(n):
                expected_char = target_start_char
                if i % 2 != 0: # For odd indices, the character should be the opposite of the start char
                    expected_char = '1' if target_start_char == '0' else '0'
                
                if s[i] != expected_char:
                    mismatches += 1
            return mismatches
            
        ans = float('inf')
        
        if n % 2 == 0: # Length is even, so count0 must equal count1
            # Both '0101...' and '1010...' are possible target patterns
            mismatches_start_0 = calculate_mismatches('0')
            mismatches_start_1 = calculate_mismatches('1')
            
            ans = min(mismatches_start_0 // 2, mismatches_start_1 // 2)
        else: # Length is odd
            # If count0 > count1, string must start with '0' (e.g., "010")
            if count0 > count1:
                mismatches_start_0 = calculate_mismatches('0')
                ans = mismatches_start_0 // 2
            # If count1 > count0, string must start with '1' (e.g., "101")
            else: # count1 > count0
                mismatches_start_1 = calculate_mismatches('1')
                ans = mismatches_start_1 // 2
                
        return ans