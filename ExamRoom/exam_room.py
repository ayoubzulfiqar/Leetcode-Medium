import bisect

class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0

        max_dist = -1
        best_seat = -1

        # Candidate 1: Seat 0
        # Distance from seat 0 to the first occupied seat (self.seats[0])
        # The actual distance is self.seats[0] - 0.
        # If self.seats[0] is 0, this distance is 0.
        dist_from_0 = self.seats[0]
        max_dist = dist_from_0
        best_seat = 0

        # Candidate 2: Midpoints between adjacent occupied seats
        for i in range(len(self.seats) - 1):
            s1 = self.seats[i]
            s2 = self.seats[i+1]
            current_dist = (s2 - s1) // 2
            current_candidate_seat = s1 + current_dist

            if current_dist > max_dist:
                max_dist = current_dist
                best_seat = current_candidate_seat
            elif current_dist == max_dist:
                best_seat = min(best_seat, current_candidate_seat)

        # Candidate 3: Seat n-1
        # Distance from the last occupied seat (self.seats[-1]) to n-1
        # The actual distance is (self.n - 1) - self.seats[-1].
        dist_to_n_minus_1 = (self.n - 1) - self.seats[-1]
        candidate_seat_n_minus_1 = self.n - 1

        if dist_to_n_minus_1 > max_dist:
            max_dist = dist_to_n_minus_1
            best_seat = candidate_seat_n_minus_1
        elif dist_to_n_minus_1 == max_dist:
            best_seat = min(best_seat, candidate_seat_n_minus_1)
        
        bisect.insort_left(self.seats, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        self.seats.remove(p)