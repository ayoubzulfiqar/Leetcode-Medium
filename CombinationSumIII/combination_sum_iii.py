class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        results = []

        def backtrack(current_combination, current_sum, start_num):
            # Base Case 1: If we have found k numbers
            if len(current_combination) == k:
                # Check if their sum equals n
                if current_sum == n:
                    results.append(list(current_combination)) # Append a copy of the combination
                return # Prune this path, as we've already picked k numbers

            # Base Case 2: Pruning conditions
            # If the current sum exceeds n, no need to continue this path
            if current_sum > n:
                return
            
            # If we pick more numbers, and the sum will definitely exceed n, or we can't pick enough numbers
            # (e.g., current_sum + start_num * (k - len(current_combination)) > n is another possible prune)
            # Or if we don't have enough remaining numbers to reach k elements
            # (9 - start_num + 1) is the count of numbers from start_num to 9
            # k - len(current_combination) is the count of numbers we still need
            if (9 - start_num + 1) < (k - len(current_combination)):
                return

            # Recursive Step: Iterate through possible numbers from start_num to 9
            for i in range(start_num, 10):
                # Pruning: If adding the current number 'i' makes the sum exceed 'n',
                # then any subsequent larger numbers will also exceed 'n', so we can break.
                if current_sum + i > n:
                    break
                
                # Pruning: If we don't have enough numbers left (including 'i') to reach 'k' elements
                # (10 - i) is the number of available numbers from 'i' to '9' (inclusive).
                # (k - len(current_combination) - 1) is the number of elements we still need to pick after 'i'.
                # So if (10 - i) < (k - len(current_combination)), we cannot form a combination of size k.
                # A more robust check: (9 - i + 1) < (k - len(current_combination))
                # This means, count of numbers from 'i' to '9' is less than the count of numbers we still need to pick.
                if (9 - i + 1) < (k - len(current_combination)):
                    break

                current_combination.append(i)
                backtrack(current_combination, current_sum + i, i + 1)
                current_combination.pop() # Backtrack: remove the last added number for the next iteration

        # Initial pruning based on the problem constraints:
        # Smallest possible sum for k numbers (1+2+...+k)
        min_possible_sum = k * (k + 1) // 2
        # Largest possible sum for k numbers (9+8+...+(9-k+1))
        max_possible_sum = k * (19 - k) // 2

        if n < min_possible_sum or n > max_possible_sum:
            return []

        # Start the backtracking process
        # An empty combination, initial sum 0, and numbers starting from 1
        backtrack([], 0, 1)
        return results