class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        # The maximum location is 1000. We need an array to track changes
        # at each location from 0 to 1000.
        # An array of size 1001 will cover indices 0 through 1000.
        location_changes = [0] * 1001

        # Populate the location_changes array based on trips
        for num_passengers, from_location, to_location in trips:
            # At from_location, passengers board
            location_changes[from_location] += num_passengers
            # At to_location, passengers alight
            # Note: Passengers alight *at* to_location, so the capacity
            # check should happen *before* they alight.
            # Thus, the change applies *after* the current location's check.
            # If a trip is [num, 1, 5], passengers are on board for locations 1, 2, 3, 4.
            # They get off at 5. So, the count decreases starting from location 5.
            location_changes[to_location] -= num_passengers

        current_passengers = 0
        # Iterate through all possible locations to simulate the journey
        for i in range(1001):
            current_passengers += location_changes[i]
            # Check if the current number of passengers exceeds capacity
            if current_passengers > capacity:
                return False

        # If we complete the journey without exceeding capacity at any point
        return True