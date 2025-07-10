class FrequencyTracker:

    def __init__(self):
        self.counts = {}  # Stores number -> its current frequency
        self.freq_counts = {}  # Stores frequency -> count of numbers that have this frequency

    def add(self, number: int) -> None:
        old_freq = self.counts.get(number, 0)

        # If the number previously existed, decrement the count for its old frequency
        if old_freq > 0:
            self.freq_counts[old_freq] -= 1
            if self.freq_counts[old_freq] == 0:
                del self.freq_counts[old_freq]

        # Increment the number's count
        self.counts[number] = old_freq + 1
        new_freq = self.counts[number]

        # Increment the count for the new frequency
        self.freq_counts[new_freq] = self.freq_counts.get(new_freq, 0) + 1

    def deleteOne(self, number: int) -> None:
        # If the number is not in the data structure or its count is already 0, do nothing
        if number not in self.counts or self.counts[number] == 0:
            return

        old_freq = self.counts[number]

        # Decrement the count for the old frequency
        self.freq_counts[old_freq] -= 1
        if self.freq_counts[old_freq] == 0:
            del self.freq_counts[old_freq]

        # Decrement the number's count
        self.counts[number] -= 1
        new_freq = self.counts[number]

        # If the number still exists (new_freq > 0), increment the count for its new frequency
        if new_freq > 0:
            self.freq_counts[new_freq] = self.freq_counts.get(new_freq, 0) + 1
        else:
            # If new_freq is 0, the number is completely removed, so remove it from counts
            del self.counts[number]

    def hasFrequency(self, frequency: int) -> bool:
        # Return true if there is at least one number with the given frequency
        return self.freq_counts.get(frequency, 0) > 0