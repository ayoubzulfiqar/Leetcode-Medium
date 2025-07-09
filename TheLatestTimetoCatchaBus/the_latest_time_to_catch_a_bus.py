class Solution:
    def latestTimeCatchTheBus(self, buses: list[int], passengers: list[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        passenger_ptr = 0
        taken_times = set()
        
        last_bus_was_full = False 
        latest_passenger_on_last_bus_time = -1 
        
        for bus_time in buses:
            current_bus_passengers_boarded = 0
            current_bus_latest_passenger_time = -1 

            while (current_bus_passengers_boarded < capacity and 
                   passenger_ptr < len(passengers) and 
                   passengers[passenger_ptr] <= bus_time):
                
                taken_times.add(passengers[passenger_ptr])
                current_bus_latest_passenger_time = passengers[passenger_ptr]
                current_bus_passengers_boarded += 1
                passenger_ptr += 1
            
            if current_bus_passengers_boarded == capacity:
                last_bus_was_full = True
                latest_passenger_on_last_bus_time = current_bus_latest_passenger_time
            else:
                last_bus_was_full = False
                latest_passenger_on_last_bus_time = -1 
                
        my_arrival_time_candidate = -1

        if last_bus_was_full:
            my_arrival_time_candidate = latest_passenger_on_last_bus_time - 1
        else:
            my_arrival_time_candidate = buses[-1]
        
        while my_arrival_time_candidate in taken_times:
            my_arrival_time_candidate -= 1
            
        return my_arrival_time_candidate