class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        val_to_node = {}
        children_set = set()

        for parent_val, child_val, is_left in descriptions:
            if parent_val not in val_to_node:
                val_to_node[parent_val] = TreeNode(parent_val)
            parent_node = val_to_node[parent_val]

            if child_val not in val_to_node:
                val_to_node[child_val] = TreeNode(child_val)
            child_node = val_to_node[child_val]

            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            children_set.add(child_val)

        root_val = -1
        for node_val in val_to_node:
            if node_val not in children_set:
                root_val = node_val
                break
        
        return val_to_node[root_val]