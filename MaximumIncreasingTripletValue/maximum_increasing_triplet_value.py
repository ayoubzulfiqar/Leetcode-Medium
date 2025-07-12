def maxIncreasingTripletValue(arr):
    n = len(arr)
    if n < 3:
        return 0

    smaller_left = [-1] * n
    for i in range(n):
        max_val_left = -1
        for j in range(i):
            if arr[j] < arr[i]:
                max_val_left = max(max_val_left, arr[j])
        smaller_left[i] = max_val_left

    greater_right = [-1] * n
    
    suffix_max = [-1] * n
    if n > 0:
        suffix_max[n-1] = arr[n-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(arr[i], suffix_max[i+1])

    for i in range(n):
        if i + 1 < n and arr[i] < suffix_max[i+1]:
            greater_right[i] = suffix_max[i+1]

    max_sum = 0 

    for i in range(n):
        if smaller_left[i] != -1 and greater_right[i] != -1:
            current_sum = smaller_left[i] + arr[i] + greater_right[i]
            max_sum = max(max_sum, current_sum)

    return max_sum