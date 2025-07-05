class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def _find_lca(root, p, q):
    if root is None or root == p or root == q:
        return root

    left_lca = _find_lca(root.left, p, q)
    right_lca = _find_lca(root.right, p, q)

    if left_lca and right_lca:
        return root
    elif left_lca:
        return left_lca
    else:
        return right_lca

def _find_depth(root, target, depth):
    if root is None:
        return -1
    if root == target:
        return depth

    left_depth = _find_depth(root.left, target, depth + 1)
    if left_depth != -1:
        return left_depth

    right_depth = _find_depth(root.right, target, depth + 1)
    return right_depth

def _find_node_by_val(current_root, val):
    if current_root is None:
        return None
    if current_root.val == val:
        return current_root
    left_found = _find_node_by_val(current_root.left, val)
    if left_found:
        return left_found
    return _find_node_by_val(current_root.right, val)

def find_distance_in_binary_tree(root, node1_val, node2_val):
    node1 = _find_node_by_val(root, node1_val)
    node2 = _find_node_by_val(root, node2_val)

    if not node1 or not node2:
        return -1

    lca_node = _find_lca(root, node1, node2)

    if lca_node is None:
        return -1

    dist1 = _find_depth(lca_node, node1, 0)
    dist2 = _find_depth(lca_node, node2, 0)

    if dist1 == -1 or dist2 == -1:
        return -1

    return dist1 + dist2