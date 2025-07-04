class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def are_equivalent_trees(root1, root2):
    def _get_terms(node, operator):
        """
        Recursively collects all terms for a given associative operator.
        For example, for (a + (b + c)), it would return [a, b, c] by flattening.
        """
        if not node:
            return []
        
        # If the current node's value is the same as the target operator,
        # it means we can flatten its children into the list of terms.
        if node.val == operator:
            terms = []
            terms.extend(_get_terms(node.left, operator))
            terms.extend(_get_terms(node.right, operator))
            return terms
        else:
            # If it's a different operator or an operand, treat it as a single term
            # and convert it to its canonical string representation.
            return [_get_canonical_string_recursive(node)]

    def _get_canonical_string_recursive(node):
        """
        Generates a canonical string representation of the expression tree.
        Handles commutativity and associativity for '+' and '*' operators.
        """
        if not node:
            return ""

        # If it's a leaf node (operand), return its string value.
        if not node.left and not node.right:
            return str(node.val)

        # Handle associative and commutative operators: '+' and '*'
        if node.val in ('+', '*'):
            # Collect all terms for this operator by flattening the tree.
            terms = _get_terms(node, node.val)
            # Sort terms lexicographically to handle commutativity.
            terms.sort()
            # Join terms with the operator and enclose in parentheses.
            return "(" + node.val.join(terms) + ")"
        
        # Handle non-associative and non-commutative operators: '-' and '/'
        # These do not flatten or reorder their children.
        left_str = _get_canonical_string_recursive(node.left)
        right_str = _get_canonical_string_recursive(node.right)
        
        # Enclose the sub-expression in parentheses to preserve order of operations.
        return f"({left_str}{node.val}{right_str})"

    # Generate canonical strings for both trees and compare them.
    s1 = _get_canonical_string_recursive(root1)
    s2 = _get_canonical_string_recursive(root2)
    
    return s1 == s2