class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        # Iterate from the largest possible side 'c', which is nums[k]
        # 'k' goes from n-1 down to 2, as we need at least 3 elements for a triangle.
        for k in range(n - 1, 1, -1):
            left = 0
            right = k - 1 # 'right' pointer starts just before 'k'

            # Use two pointers 'left' and 'right' to find 'a' and 'b'
            # such that nums[left] + nums[right] > nums[k]
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    # If nums[left] + nums[right] > nums[k], then
                    # nums[left] and nums[right] can form a triangle with nums[k].
                    #
                    # Also, since the array is sorted, any element nums[p]
                    # where 'left <= p < right' will satisfy nums[p] <= nums[right].
                    # Therefore, nums[p] + nums[right] >= nums[left] + nums[right] > nums[k].
                    # This means all elements from nums[left] up to nums[right-1]
                    # (inclusive) can form a triangle with nums[right] and nums[k].
                    # The number of such elements (and thus valid pairs) is (right - left).
                    count += (right - left)
                    
                    # Now, try to find smaller 'b' (nums[right]) values that might
                    # still form a triangle with nums[left] and nums[k], or
                    # to reduce the sum for the next iteration.
                    right -= 1
                else:
                    # If nums[left] + nums[right] <= nums[k], then nums[left] is too small.
                    # We need a larger 'a' value to satisfy the triangle inequality.
                    left += 1
        
        return count