class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        jobs = []
        for i in range(len(difficulty)):
            jobs.append((difficulty[i], profit[i]))

        jobs.sort() 

        worker.sort() 

        total_profit = 0
        current_max_profit = 0
        job_idx = 0
        num_jobs = len(jobs)

        for w_ability in worker:
            while job_idx < num_jobs and jobs[job_idx][0] <= w_ability:
                current_max_profit = max(current_max_profit, jobs[job_idx][1])
                job_idx += 1
            
            total_profit += current_max_profit
            
        return total_profit