class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [0] * 300
        self.counts = [0] * 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = (timestamp - 1) % 300

        if self.times[idx] == timestamp:
            # If the timestamp matches, it means there's another hit
            # at the same second, so just increment the count.
            self.counts[idx] += 1
        else:
            # If the timestamp does not match, it means this slot
            # is either empty or holds an old hit that has fallen
            # out of the 300-second window. Reset it for the new hit.
            self.times[idx] = timestamp
            self.counts[idx] = 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        total_hits = 0
        # Iterate through all 300 possible slots in our circular buffer
        for i in range(300):
            # Check if the timestamp stored at this slot is within the
            # past 300 seconds (i.e., in the window [timestamp - 299, timestamp]).
            # This is equivalent to times[i] > timestamp - 300.
            if self.times[i] > timestamp - 300:
                total_hits += self.counts[i]
        return total_hits