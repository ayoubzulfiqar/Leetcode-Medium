class Solution:
    def substringXorQueries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        val_map = {}
        n = len(s)
        # Maximum possible target value is < 2^31 (approx 2 * 10^9).
        # A number up to 2^31 - 1 requires 31 bits.
        # So, we only need to consider substrings up to length 31 (or 32 for safety).
        MAX_BITS = 32 

        for left in range(n):
            if s[left] == '0':
                # Special case for the value 0. The shortest representation is "0".
                # We store the first encountered "0" (minimum left index) as the answer for value 0.
                if 0 not in val_map or left < val_map[0][0]:
                    val_map[0] = [left, left]
                # Substrings starting with '0' (e.g., "01", "001") are not canonical binary representations
                # and would be longer than their canonical counterparts (e.g., "1", "1").
                # The problem asks for the shortest substring. So, we only process '0' itself for value 0.
                continue

            # Process substrings starting with '1'
            current_val = 0
            # Iterate 'right' to form substrings s[left:right+1]
            # Limit the length of substrings to MAX_BITS, as larger values are out of target range.
            for right in range(left, min(n, left + MAX_BITS)):
                bit = int(s[right])
                current_val = (current_val << 1) | bit

                # If current_val exceeds the maximum possible target value (2^31 - 1),
                # any further extension will also exceed it, so we can break.
                if current_val >= (1 << 31): 
                    break 
                
                length = right - left + 1
                
                if current_val not in val_map:
                    val_map[current_val] = [left, right]
                else:
                    existing_left, existing_right = val_map[current_val]
                    existing_length = existing_right - existing_left + 1
                    
                    # Prioritize shorter length
                    if length < existing_length:
                        val_map[current_val] = [left, right]
                    # If lengths are equal, prioritize smaller left index
                    elif length == existing_length and left < existing_left:
                        val_map[current_val] = [left, right]

        ans = []
        for first, second in queries:
            target_val = first ^ second
            if target_val in val_map:
                ans.append(val_map[target_val])
            else:
                ans.append([-1, -1])
        
        return ans