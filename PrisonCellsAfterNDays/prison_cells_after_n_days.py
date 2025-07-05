class Solution:
    def prisonAfterNDays(self, cells: list[int], n: int) -> list[int]:
        seen = {}
        history = []

        current_cells = list(cells)

        for day in range(n):
            state_tuple = tuple(current_cells)

            if state_tuple in seen:
                cycle_start_day = seen[state_tuple]
                cycle_length = day - cycle_start_day
                
                offset_in_cycle = (n - day) % cycle_length
                
                return history[cycle_start_day + offset_in_cycle]
            
            seen[state_tuple] = day
            history.append(current_cells)

            next_day_cells = [0] * 8

            for i in range(1, 7):
                if current_cells[i-1] == current_cells[i+1]:
                    next_day_cells[i] = 1
                else:
                    next_day_cells[i] = 0
            
            current_cells = next_day_cells
        
        return current_cells