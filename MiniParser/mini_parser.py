class NestedInteger:
    def __init__(self, value=None):
        """
        Initialize a NestedInteger.
        If value is provided, it holds a single integer.
        Otherwise, it holds an empty list.
        """
        if value is not None:
            self.integer = value
            self.list = None
        else:
            self.integer = None
            self.list = []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.integer is not None

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return self.integer

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer.
        :return: void
        """
        self.integer = value
        self.list = None

    def add(self, elem):
        """
        Add a nested integer elem to a nested list this NestedInteger holds.
        :return: void
        """
        if self.list is None:
            # This case should ideally not be reached if NestedInteger is used correctly
            # (i.e., add is only called on NestedInteger objects initialized as lists)
            self.list = [] # Convert to list if it was somehow an integer
        self.list.append(elem)

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype list[NestedInteger]
        """
        return self.list


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        self.s = s
        self.index = 0

        def parse_element():
            # Check if it's a list
            if self.s[self.index] == '[':
                self.index += 1  # Skip '['
                ni = NestedInteger()
                while self.s[self.index] != ']':
                    child_ni = parse_element()
                    ni.add(child_ni)
                    if self.s[self.index] == ',':
                        self.index += 1  # Skip ','
                self.index += 1  # Skip ']'
                return ni
            # Otherwise, it's an integer
            else:
                sign = 1
                if self.s[self.index] == '-':
                    sign = -1
                    self.index += 1
                num = 0
                while self.index < len(self.s) and self.s[self.index].isdigit():
                    num = num * 10 + int(self.s[self.index])
                    self.index += 1
                return NestedInteger(num * sign)

        return parse_element()