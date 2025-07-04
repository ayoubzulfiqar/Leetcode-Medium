class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0

        total_teams = 0

        for j in range(1, n - 1):
            current_rating = rating[j]

            less_left = 0
            greater_left = 0
            for i in range(j):
                if rating[i] < current_rating:
                    less_left += 1
                else:
                    greater_left += 1

            less_right = 0
            greater_right = 0
            for k in range(j + 1, n):
                if rating[k] < current_rating:
                    less_right += 1
                else:
                    greater_right += 1

            total_teams += less_left * greater_right
            total_teams += greater_left * less_right

        return total_teams