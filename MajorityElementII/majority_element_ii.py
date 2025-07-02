class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []

        # Initialize candidates and their counts.
        # There can be at most two elements that appear more than n/3 times.
        cand1, count1 = 0, 0
        cand2, count2 = 0, 0

        # First pass: Find potential candidates
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                # If current num is different from both candidates,
                # and both counts are positive, decrement both counts.
                # This effectively cancels out three distinct elements.
                count1 -= 1
                count2 -= 1

        # Second pass: Verify the counts of the potential candidates
        # Reset counts for precise calculation
        count1_actual = 0
        count2_actual = 0
        
        for num in nums:
            if num == cand1:
                count1_actual += 1
            # Use elif to avoid double counting if cand1 and cand2 somehow ended up being the same value
            # (though with the logic, they should be distinct if both counts are > 0 after pass 1)
            elif num == cand2: 
                count2_actual += 1

        result = []
        n = len(nums)
        threshold = n // 3

        # Check if candidate1 is a majority element
        if count1_actual > threshold:
            result.append(cand1)
        
        # Check if candidate2 is a majority element
        # Ensure it's not the same as cand1 if cand1 was already added
        if cand2 != cand1 and count2_actual > threshold:
            result.append(cand2)
            
        return result