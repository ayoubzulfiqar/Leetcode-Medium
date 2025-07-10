import collections

class Flight:
    """
    Represents a single flight with its capacity, booked passengers, and a waitlist.
    """
    def __init__(self, flight_number: str, capacity: int):
        if not isinstance(flight_number, str) or not flight_number:
            raise ValueError("Flight number must be a non-empty string.")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")

        self.flight_number = flight_number
        self.capacity = capacity
        self.booked_passengers = set()  # Stores IDs of booked passengers
        self.waitlist = collections.deque()  # Stores IDs of waitlisted passengers in order

    def book_passenger(self, passenger_id: str) -> str:
        """
        Attempts to book a passenger. If the flight is full, the passenger is added to the waitlist.
        Returns:
            "BOOKED": Passenger successfully booked.
            "WAITLISTED": Passenger added to waitlist.
            "ALREADY_PROCESSED": Passenger is already booked or on the waitlist.
        """
        if not isinstance(passenger_id, str) or not passenger_id:
            raise ValueError("Passenger ID must be a non-empty string.")

        if passenger_id in self.booked_passengers:
            return "ALREADY_PROCESSED"
        
        # Check if passenger is already on waitlist.
        # This operation is O(N) for deque, where N is waitlist size.
        if passenger_id in self.waitlist:
            return "ALREADY_PROCESSED"

        if len(self.booked_passengers) < self.capacity:
            self.booked_passengers.add(passenger_id)
            return "BOOKED"
        else:
            self.waitlist.append(passenger_id)
            return "WAITLISTED"

    def cancel_passenger(self, passenger_id: str) -> str:
        """
        Attempts to cancel a passenger's booking or waitlist position.
        If a booked passenger cancels and there's a waitlist, the first waitlisted passenger is upgraded.
        Returns:
            "CANCELLED_AND_UPGRADED_[ID]": Booked passenger cancelled, and a waitlisted passenger was upgraded.
            "CANCELLED": Booked passenger cancelled, no waitlist to upgrade.
            "WAITLIST_CANCELLED": Passenger successfully removed from waitlist.
            "PASSENGER_NOT_FOUND": Passenger ID not found in booked or waitlist.
        """
        if not isinstance(passenger_id, str) or not passenger_id:
            raise ValueError("Passenger ID must be a non-empty string.")

        if passenger_id in self.booked_passengers:
            self.booked_passengers.remove(passenger_id)
            if self.waitlist:
                upgraded_passenger = self.waitlist.popleft()
                self.booked_passengers.add(upgraded_passenger)
                return f"CANCELLED_AND_UPGRADED_{upgraded_passenger}"
            else:
                return "CANCELLED"
        elif passenger_id in self.waitlist:
            # To remove an arbitrary element from a deque, convert to list, remove, convert back.
            # This operation is O(N) for deque.
            temp_list = list(self.waitlist)
            try:
                temp_list.remove(passenger_id)
                self.waitlist = collections.deque(temp_list)
                return "WAITLIST_CANCELLED"
            except ValueError:
                # This case should ideally not be reached if passenger_id was in self.waitlist
                return "PASSENGER_NOT_FOUND" 
        else:
            return "PASSENGER_NOT_FOUND"

    def get_occupancy(self) -> int:
        """Returns the current number of booked passengers."""
        return len(self.booked_passengers)

    def get_available_seats(self) -> int:
        """Returns the number of available seats."""
        return self.capacity - len(self.booked_passengers)

    def get_waitlist_size(self) -> int:
        """Returns the current number of passengers on the waitlist."""
        return len(self.waitlist)

    def get_waitlist(self) -> list:
        """Returns a list of passengers currently on the waitlist (order matters)."""
        return list(self.waitlist)

    def get_booked_passengers(self) -> list:
        """Returns a list of passengers currently booked."""
        return list(self.booked_passengers)

    def get_flight_status(self) -> dict:
        """Returns a dictionary with comprehensive flight status."""
        return {
            "flight_number": self.flight_number,
            "capacity": self.capacity,
            "current_occupancy": self.get_occupancy(),
            "available_seats": self.get_available_seats(),
            "waitlist_size": self.get_waitlist_size(),
            "booked_passengers": sorted(list(self.booked_passengers)), # Sorted for consistent output
            "waitlist": list(self.waitlist)
        }

