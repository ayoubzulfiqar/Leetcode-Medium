```python
import collections
from typing import List

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king_name = kingName
        self.children = collections.defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(person_name):
            # Only add the person to the inheritance order if they are not dead.
            if person_name not in self.dead:
                order.append(person_name)

            # Recursively visit children in their birth order.
            # The children are stored in the order they were born (appended).
            for child in self.children[person_name]:
                dfs(child)

        # Start the DFS traversal from the king.
        dfs(self.king_name)
        return order

```