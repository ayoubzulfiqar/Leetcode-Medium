class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        minutes = []
        for time_str in timePoints:
            hh, mm = map(int, time_str.split(':'))
            minutes.append(hh * 60 + mm)

        minutes.sort()

        min_diff = float('inf')

        for i in range(len(minutes) - 1):
            diff = minutes[i+1] - minutes[i]
            min_diff = min(min_diff, diff)

        wrap_around_diff = (1440 - minutes[-1]) + minutes[0]
        min_diff = min(min_diff, wrap_around_diff)

        return min_diff