import collections

class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}
        self.travel_times = collections.defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_ins[id]
        del self.check_ins[id]

        travel_time = t - check_in_time
        
        route_key = (start_station, stationName)
        
        self.travel_times[route_key][0] += travel_time
        self.travel_times[route_key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route_key = (startStation, endStation)
        total_time, count = self.travel_times[route_key]
        return total_time / count