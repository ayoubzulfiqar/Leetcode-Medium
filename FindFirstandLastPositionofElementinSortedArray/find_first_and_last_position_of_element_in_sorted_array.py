class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first(arr, val):
            ans = -1
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == val:
                    ans = mid
                    high = mid - 1
                elif arr[mid] < val:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        def find_last(arr, val):
            ans = -1
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == val:
                    ans = mid
                    low = mid + 1
                elif arr[mid] < val:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        first_occurrence = find_first(nums, target)
        last_occurrence = find_last(nums, target)

        return [first_occurrence, last_occurrence]