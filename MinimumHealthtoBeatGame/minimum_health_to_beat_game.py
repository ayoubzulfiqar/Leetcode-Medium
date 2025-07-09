class Solution:
    def min_health_to_beat_game(self, health_changes: list[int]) -> int:
        current_health_relative_to_start = 0
        min_health_relative_to_start = 0

        for change in health_changes:
            current_health_relative_to_start += change
            min_health_relative_to_start = min(min_health_relative_to_start, current_health_relative_to_start)

        required_initial_health = 1 - min_health_relative_to_start
        return required_initial_health