class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        jobs.sort(reverse=True)

        low = max(jobs)
        high = sum(jobs)
        ans = high

        def check(time_limit: int) -> bool:
            worker_loads = [0] * k

            def dfs(job_index: int) -> bool:
                if job_index == len(jobs):
                    return True

                current_job = jobs[job_index]

                for i in range(k):
                    if worker_loads[i] + current_job <= time_limit:
                        worker_loads[i] += current_job
                        if dfs(job_index + 1):
                            return True
                        worker_loads[i] -= current_job

                    if worker_loads[i] == 0:
                        break

                return False

            return dfs(0)

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans