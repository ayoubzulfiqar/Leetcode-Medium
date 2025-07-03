import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.q = collections.deque()

        bfs_q = collections.deque([root])
        while bfs_q:
            node = bfs_q.popleft()
            
            if not node.left or not node.right:
                self.q.append(node)
            
            if node.left:
                bfs_q.append(node.left)
            if node.right:
                bfs_q.append(node.right)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        
        parent = self.q[0]
        
        parent_val = parent.val
        
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.q.popleft()
            
        self.q.append(new_node)
        
        return parent_val

    def get_root(self) -> TreeNode:
        return self.root