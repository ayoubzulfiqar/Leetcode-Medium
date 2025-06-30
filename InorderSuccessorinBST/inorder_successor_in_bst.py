class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderSuccessor(root: TreeNode, p: TreeNode) -> TreeNode:
    successor = None
    
    current = root
    while current:
        if p.val < current.val:
            # If p's value is less than current's value,
            # current could be the successor.
            # We then try to find a smaller successor in the left subtree.
            successor = current
            current = current.left
        elif p.val > current.val:
            # If p's value is greater than current's value,
            # p must be in the right subtree.
            current = current.right
        else: # p.val == current.val, we found the node p
            # Case 1: p has a right child.
            # The successor is the leftmost node in p's right subtree.
            if current.right:
                temp = current.right
                while temp.left:
                    temp = temp.left
                successor = temp
            # Case 2: p does not have a right child.
            # In this case, the successor would have been set by an ancestor
            # in the 'p.val < current.val' branch during the traversal.
            # If no such ancestor was found (e.g., p is the largest element),
            # 'successor' will remain None.
            break # We found p, so we can stop searching.
            
    return successor