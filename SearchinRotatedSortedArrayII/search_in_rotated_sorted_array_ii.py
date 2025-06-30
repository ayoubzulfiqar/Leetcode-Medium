import typing

class Solution:
    def search(self, nums: typing.List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates: if nums[low] == nums[mid] == nums[high],
            # we cannot determine which side is sorted.
            # In this case, we can safely shrink the search space by
            # moving low and high inwards.
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Determine which half is sorted
            if nums[low] <= nums[mid]: # Left half is sorted (or partially sorted up to mid)
                # Check if target is in the left sorted half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    # Target is in the right half (which might be rotated)
                    low = mid + 1
            else: # Right half is sorted (nums[mid] < nums[high] implies this, because nums[low] > nums[mid])
                # Check if target is in the right sorted half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    # Target is in the left half (which might be rotated)
                    high = mid - 1
        
        return False