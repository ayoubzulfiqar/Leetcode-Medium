class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        player_time_to_target = abs(target[0]) + abs(target[1])

        for ghost_pos in ghosts:
            ghost_time_to_target = abs(ghost_pos[0] - target[0]) + abs(ghost_pos[1] - target[1])
            if ghost_time_to_target <= player_time_to_target:
                return False
        
        return True