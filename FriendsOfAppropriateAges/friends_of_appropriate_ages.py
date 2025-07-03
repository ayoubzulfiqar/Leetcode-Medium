class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        age_counts = [0] * 121 
        for age in ages:
            age_counts[age] += 1

        total_requests = 0

        for age_x in range(1, 121):
            if age_counts[age_x] == 0:
                continue

            for age_y in range(1, 121):
                if age_counts[age_y] == 0:
                    continue

                # Condition 1: age[y] <= 0.5 * age[x] + 7
                if age_y <= 0.5 * age_x + 7:
                    continue

                # Condition 2: age[y] > age[x]
                if age_y > age_x:
                    continue

                # Condition 3: age[y] > 100 && age[x] < 100
                if age_y > 100 and age_x < 100:
                    continue

                if age_x == age_y:
                    total_requests += age_counts[age_x] * (age_counts[age_x] - 1)
                else:
                    total_requests += age_counts[age_x] * age_counts[age_y]
        
        return total_requests