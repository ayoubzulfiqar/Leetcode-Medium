class Solution:
    def productOfTwoRunLengthEncodedArrays(self, encoded1: list[list[int]], encoded2: list[list[int]]) -> list[list[int]]:
        # Calculate the total length of the conceptual arrays
        total_len1 = sum(freq for _, freq in encoded1)
        total_len2 = sum(freq for _, freq in encoded2)
        max_total_len = max(total_len1, total_len2)

        res = []
        p1 = 0  # Pointer for encoded1
        p2 = 0  # Pointer for encoded2
        
        # Current value and remaining frequency for the run being processed from encoded1
        val1 = 0
        rem1 = 0 
        # Current value and remaining frequency for the run being processed from encoded2
        val2 = 0
        rem2 = 0

        current_idx = 0 # Represents the current index in the conceptual product array

        # Iterate as long as we haven't processed up to the maximum length of the conceptual arrays
        while current_idx < max_total_len:
            # If the current run from encoded1 is exhausted, get the next run
            # If encoded1 is fully consumed, subsequent values are treated as 0
            if rem1 == 0:
                if p1 < len(encoded1):
                    val1, rem1 = encoded1[p1]
                    p1 += 1
                else:
                    # encoded1 is exhausted, treat subsequent values as 0
                    val1 = 0
                    # The remaining frequency for these 0s is up to the max_total_len
                    rem1 = max_total_len - current_idx 

            # If the current run from encoded2 is exhausted, get the next run
            # If encoded2 is fully consumed, subsequent values are treated as 0
            if rem2 == 0:
                if p2 < len(encoded2):
                    val2, rem2 = encoded2[p2]
                    p2 += 1
                else