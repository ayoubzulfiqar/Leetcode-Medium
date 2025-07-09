class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        current_day = 0
        last_completion_time = {}

        for task in tasks:
            day_if_no_cooldown = current_day + 1
            
            if task in last_completion_time:
                last_day = last_completion_time[task]
                earliest_available_day = last_day + space + 1
                
                current_day = max(day_if_no_cooldown, earliest_available_day)
            else:
                current_day = day_if_no_cooldown
            
            last_completion_time[task] = current_day
            
        return current_day