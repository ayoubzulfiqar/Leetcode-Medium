```python
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        ans = [0] * m

        # available_servers_heap stores (weight, index) for servers that are free.
        # It prioritizes by weight, then by index.
        available_servers_heap = []
        for i in range(n):
            heapq.heappush(available_servers_heap, (servers[i], i))

        # busy_servers_heap stores (free_time, index) for servers that are currently busy.
        # It prioritizes by free_time, then by index (though index tie-breaking isn't strictly
        # necessary here as we only care about free_time to move them to available).
        busy_servers_heap = []

        current_time = 0  # Represents the current simulation time
        task_idx = 0      # Represents the index of the task currently being considered for assignment

        while task_idx < m:
            # 1. Advance current_time if necessary to the arrival time of the current task.
            #    This ensures we don't try to assign task_idx before it arrives.
            current_time = max(current_time, task_idx)

            # 2. Move servers that have become free by current_time from busy_servers_heap
            #    to available_servers_heap.
            while busy_servers_heap and busy_servers_heap[0][0] <= current_time:
                free_time, server_id = heapq.heappop(busy_servers_heap)
                heapq.heappush(available_servers_heap, (servers[server_id], server_id))
            
            # 3. If no servers are available, it means we must wait for one to become free.
            #    Advance current_time to the time the next server becomes free.
            #    Then, move any servers that become free at this new time.
            if not available_servers_heap:
                # current_time must jump to the free_time of the earliest freeing server.
                current_time = busy_servers_heap[0][0]
                
                # After jumping time, more servers might become free. Process them.
                while busy_servers_heap and busy_servers_heap[0][0] <= current_time:
                    free_time, server_id = heapq.heappop(busy_servers_heap)
                    heapq.heappush(available_servers_heap, (servers[server_id], server_id))
            
            # 4. Assign the current task (task_idx) to the best available server.
            #    By this point, available_servers_heap is guaranteed to have at least one server.
            weight, server_id = heapq.heappop(available_servers_heap)
            ans[task_idx] = server_id
            
            # 5. Calculate when this server will be free and add it to the busy_servers_heap.
            server_free_time = current_time + tasks[task_idx]
            heapq.heappush(busy_servers_heap, (server_free_time, server_id))
            
            # 6. Move to the next task.
            task_idx += 1
            
        return ans

```