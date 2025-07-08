import heapq

class Solution:
    def findShortestPath(self, gridMaster: 'GridMaster') -> int:
        self.grid_map = {}
        self.target_coords = [None]
        self.visited_dfs = set()

        self.dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.rev_dirs = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

        self.grid_map[(0, 0)] = 0 
        self.explore(0, 0, gridMaster)

        if self.target_coords[0] is None:
            return -1

        start_node = (0, 0)
        target_node = self.target_coords[0]

        dist_to_node = {start_node: 0}
        
        pq = [(0, start_node[0], start_node[1])]

        while pq:
            current_total_cost, r, c = heapq.heappop(pq)

            if current_total_cost > dist_to_node.get((r, c), float('inf')):
                continue

            if (r, c) == target_node:
                return current_total_cost

            for d_char, (dr, dc) in self.dirs.items():
                nr, nc = r + dr, c + dc
                
                if (nr, nc) in self.grid_map:
                    cost_of_neighbor = self.grid_map[(nr, nc)]
                    new_total_cost = current_total_cost + cost_of_neighbor

                    if new_total_cost < dist_to_node.get((nr, nc), float('inf')):
                        dist_to_node[(nr, nc)] = new_total_cost
                        heapq.heappush(pq, (new_total_cost, nr, nc))
        
        return -1

    def explore(self, r: int, c: int, gridMaster: 'GridMaster'):
        self.visited_dfs.add((r, c))

        if gridMaster.isTarget():
            self.target_coords[0] = (r, c)

        for d_char, (dr, dc) in self.dirs.items():
            nr, nc = r + dr, c + dc
            
            if (nr, nc) not in self.visited_dfs and gridMaster.canMove(d_char):
                cost = gridMaster.move(d_char) 
                self.grid_map[(nr, nc)] = cost
                
                self.explore(nr, nc, gridMaster)
                
                gridMaster.move(self.rev_dirs[d_char])

```