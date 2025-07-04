class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return -1

            child_heights = []
            for child in node.children:
                child_heights.append(dfs(child))

            child_heights.sort(reverse=True)

            current_node_height = 0
            if child_heights:
                current_node_height = 1 + child_heights[0]

            current_node_diameter_through_it = 0
            if len(child_heights) >= 2:
                current_node_diameter_through_it = (1 + child_heights[0]) + (1 + child_heights[1])
            elif len(child_heights) == 1:
                current_node_diameter_through_it = 1 + child_heights[0]

            self.max_diameter = max(self.max_diameter, current_node_diameter_through_it)

            return current_node_height

        if not root:
            return 0

        dfs(root)
        return self.max_diameter