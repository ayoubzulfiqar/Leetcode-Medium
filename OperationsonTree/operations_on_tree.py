import collections

class LockingTree:

    def __init__(self, parent: list[int]):
        self.parent = parent
        self.n = len(parent)
        self.locked_by = [0] * self.n  # 0 means unlocked, otherwise stores user_id
        
        self.children = collections.defaultdict(list)
        for i in range(1, self.n):
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked_by[num] == 0:
            self.locked_by[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked_by[num] == user:
            self.locked_by[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        # Condition 1: The node is unlocked
        if self.locked_by[num] != 0:
            return False

        # Condition 3: It does not have any locked ancestors
        curr_ancestor = num
        while curr_ancestor != -1:
            if self.locked_by[curr_ancestor] != 0:
                return False
            curr_ancestor = self.parent[curr_ancestor]
        
        # Condition 2: It has at least one locked descendant
        locked_descendant_found = False
        descendants_to_unlock = []
        
        q = collections.deque()
        for child in self.children[num]:
            q.append(child)
            
        while q:
            curr_descendant = q.popleft()
            
            if self.locked_by[curr_descendant] != 0:
                locked_descendant_found = True
            
            descendants_to_unlock.append(curr_descendant)
            
            for child_of_descendant in self.children[curr_descendant]:
                q.append(child_of_descendant)
        
        if not locked_descendant_found:
            return False
            
        # All conditions met, perform upgrade
        self.locked_by[num] = user # Lock the node
        
        # Unlock all descendants
        for descendant in descendants_to_unlock:
            self.locked_by[descendant] = 0
            
        return True