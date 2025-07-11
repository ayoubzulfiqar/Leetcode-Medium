class Solution:
    def countSetBits(self, n: int) -> int:
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count

    def canBeSorted(self, nums: list[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        bit_counts = [self.countSetBits(num) for num in nums]

        start_idx = 0
        for i in range(n):
            if i == n - 1 or bit_counts[i+1] != bit_counts[i]:
                segment = nums[start_idx : i+1]
                segment.sort()
                
                for j in range(len(segment)):
                    nums[start_idx + j] = segment[j]
                
                start_idx = i + 1
        
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                return False
        
        return True