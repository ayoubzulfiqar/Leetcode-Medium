class Solution:
    def minimumLevels(self, possible: list[int]) -> int:
        n = len(possible)

        total_score = 0
        for val in possible:
            total_score += (1 if val == 1 else -1)

        alice_current_score = 0
        for k_idx in range(n - 1):
            level_points = (1 if possible[k_idx] == 1 else -1)
            alice_current_score += level_points

            bob_current_score = total_score - alice_current_score

            if alice_current_score > bob_current_score:
                return k_idx + 1

        return -1