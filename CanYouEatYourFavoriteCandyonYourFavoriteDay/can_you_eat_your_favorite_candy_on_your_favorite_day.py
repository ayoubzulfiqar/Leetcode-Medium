class Solution:
    def canEat(self, candiesCount: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(candiesCount)
        
        # Calculate prefix sums of candiesCount
        # prefix_sum[i] stores the total number of candies from type 0 to i-1.
        # prefix_sum[0] = 0
        # prefix_sum[k] = sum(candiesCount[0]...candiesCount[k-1]) for k > 0.
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + candiesCount[i]
            
        results = []
        for query in queries:
            favoriteType, favoriteDay, dailyCap = query
            
            # Calculate the earliest day we can possibly start eating favoriteType candy.
            # To eat favoriteType candy, all candies of types 0 to favoriteType - 1 must be eaten.
            # The total number of such candies is prefix_sum[favoriteType].
            # Since we can eat at most `dailyCap` candies per day, the minimum number of days
            # required to consume `prefix_sum[favoriteType]` candies is `prefix_sum[favoriteType] // dailyCap`.
            # This value represents the day index on which we would start eating `favoriteType`
            # if we ate `dailyCap` candies every day until `favoriteType` candies become available.
            # Example: if 10 candies before, dailyCap 3. 10 // 3 = 3.
            # Day 0: 3 candies, Day 1: 3 candies, Day 2: 3 candies, Day 3: 1 candy (from previous types) + can start favoriteType.
            # So, day 3 is the earliest day.
            earliest_day_to_eat_fav_type = prefix_sum[favoriteType] // dailyCap
            
            # Calculate the latest day we can still be eating favoriteType candy.
            # To still be eating favoriteType candy on favoriteDay, we must not have finished
            # all candies up to and including favoriteType.
            # The total number of candies up to and including favoriteType is prefix_sum[favoriteType + 1].
            # Since we must eat at least 1 candy per day, the maximum number of days
            # we can spend eating these candies is `prefix_sum[favoriteType + 1]` days.
            # If we eat 1 candy per day, we would finish on day `(total_candies - 1)`.
            # Example: if 10 total candies (up to fav type). Eat 1 per day.
            # Day 0: 1st candy, Day 1: 2nd candy, ..., Day 9: 10th candy. We finish on day 9.
            # So, we can eat on day 9. We cannot eat on day 10.
            latest_day_to_eat_fav_type = prefix_sum[favoriteType + 1] - 1
            
            # Check if favoriteDay falls within the possible range
            can_eat = (favoriteDay >= earliest_day_to_eat_fav_type) and \
                      (favoriteDay <= latest_day_to_eat_fav_type)
            
            results.append(can_eat)
            
        return results