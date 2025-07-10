def get_passengers_per_bus(buses, passengers):
    buses.sort(key=lambda x: x[0])
    passengers.sort()

    num_buses = len(buses)
    bus_passengers_count = [0] * num_buses
    
    p_idx = 0 
    num_passengers = len(passengers)

    for b_idx in range(num_buses):
        bus_arrival_time, bus_capacity = buses[b_idx]
        
        current_bus_capacity_left = bus_capacity
        
        while p_idx < num_passengers and \
              passengers[p_idx] <= bus_arrival_time and \
              current_bus_capacity_left > 0:
            
            bus_passengers_count[b_idx] += 1
            current_bus_capacity_left -= 1
            p_idx += 1
            
    return bus_passengers_count