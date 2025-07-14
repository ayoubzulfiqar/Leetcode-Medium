import collections

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        if not fruits:
            return 0

        window_start = 0
        max_length = 0
        # Use a dictionary to store the frequency of each fruit type in the current window
        fruit_frequency = collections.defaultdict(int)
        
        # The problem "Fruits Into Baskets III" implies K=3 distinct fruit types (baskets).
        # This is a variation of "Longest Substring with At Most K Distinct Characters".
        K = 3

        # Iterate through the array with the window_end pointer
        for window_end in range(len(fruits)):
            right_fruit = fruits[window_end]
            fruit_frequency[right_fruit] += 1

            # Shrink the window from the left if the number of distinct fruit types exceeds K
            while len(fruit_frequency) > K:
                left_fruit = fruits[window_start]
                fruit_frequency[left_fruit] -= 1
                if fruit_frequency[left_fruit] == 0:
                    del fruit_frequency[left_fruit]
                window_start += 1
            
            # Update the maximum length of the subarray found so far
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length