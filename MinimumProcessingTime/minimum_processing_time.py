class Solution:
    def minimumProcessingTime(self, processorTime: list[int], tasks: list[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        max_overall_completion_time = 0
        num_processors = len(processorTime)

        for i in range(num_processors):
            processor_avail_time = processorTime[i]
            
            # Each processor has 4 cores. Tasks are assigned in blocks of 4.
            # Since tasks are sorted in descending order, the task at index i*4
            # will be the longest among the four tasks assigned to the current processor.
            longest_task_in_current_batch = tasks[i * 4] 
            
            current_processor_completion_time = processor_avail_time + longest_task_in_current_batch
            
            max_overall_completion_time = max(max_overall_completion_time, current_processor_completion_time)
            
        return max_overall_completion_time