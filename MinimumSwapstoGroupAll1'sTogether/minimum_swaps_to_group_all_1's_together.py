class Solution:
    def minSwaps(self, data: list[int]) -> int:
        n = len(data)
        total_ones = sum(data)

        if total_ones <= 1:
            return 0

        # Calculate ones in the first window of size total_ones
        current_ones_in_window = 0
        for i in range(total_ones):
            current_ones_in_window += data[i]

        max_ones_in_window = current_ones_in_window

        # Slide the window
        for i in range(total_ones, n):
            current_ones_in_window += data[i]  # Add new element
            current_ones_in_window -= data[i - total_ones]  # Remove old element
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)

        # The number of zeros in the best window needs to be swapped out
        return total_ones - max_ones_in_window

# Example Usage (for testing, not part of the required output)
# sol = Solution()
# print(sol.minSwaps([1,0,1,0,1])) # Expected: 1
# print(sol.minSwaps([0,0,0,1,0,0,1,1,0,1])) # Expected: 3
# print(sol.minSwaps([1,0,1,1,0,0])) # Expected: 1
# print(sol.minSwaps([1,1,1,1,1])) # Expected: 0
# print(sol.minSwaps([0,0,0,0,0])) # Expected: 0
# print(sol.minSwaps([1])) # Expected: 0
# print(sol.minSwaps([0])) # Expected: 0