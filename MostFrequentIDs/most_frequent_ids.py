import collections

class Solution:
    def mostFrequentIDs(self, nums: list[int], freq: list[int]) -> list[int]:
        id_counts = collections.defaultdict(int)
        freq_counts = collections.defaultdict(int)
        max_freq = 0
        ans = []

        for i in range(len(nums)):
            num = nums[i]
            delta = freq[i]

            old_count = id_counts[num]
            new_count = old_count + delta

            if old_count > 0:
                freq_counts[old_count] -= 1
                if freq_counts[old_count] == 0:
                    # If the old_count was the max_freq and no other ID has this frequency,
                    # we need to find the new maximum frequency.
                    if old_count == max_freq:
                        # Decrement max_freq until we find a frequency with at least one ID
                        # or until max_freq becomes 0 (collection empty).
                        while max_freq > 0 and freq_counts[max_freq] == 0:
                            max_freq -= 1

            id_counts[num] = new_count

            if new_count > 0:
                freq_counts[new_count] += 1
                # If the new_count is greater than the current max_freq, update max_freq.
                if new_count > max_freq:
                    max_freq = new_count

            ans.append(max_freq)

        return ans