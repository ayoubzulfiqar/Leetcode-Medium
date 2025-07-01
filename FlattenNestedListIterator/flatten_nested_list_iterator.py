class NestedInteger:
   def isInteger(self) -> bool:
       pass

   def getInteger(self) -> int:
       pass

   def getList(self) -> ['NestedInteger']:
       pass

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened_list = []
        self._flatten(nestedList)
        self.current_index = 0

    def _flatten(self, nested_items: [NestedInteger]):
        for item in nested_items:
            if item.isInteger():
                self.flattened_list.append(item.getInteger())
            else:
                self._flatten(item.getList())

    def next(self) -> int:
        val = self.flattened_list[self.current_index]
        self.current_index += 1
        return val

    def hasNext(self) -> bool:
        return self.current_index < len(self.flattened_list)