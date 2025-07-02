```python
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        ans = [0] * n
        stack = []  # Stores function IDs
        
        # Parse the first log to initialize prev_timestamp
        # The first event's timestamp is the starting point for time tracking.
        first_log_parts = logs[0].split(':')
        prev_timestamp = int(first_log_parts[2])

        for log in logs:
            func_id_str, type_str, timestamp_str = log.split(':')
            func_id = int(func_id_str)
            timestamp = int(timestamp_str)

            if type_str == "start":
                # If there's a function on the stack, it means that function
                # was executing until the current timestamp.
                if stack: 
                    ans[stack[-1]] += timestamp - prev_timestamp
                
                # Push the new function onto the stack
                stack.append(func_id)
                
                # Update prev_timestamp to the current timestamp
                # as this is the new reference point for duration calculations.
                prev_timestamp = timestamp
            else:  # type_str == "end"
                # The function that just ended was executing from prev_timestamp
                # until the current timestamp (inclusive).
                # Pop the function from the stack (it must be the one at the top).
                ans[stack.pop()] += timestamp - prev_timestamp + 1
                
                # After this function ends, the next event (either a new start
                # or the resumption of a parent function) will effectively start
                # from the timestamp *after* this function ended.
                prev_timestamp = timestamp + 1
        
        return ans

```