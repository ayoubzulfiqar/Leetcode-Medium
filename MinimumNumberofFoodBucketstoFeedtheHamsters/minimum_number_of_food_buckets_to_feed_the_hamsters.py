class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        arr = list(hamsters)
        buckets = 0

        for i in range(n):
            if arr[i] == 'H':
                if i > 0 and arr[i-1] == 'B':
                    continue 

                if i < n - 1 and arr[i+1] == '.':
                    arr[i+1] = 'B'
                    buckets += 1
                elif i > 0 and arr[i-1] == '.':
                    arr[i-1] = 'B'
                    buckets += 1
                else:
                    return -1
        
        return buckets