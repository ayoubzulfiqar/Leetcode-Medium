import collections

class Solution:
    def solve(self, maze: list[str]) -> bool:
        rows = len(maze)
        if rows == 0:
            return False
        cols = len(maze[0])
        if cols == 0:
            return False

        start_pos = None
        for r in range(rows):
            for c in range(cols):
                if maze[r][c] == 'S':
                    start_pos = (r, c)
                    break
            if start_pos:
                break

        if not start_pos:
            return False

        room_paths = collections.defaultdict(list)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, current_path_list, visited_set):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if maze[r][c] == '#':
                return
            if (r, c) in visited_set:
                return

            current_path_list.append((r, c))
            visited_set.add((r, c))

            if maze[r][c] == 'R':
                room_paths[(r, c)].append(list(current_path_list))
                current_path_list.pop()
                visited_set.remove((r, c))
                return

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, current_path_list, visited_set)
            
            current_path_list.pop()
            visited_set.remove((r, c))

        dfs(start_pos[0], start_pos[1], [], set())

        for room_coord in room_paths:
            if len(room_paths[room_coord]) >= 2:
                return True
        
        return False