import collections

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = collections.Counter(tasks)
        
        max_freq = 0
        for count in task_counts.values():
            if count > max_freq:
                max_freq = count
        
        count_of_max_freq_tasks = 0
        for count in task_counts.values():
            if count == max_freq:
                count_of_max_freq_tasks += 1
        
        intervals_from_cooling = (max_freq - 1) * (n + 1) + count_of_max_freq_tasks
        
        return max(len(tasks), intervals_from_cooling)