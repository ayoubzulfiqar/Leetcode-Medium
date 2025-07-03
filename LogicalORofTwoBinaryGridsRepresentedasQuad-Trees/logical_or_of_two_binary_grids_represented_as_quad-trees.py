class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # Case 1: Both nodes are leaves
        if quadTree1.isLeaf and quadTree2.isLeaf:
            # The value of the resulting leaf node is the logical OR of their values
            return Node(quadTree1.val or quadTree2.val, True)

        # Case 2: One node is a leaf, the other is not
        # If quadTree1 is a leaf:
        if quadTree1.isLeaf:
            # If quadTree1 represents an area of all 1s (val is True),
            # then the logical OR of this area with any other area will result in an area of all 1s.
            if quadTree1.val:
                return Node(True, True)
            # If quadTree1 represents an area of all 0s (val is False),
            # then the logical OR of this area with quadTree2 simply results in quadTree2.
            # This is handled by falling through to the recursive step, where quadTree1 (False leaf)
            # will be OR'd with each of quadTree2's children, effectively copying quadTree2.
            pass

        # If quadTree2 is a leaf (and quadTree1 is not, or quadTree1 was a False leaf that fell through):
        if quadTree2.isLeaf:
            # If quadTree2 represents an area of all 1s (val is True),
            # then the logical OR of this area with any other area will result in an area of all 1s.
            if quadTree2.val:
                return Node(True, True)
            # If quadTree2 represents an area of all 0s (val is False),
            # then the logical OR of this area with quadTree1 simply results in quadTree1.
            # This is handled by falling through to the recursive step, where quadTree2 (False leaf)
            # will be OR'd with each of quadTree1's children, effectively copying quadTree1.
            pass

        # Case 3: Neither node is a leaf, or one is a False leaf (handled by recursive calls)
        # In this case, we need to recursively compute the OR for each of the four quadrants.
        new_topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        new_topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        new_bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        new_bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        # After computing the children, check if the current node can be simplified into a leaf.
        # This happens if all four children are leaves and have the same value.
        if (new_topLeft.isLeaf and new_topRight.isLeaf and
                new_bottomLeft.isLeaf and new_bottomRight.isLeaf and
                new_topLeft.val == new_topRight.val == new_bottomLeft.val == new_bottomRight.val):
            # If they can be simplified, create a new leaf node with that common value.
            return Node(new_topLeft.val, True)
        else:
            # Otherwise, create a new non-leaf node with the computed children.
            # The 'val' attribute for a non-leaf node can be arbitrary.
            # Following the example output, we set it to False.
            return Node(False, False, new_topLeft, new_topRight, new_bottomLeft, new_bottomRight)