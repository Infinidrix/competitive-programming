
# https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flight_seats = [0 for i in range(n + 1)]
        for booking in bookings:
            flight_seats[booking[0] - 1] += booking[2]
            flight_seats[booking[1]] -= booking[2]
        last_seats = 0
        for seat in range(len(flight_seats)):
            flight_seats[seat] = last_seats + flight_seats[seat]
            last_seats = flight_seats[seat]
        flight_seats.pop()
        return flight_seats
