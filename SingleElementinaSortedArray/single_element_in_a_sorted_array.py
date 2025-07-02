class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            # Ensure mid is at an even index.
            # This way, nums[mid] should be the first element of a pair
            # if the single element is to its right.
            if mid % 2 == 1:
                mid -= 1

            # Check if nums[mid] and nums[mid+1] form a pair.
            if nums[mid] == nums[mid+1]:
                # If they are equal, it means the single element is
                # in the subarray to the right of this pair.
                # Move low pointer past this pair.
                low = mid + 2
            else:
                # If they are not equal, it means nums[mid] is either
                # the single element itself, or the single element is
                # in the subarray to the left of mid (breaking the pair pattern).
                # The single element must be in the range [low, mid].
                # So, move high pointer to mid.
                high = mid
        
        # When the loop terminates, low will be equal to high,
        # and this index will point to the single non-duplicate element.
        return nums[low]