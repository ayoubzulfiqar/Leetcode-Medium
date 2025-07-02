import collections
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        class WordFreq:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq

            # This method defines the "less than" relationship for elements in the min-heap.
            # An element `self` is considered "less than" `other` if `self` is less desirable
            # (i.e., should be popped first from a min-heap that keeps "top K" elements).
            def __lt__(self, other):
                # If frequencies are different, the one with lower frequency is "less desirable".
                if self.freq != other.freq:
                    return self.freq < other.freq
                # If frequencies are the same, the one with a lexicographically LARGER word
                # is "less desirable" because we want to keep the lexicographically smaller word among ties.
                return self.word > other.word

        counts = collections.Counter(words)

        pq = []  # Min-heap

        for word, freq in counts.items():
            heapq.heappush(pq, WordFreq(word, freq))
            if len(pq) > k:
                heapq.heappop(pq)  # Remove the least desirable element (lowest freq, or highest word if freq tied)

        # The heap now contains the k most frequent words, ordered by their "desirability".
        # When popping from the min-heap, elements come out in increasing order of "desirability"
        # (i.e., least desirable first).
        # To get them in the final desired order (most desirable first), we pop all and then reverse.
        result_objs = []
        while pq:
            result_objs.append(heapq.heappop(pq))

        # Reverse the list to get elements from most desirable to least desirable.
        result_objs.reverse()

        # Extract just the words from the WordFreq objects.
        final_result = [wf.word for wf in result_objs]

        return final_result