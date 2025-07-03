class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        answer = [0] * n

        for first, last, seats in bookings:
            # Adjust to 0-indexed
            first_idx = first - 1
            last_idx = last - 1

            # Add seats at the start of the range
            answer[first_idx] += seats

            # Subtract seats right after the end of the range
            # This ensures the seats are only counted within [first, last]
            if last_idx + 1 < n:
                answer[last_idx + 1] -= seats
        
        # Perform prefix sum to get the total seats for each flight
        for i in range(1, n):
            answer[i] += answer[i-1]
            
        return answer

```python
# Example Usage (for testing purposes, not part of the solution file)
# sol = Solution()
# print(sol.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5)) # Expected: [10, 55, 45, 25, 25]
# print(sol.corpFlightBookings([[1,2,10],[2,2,15]], 2)) # Expected: [10, 25]
```