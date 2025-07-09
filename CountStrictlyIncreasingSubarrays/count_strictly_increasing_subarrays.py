def countStrictlyIncreasingSubarrays(arr):
    n = len(arr)
    if n == 0:
        return 0

    count = 0
    current_length = 0

    for i in range(n):
        # If it's the first element or the current element does not extend the increasing sequence
        # (i.e., it's less than or equal to the previous element),
        # a new strictly increasing sequence of length 1 starts.
        if i == 0 or arr[i] <= arr[i-1]:
            current_length = 1
        else:
            # The current element extends the increasing sequence.
            current_length += 1
        
        # Add all strictly increasing subarrays ending at the current index 'i'.
        # If current_length is k, it means there are k such subarrays:
        # [arr[i]], [arr[i-1], arr[i]], ..., [arr[i-k+1], ..., arr[i]]
        count += current_length
    
    return count