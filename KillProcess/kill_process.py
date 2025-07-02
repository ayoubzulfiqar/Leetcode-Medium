import collections

class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        children = collections.defaultdict(list)
        for i in range(len(pid)):
            children[ppid[i]].append(pid[i])

        queue = collections.deque([kill])
        
        killed_processes = []

        while queue:
            current_pid = queue.popleft()
            killed_processes.append(current_pid)
            
            for child_pid in children[current_pid]:
                queue.append(child_pid)
                
        return killed_processes