import collections

class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        task_counts = collections.Counter(tasks)
        
        total_rounds = 0
        for count in task_counts.values():
            if count == 1:
                return -1
            
            # For any count c >= 2:
            # If c % 3 == 0, rounds = c // 3
            # If c % 3 == 1, rounds = c // 3 + 1 (e.g., 4 tasks -> two 2-task rounds = 2 rounds; 7 tasks -> one 3-task, two 2-task rounds = 3 rounds)
            # If c % 3 == 2, rounds = c // 3 + 1 (e.g., 2 tasks -> one 2-task round = 1 round; 5 tasks -> one 3-task, one 2-task round = 2 rounds)
            # This logic can be compactly expressed as (count + 2) // 3 using integer division.
            total_rounds += (count + 2) // 3
            
        return total_rounds