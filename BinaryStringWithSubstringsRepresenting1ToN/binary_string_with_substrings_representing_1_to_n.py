class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # Maximum length of binary representation for n (up to 10^9).
        # log2(10^9) is approximately 29.89, so the longest binary string
        # we need to consider will have 30 bits (e.g., bin(2^29) is 30 bits long).
        MAX_BIN_LEN = 30 

        # Use a set to store unique integers found as substrings
        found_nums = set()

        # Iterate through all possible substrings of s
        # We only need to consider substrings up to MAX_BIN_LEN in length
        for i in range(len(s)):
            # The inner loop iterates to form substrings starting at 'i'.
            # It goes up to MAX_BIN_LEN characters from 'i' or until the end of string s,
            # whichever comes first.
            for j in range(i, min(len(s), i + MAX_BIN_LEN)):
                sub = s[i : j+1]

                # Skip substrings that represent numbers with leading zeros (e.g., "01", "001")
                # as standard binary representations for numbers > 0 do not have leading zeros.
                if sub[0] == '0' and len(sub) > 1:
                    continue
                
                # Convert the binary substring to an integer
                val = int(sub, 2)

                # Optimization: If the current integer 'val' already exceeds 'n',
                # then any longer substring starting with 'sub' will also represent
                # an even larger number, which will also exceed 'n'.
                # So, we can safely break the inner loop for the current starting index 'i'.
                if val > n:
                    break
                
                # If the integer is within the range [1, n], add it to the set
                if 1 <= val <= n:
                    found_nums.add(val)
        
        # After populating found_nums, check if all integers from 1 to n are present.
        # The loop will run at most 'n' times. However, since 'found_nums' can contain
        # at most len(s) * MAX_BIN_LEN unique numbers (roughly 1000 * 30 = 30,000),
        # if 'n' is larger than this, the loop will quickly find a missing number
        # and return False, making this check efficient even for large 'n'.
        for k in range(1, n + 1):
            if k not in found_nums:
                return False
        
        # If the loop completes, it means all integers from 1 to n were found.
        return True