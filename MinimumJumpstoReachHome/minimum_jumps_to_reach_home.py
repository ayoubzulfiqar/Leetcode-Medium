import collections

class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        forbidden_set = set(forbidden)

        # Determine the maximum position to explore.
        # Based on problem constraints (max x, a, b, forbidden[i] are 2000),
        # a safe upper bound for positions to explore is around 6000.
        # This covers scenarios like 0 -> a -> a-b -> a-b+a, where a is large.
        # Or reaching x by overshooting and coming back.
        # A common heuristic for such problems is max(x, max(forbidden)) + a + b.
        # Given max values are 2000, this is 2000 + 2000 + 2000 = 6000.
        MAX_POS = 6000 

        q = collections.deque([(0, False, 0)]) # (current_pos, last_jump_was_backward, jumps)
        # last_jump_was_backward: True if the last jump was backward, False otherwise.
        # This is crucial to enforce the "cannot jump backward twice in a row" rule.
        
        visited = set() # Stores (position, last_jump_was_backward) to avoid cycles and redundant work.
        visited.add((0, False))

        while q:
            current_pos, last_jump_backward, jumps = q.popleft()

            if current_pos == x:
                return jumps

            # Option 1: Jump forward (current_pos + a)
            next_pos_forward = current_pos + a
            if next_pos_forward <= MAX_POS and \
               next_pos_forward not in forbidden_set and \
               (next_pos_forward, False) not in visited:
                visited.add((next_pos_forward, False))
                q.append((next_pos_forward, False, jumps + 1))

            # Option 2: Jump backward (current_pos - b)
            # Cannot jump backward twice in a row, and cannot jump to negative positions.
            next_pos_backward = current_pos - b
            if not last_jump_backward and \
               next_pos_backward >= 0 and \
               next_pos_backward not in forbidden_set and \
               (next_pos_backward, True) not in visited:
                visited.add((next_pos_backward, True))
                q.append((next_pos_backward, True, jumps + 1))
        
        return -1 # If queue becomes empty and x is not reached