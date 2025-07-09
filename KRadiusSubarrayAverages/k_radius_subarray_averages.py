def getAverages(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    avgs = [-1] * n
    
    window_size = 2 * k + 1
    
    if k == 0:
        return list(nums)
    
    if window_size > n:
        return avgs
        
    current_sum = sum(nums[0:window_size])
    avgs[k] = current_sum // window_size
    
    for i in range(k + 1, n - k):
        current_sum = current_sum - nums[i - k - 1] + nums[i + k]
        avgs[i] = current_sum // window_size
            
    return avgs