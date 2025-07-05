def minDeletions(s: str) -> int:
    n = len(s)
    
    # a_count_right: keeps track of 'a's to the right of the current potential split point.
    # These 'a's would need to be deleted if they are in the 'b' part of the balanced string.
    a_count_right = s.count('a')
    
    # b_count_left: keeps track of 'b's to the left of the current potential split point.
    # These 'b's would need to be deleted if they are in the 'a' part of the balanced string.
    b_count_left = 0
    
    # min_deletions: stores the minimum deletions found so far.
    # Initialize with the case where the entire string becomes 'b's (split point at index 0).
    # In this case, all 'a's in the string must be deleted.
    min_deletions = a_count_right
    
    # Iterate through each character of the string.
    # At each iteration, we consider a potential split point after the current character.
    # The string is conceptually divided into s[0...i] (intended to be 'a's) and s[i+1...n-1] (intended to be 'b's).
    for char in s:
        if char == 'a':
            # If the current character is 'a', it moves from the 'right' part to the 'left' part.
            # It no longer contributes to 'a_count_right'.
            a_count_right -= 1
        else: # char == 'b'
            # If the current character is 'b', it moves from the 'right' part to the 'left' part.
            # Since the 'left' part should be 'a's, this 'b' must be deleted.
            # So, we increment b_count_left.
            b_count_left += 1
        
        # Calculate the total deletions for the current split point:
        # (b's on the left that need to be deleted) + (a's on the right that need to be deleted).
        current_deletions = b_count_left + a_count_right
        
        # Update the minimum deletions found so far.
        min_deletions = min(min_deletions, current_deletions)
            
    return min_deletions