import heapq
from typing import List, Tuple, Dict

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_details: Dict[int, Tuple[int, int]] = {}
        self.priority_queue: List[Tuple[int, int]] = []

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_details[taskId] = (userId, priority)
        heapq.heappush(self.priority_queue, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task_details[taskId][0]
        self.task_details[taskId] = (userId, newPriority)
        heapq.heappush(self.priority_queue, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_details:
            del self.task_details[taskId]

    def execTop(self) -> int:
        while self.priority_queue:
            neg_priority, neg_taskId = heapq.heappop(self.priority_queue)
            current_priority = -neg_priority
            current_taskId = -neg_taskId

            if current_taskId in self.task_details and \
               self.task_details[current_taskId][1] == current_priority:
                
                userId = self.task_details[current_taskId][0]
                del self.task_details[current_taskId]
                return userId
        
        return -1