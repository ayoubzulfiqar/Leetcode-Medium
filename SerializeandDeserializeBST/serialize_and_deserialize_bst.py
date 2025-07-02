class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""

        nodes = []
        stack = [root]
        while stack:
            node = stack.pop()
            nodes.append(str(node.val))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return ",".join(nodes)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        
        nodes_str = data.split(',')
        nodes_int = [int(x) for x in nodes_str]
        
        self.idx = 0 

        def _deserialize_helper(lower_bound, upper_bound):
            if self.idx >= len(nodes_int):
                return None
            
            val = nodes_int[self.idx]
            
            if val < lower_bound or val > upper_bound:
                return None
            
            node = TreeNode(val)
            self.idx += 1
            
            node.left = _deserialize_helper(lower_bound, node.val)
            node.right = _deserialize_helper(node.val, upper_bound)
            
            return node
        
        return _deserialize_helper(float('-inf'), float('inf'))