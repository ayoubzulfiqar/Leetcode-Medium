class NestedInteger:
   def __init__(self, value=None):
       """
       Initializes this NestedInteger with either an integer or a list.
       :type value: int or list
       """
       self._is_int = False
       self._integer = None
       self._list = None

       if isinstance(value, int):
           self._is_int = True
           self._integer = value
       elif isinstance(value, list):
           self._is_int = False
           self._list = [NestedInteger(item) for item in value]

   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       return self._is_int

   def getInteger(self) -> int:
       """
       @return The single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       return self._integer

   def getList(self) -> list:
       """
       @return The nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype list[NestedInteger]
       """
       return self._list

class Solution:
    def depthSum(self, nestedList: 'list[NestedInteger]') -> int:
        def dfs(nested_items: 'list[NestedInteger]', depth: int) -> int:
            current_level_sum = 0
            for item in nested_items:
                if item.isInteger():
                    current_level_sum += item.getInteger() * depth
                else:
                    current_level_sum += dfs(item.getList(), depth + 1)
            return current_level_sum

        return dfs(nestedList, 1)