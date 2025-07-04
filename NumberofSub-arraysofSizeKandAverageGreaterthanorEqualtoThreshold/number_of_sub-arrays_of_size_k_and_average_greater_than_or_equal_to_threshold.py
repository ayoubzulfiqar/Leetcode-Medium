def numOfSubarrays(arr, k, threshold):
    n = len(arr)
    count = 0
    current_sum = 0
    
    for i in range(k):
        current_sum += arr[i]
        
    if current_sum >= threshold * k:
        count += 1
        
    for i in range(k, n):
        current_sum = current_sum - arr[i - k] + arr[i]
        if current_sum >= threshold * k:
            count += 1
            
    return count