import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        n = len(tasks)
        
        tasks_with_indices = []
        for i in range(n):
            tasks_with_indices.append((tasks[i][0], tasks[i][1], i))
            
        tasks_with_indices.sort()
        
        processed_order = []
        
        available_tasks_heap = [] 
        
        current_time = 0
        task_idx = 0 
        
        while len(processed_order) < n:
            while task_idx < n and tasks_with_indices[task_idx][0] <= current_time:
                enqueue_time, proc_time, original_idx = tasks_with_indices[task_idx]
                heapq.heappush(available_tasks_heap, (proc_time, original_idx))
                task_idx += 1
            
            if not available_tasks_heap:
                current_time = tasks_with_indices[task_idx][0]
                continue 
            else:
                proc_time, original_idx = heapq.heappop(available_tasks_heap)
                processed_order.append(original_idx)
                current_time += proc_time
                
        return processed_order