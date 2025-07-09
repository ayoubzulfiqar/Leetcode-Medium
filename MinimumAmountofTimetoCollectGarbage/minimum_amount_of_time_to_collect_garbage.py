class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        n = len(garbage)

        # Calculate prefix sums for travel times.
        # travel_prefix_sum[i] will store the cumulative time to travel from house 0 to house i.
        travel_prefix_sum = [0] * n
        current_sum = 0
        for i in range(n - 1):
            current_sum += travel[i]
            travel_prefix_sum[i + 1] = current_sum

        total_minutes = 0

        # Iterate through each type of garbage ('M', 'P', 'G')
        garbage_types = ['M', 'P', 'G']

        for g_type in garbage_types:
            pickup_time_for_type = 0
            last_house_idx_for_type = -1 # Stores the index of the last house where this garbage type was found

            # Iterate through all houses to calculate pickup time and find the last house
            for i in range(n):
                house_garbage = garbage[i]
                count = house_garbage.count(g_type)
                if count > 0:
                    pickup_time_for_type += count
                    last_house_idx_for_type = i
            
            # Add the total time spent picking up this type of garbage
            total_minutes += pickup_time_for_type

            # Add the travel time for this truck
            # The truck only needs to travel up to the last house where it picked up garbage.
            if last_house_idx_for_type != -1:
                total_minutes += travel_prefix_sum[last_house_idx_for_type]
        
        return total_minutes