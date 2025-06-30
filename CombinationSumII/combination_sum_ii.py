class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        candidates.sort()

        def backtrack(current_combination, remaining_target, start_index):
            if remaining_target == 0:
                results.append(list(current_combination))
                return
            if remaining_target < 0:
                return

            for i in range(start_index, len(candidates)):
                # Skip duplicates: If the current number is the same as the previous one,
                # and we are not at the very beginning of this level of recursion (i > start_index),
                # then skip it to avoid duplicate combinations.
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue

                current_num = candidates[i]
                if current_num <= remaining_target:
                    current_combination.append(current_num)
                    # Move to the next index (i + 1) because each number can be used only once
                    backtrack(current_combination, remaining_target - current_num, i + 1)
                    current_combination.pop() # Backtrack

        backtrack([], target, 0)
        return results