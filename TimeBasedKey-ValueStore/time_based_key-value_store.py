import collections
import bisect

class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        key_data = self.store[key]
        
        # The dummy value '{' is chosen because it is lexicographically greater
        # than any lowercase English letter or digit, ensuring that when timestamps
        # are equal, the search tuple is considered greater, pushing the insertion
        # point to the right. This allows bisect_right to correctly find the
        # rightmost element with a timestamp less than or equal to the target.
        idx = bisect.bisect_right(key_data, (timestamp, '{'))

        if idx == 0:
            return ""
        else:
            return key_data[idx - 1][1]