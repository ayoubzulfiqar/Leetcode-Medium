class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        def checkPath(list_node: ListNode, tree_node: TreeNode) -> bool:
            if not list_node:
                return True
            
            if not tree_node or list_node.val != tree_node.val:
                return False
            
            return checkPath(list_node.next, tree_node.left) or \
                   checkPath(list_node.next, tree_node.right)

        if not root:
            return False
        
        if checkPath(head, root):
            return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)