class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Combine position and speed into pairs.
        # Each pair represents a car: (initial_position, speed).
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        # Sort the cars by their initial position in descending order.
        # This means we process cars starting from the one closest to the target
        # moving backwards to the one furthest from the target.
        cars.sort(key=lambda x: x[0], reverse=True)

        num_fleets = 0
        # This variable will store the arrival time at the target for the
        # current leading fleet. When processing cars from closest to furthest,
        # any car behind the current leading fleet might merge with it if it
        # can catch up.
        # Initialize with a value that any valid car's arrival time will be greater than.
        current_fleet_arrival_time = -1.0 

        for pos, spd in cars:
            # Calculate the time it takes for this car to reach the target.
            # Use float division to maintain precision.
            time_to_target = float(target - pos) / spd

            # If this car's calculated time to reach the target is strictly greater
            # than the arrival time of the current leading fleet, it means:
            # 1. This car will arrive *after* the current leading fleet.
            # 2. Since cars cannot pass, this car will never catch up to the
            #    current leading fleet.
            # Therefore, this car forms a new, separate fleet.
            if time_to_target > current_fleet_arrival_time:
                num_fleets += 1
                # This new fleet's arrival time now becomes the reference for
                # subsequent cars (cars further behind it).
                current_fleet_arrival_time = time_to_target
            # Else (time_to_target <= current_fleet_arrival_time):
            # This car's calculated time to reach the target is less than or equal to
            # the arrival time of the current leading fleet.
            # This implies that this car (being behind) will catch up to the
            # current leading fleet. Once it catches up, it merges with that fleet.
            # The combined fleet's arrival time is still determined by the original
            # leading car/fleet (current_fleet_arrival_time), as it was the bottleneck.
            # No new fleet is formed, and current_fleet_arrival_time remains unchanged.
            
        return num_fleets