class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # Define the jumps required to connect non-adjacent points.
        # jumps[i][j] stores the point that must be visited if moving from i to j.
        # Points are 0-indexed (0 to 8) representing the 3x3 grid:
        # 0 1 2
        # 3 4 5
        # 6 7 8
        jumps = [[0] * 9 for _ in range(9)]

        # Populate the jumps array for symmetric pairs
        jumps[0][2] = jumps[2][0] = 1
        jumps[0][6] = jumps[6][0] = 3
        jumps[0][8] = jumps[8][0] = 4
        jumps[1][7] = jumps[7][1] = 4
        jumps[2][8] = jumps[8][2] = 5
        jumps[2][6] = jumps[6][2] = 4
        jumps[3][5] = jumps[5][3] = 4
        jumps[6][8] = jumps[8][6] = 7

        # visited array to keep track of visited points in the current path
        visited = [False] * 9
        
        # Accumulator for the total number of valid patterns
        total_patterns = 0

        # Depth First Search (DFS) function to explore patterns
        # current_num: The last number added to the pattern (0-indexed)
        # length: The current length of the pattern
        def dfs(current_num, length):
            nonlocal total_patterns

            # If the current pattern length is within the valid range [m, n], count it
            if m <= length <= n:
                total_patterns += 1
            
            # If the current pattern length has reached n, no need to explore longer paths
            if length == n:
                return

            # Mark the current number as visited for this path
            visited[current_num] = True

            # Iterate through all possible next numbers (0 to 8)
            for next_num in range(9):
                # If next_num has not been visited yet
                if not visited[next_num]:
                    # Check the jump rule:
                    # jump_over_point is the point that must be visited if moving from current_num to next_num
                    jump_over_point = jumps[current_num][next_num]
                    
                    # If there's a jump_over_point (i.e., not 0) AND it hasn't been visited,
                    # then this move is invalid. Skip this next_num.
                    if jump_over_point != 0 and not visited[jump_over_point]:
                        continue
                    
                    # If the move is valid, recurse to extend the pattern
                    dfs(next_num, length + 1)
            
            # Backtrack: Unmark the current number as visited for other paths
            visited[current_num] = False

        # Start DFS from each possible point, leveraging symmetry to optimize calculations:
        # 1. Corner points (0, 2, 6, 8) are symmetric. Start from 0 and multiply results by 4.
        # 2. Edge points (1, 3, 5, 7) are symmetric. Start from 1 and multiply results by 4.
        # 3. Center point (4) is unique. Start from 4 and multiply results by 1.

        # Calculate patterns starting from a corner point (e.g., 0)
        dfs(0, 1) # length starts at 1
        total_patterns_from_corner = total_patterns
        total_patterns = 0 # Reset accumulator for the next symmetric group

        # Calculate patterns starting from an edge point (e.g., 1)
        dfs(1, 1)
        total_patterns_from_edge = total_patterns
        total_patterns = 0

        # Calculate patterns starting from the center point (4)
        dfs(4, 1)
        total_patterns_from_center = total_patterns
        total_patterns = 0

        # Sum up results considering symmetry
        return total_patterns_from_corner * 4 + \
               total_patterns_from_edge * 4 + \
               total_patterns_from_center * 1