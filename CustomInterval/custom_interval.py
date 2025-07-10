class CustomInterval:
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start cannot be greater than end for a valid interval.")
        self.start = start
        self.end = end

    def __repr__(self):
        return f"CustomInterval({self.start}, {self.end})"

    def __str__(self):
        return f"[{self.start}, {self.end}]"

    def __eq__(self, other):
        if not isinstance(other, CustomInterval):
            return NotImplemented
        return self.start == other.start and self.end == other.end

    def __lt__(self, other):
        if not isinstance(other, CustomInterval):
            return NotImplemented
        if self.start != other.start:
            return self.start < other.start
        return self.end < other.end

    def __contains__(self, item):
        if isinstance(item, (int, float)):
            return self.start <= item <= self.end
        elif isinstance(item, CustomInterval):
            return self.start <= item.start and item.end <= self.end
        return False

    def overlaps(self, other_interval):
        if not isinstance(other_interval, CustomInterval):
            raise TypeError("Can only check overlap with another CustomInterval instance.")
        return self.start <= other_interval.end and other_interval.start <= self.end

    def merge(self, other_interval):
        if not isinstance(other_interval, CustomInterval):
            raise TypeError("Can only merge with another CustomInterval instance.")

        if self.overlaps(other_interval):
            new_start = min(self.start, other_interval.start)
            new_end = max(self.end, other_interval.end)
            return CustomInterval(new_start, new_end)
        else:
            return None

    def intersection(self, other_interval):
        if not isinstance(other_interval, CustomInterval):
            raise TypeError("Can only find intersection with another CustomInterval instance.")

        if not self.overlaps(other_interval):
            return None

        new_start = max(self.start, other_interval.start)
        new_end = min(self.end, other_interval.end)
        return CustomInterval(new_start, new_end)