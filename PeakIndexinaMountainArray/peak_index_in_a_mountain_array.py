class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2
            
            if arr[mid] < arr[mid + 1]:
                # We are on the increasing slope, peak is to the right
                low = mid + 1
            else:
                # We are on the decreasing slope or at the peak
                # The peak is at mid or to its left
                high = mid
        
        # When low == high, this index is the peak
        return low