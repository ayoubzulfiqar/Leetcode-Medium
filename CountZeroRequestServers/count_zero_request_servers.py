class Solution:
    def countZeroRequestServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        results = [0] * len(queries)

        logs.sort(key=lambda item: item[1])

        indexed_queries = []
        for i, q_time in enumerate(queries):
            indexed_queries.append((q_time, i))
        indexed_queries.sort(key=lambda item: item[0])

        left_ptr = 0
        right_ptr = 0

        server_counts = {}

        for query_time, original_index in indexed_queries:
            start_interval = query_time - x
            end_interval = query_time

            while right_ptr < len(logs) and logs[right_ptr][1] <= end_interval:
                server_id = logs[right_ptr][0]
                server_counts[server_id] = server_counts.get(server_id, 0) + 1
                right_ptr += 1

            while left_ptr < len(logs) and logs[left_ptr][1] < start_interval:
                server_id = logs[left_ptr][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    del server_counts[server_id]
                left_ptr += 1

            num_active_servers = len(server_counts)

            results[original_index] = n - num_active_servers

        return results