import heapq

class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = []
        for i in range(len(difficulty)):
            jobs.append((difficulty[i], profit[i]))
        
        jobs.sort()
        worker.sort()
        
        max_total_profit = 0
        current_job_index = 0
        
        available_profits_heap = [] 
        
        for w_ability in worker:
            while current_job_index < len(jobs) and jobs[current_job_index][0] <= w_ability:
                heapq.heappush(available_profits_heap, -jobs[current_job_index][1])
                current_job_index += 1
            
            if available_profits_heap:
                max_profit_for_this_worker = -heapq.heappop(available_profits_heap)
                max_total_profit += max_profit_for_this_worker
                
        return max_total_profit