def main():
    """
    Demonstrates the functionality of the Flight class.
    """
    print("--- Flight Occupancy and Waitlist Analysis Demonstration ---")

    # 1. Create a flight
    flight_a = Flight("FL101", 3) # Capacity of 3 seats
    print(f"\nCreated Flight {flight_a.flight_number} with capacity {flight_a.capacity}.")
    print("Initial Status:", flight_a.get_flight_status())

    # 2. Book passengers up to capacity
    print("\n--- Booking Passengers ---")
    print(f"Booking P1: {flight_a.book_passenger('P1')}")
    print(f"Booking P2: {flight_a.book_passenger('P2')}")
    print(f"Booking P3: {flight_a.book_passenger('P3')}")
    print("Status after initial bookings:", flight_a.get_flight_status())
    print(f"Available seats: {flight_a.get_available_seats()}")

    # 3. Add passengers to waitlist
    print("\n--- Adding Passengers to Waitlist ---")
    print(f"Booking P4: {flight_a.book_passenger('P4')}") # Should be waitlisted
    print(f"Booking P5: {flight_a.book_passenger('P5')}") # Should be waitlisted
    print("Status after waitlist additions:", flight_a.get_flight_status())
    print(f"Waitlist size: {flight_a.get_waitlist_size()}")
    print(f"Waitlist: {flight_a.get_waitlist()}")

    # 4. Attempt to book an already processed passenger
    print("\n--- Attempting to re-book/re-waitlist ---")
    print(f"Booking P1 again: {flight_a.book_passenger('P1')}")
    print(f"Booking P4 again: {flight_a.book_passenger('P4')}")

    # 5. Cancel a booked passenger (with waitlist)
    print("\n--- Cancelling Booked Passenger (with waitlist) ---")
    print(f"Cancelling P1: {flight_a.cancel_passenger('P1')}") # P4 should be upgraded
    print("Status after P1 cancellation:", flight_a.get_flight_status())
    print(f"Waitlist: {flight_a.get_waitlist()}")

    # 6. Cancel another booked passenger (with waitlist)
    print(f"Cancelling P2: {flight_a.cancel_passenger('P2')}") # P5 should be upgraded
    print("Status after P2 cancellation:", flight_a.get_flight_status())
    print(f"Waitlist: {flight_a.get_waitlist()}")

    # 7. Cancel a booked passenger (no waitlist)
    print("\n--- Cancelling Booked Passenger (no waitlist) ---")
    print(f"Cancelling P3: {flight_a.cancel_passenger('P3')}")
    print("Status after P3 cancellation:", flight_a.get_flight_status())

    # 8. Cancel a waitlisted passenger
    print("\n--- Cancelling Waitlisted Passenger ---")
    # Re-fill flight and add to waitlist for this test
    flight_a.book_passenger('P6') 
    flight_a.book_passenger('P7') 
    flight_a.book_passenger('P8') 
    flight_a.book_passenger('P9') # Waitlisted
    flight_a.book_passenger('P10') # Waitlisted
    print("Status before waitlist cancellation:", flight_a.get_flight_status())
    print(f"Cancelling P9 (waitlisted): {flight_a.cancel_passenger('P9')}")
    print("Status after P9 cancellation:", flight_a.get_flight_status())
    print(f"Waitlist: {flight_a.get_waitlist()}")

    # 9. Attempt to cancel a non-existent passenger
    print("\n--- Attempting to cancel non-existent passenger ---")
    print(f"Cancelling P_NON_EXISTENT: {flight_a.cancel_passenger('P_NON_EXISTENT')}")
    print("Status after non-existent cancellation attempt:", flight_a.get_flight_status())

    # 10. Test invalid input for Flight creation and methods
    print("\n--- Testing invalid inputs ---")
    try:
        Flight("FL200", 0)
    except ValueError as e:
        print(f"Error creating flight with 0 capacity: {e}")
    try:
        Flight("FL200", -5)
    except ValueError as e:
        print(f"Error creating flight with negative capacity: {e}")
    try:
        Flight("FL200", "invalid_capacity")
    except ValueError as e:
        print(f"Error creating flight with non-integer capacity: {e}")
    
    try:
        flight_a.book_passenger("")
    except ValueError as e:
        print(f"Error booking with empty passenger ID: {e}")
    try:
        flight_a.cancel_passenger(None)
    except ValueError as e:
        print(f"Error cancelling with None passenger ID: {e}")

if __name__ == "__main__":
    main()