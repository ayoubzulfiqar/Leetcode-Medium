class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.next_val = None
        self.has_next_val = False
        self._fetch_next()

    def _fetch_next(self):
        """
        Helper function to pre-fetch the next element from the underlying iterator.
        """
        if self.iterator.hasNext():
            self.next_val = self.iterator.next()
            self.has_next_val = True
        else:
            self.next_val = None
            self.has_next_val = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_val

    def next(self):
        """
        Returns the next element in the iteration and advances the iterator.
        :rtype: int
        """
        temp = self.next_val
        self._fetch_next()
        return temp

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.has_next_val