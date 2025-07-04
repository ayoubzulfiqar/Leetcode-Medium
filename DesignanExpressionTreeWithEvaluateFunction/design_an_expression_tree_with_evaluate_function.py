class Node:
    def evaluate(self):
        raise NotImplementedError

class OperandNode(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

class OperatorNode(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def evaluate(self):
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        if self.operator == '+':
            return left_val + right_val
        elif self.operator == '-':
            return left_val - right_val
        elif self.operator == '*':
            return left_val * right_val
        elif self.operator == '/':
            if right_val == 0:
                raise ZeroDivisionError("Division by zero")
            return left_val / right_val
        else:
            raise ValueError(f"Unknown operator: {self.operator}")

class ExpressionTree:
    def __init__(self, root_node):
        self.root = root_node

    def evaluate(self):
        if not self.root:
            return None
        return self.root.evaluate()

if __name__ == '__main__':
    node_3 = OperandNode(3)
    node_4 = OperandNode(4)
    node_plus = OperatorNode('+', node_3, node_4)

    node_5 = OperandNode(5)
    node_2 = OperandNode(2)
    node_minus = OperatorNode('-', node_5, node_2)

    root_node_complex = OperatorNode('*', node_plus, node_minus)
    tree_complex = ExpressionTree(root_node_complex)
    result_complex = tree_complex.evaluate()
    assert result_complex == 21

    node_10 = OperandNode(10)
    node_2_div = OperandNode(2)
    root_div = OperatorNode('/', node_10, node_2_div)
    tree_div = ExpressionTree(root_div)
    result_div = tree_div.evaluate()
    assert result_div == 5.0

    node_zero = OperandNode(0)
    root_div_by_zero = OperatorNode('/', node_10, node_zero)
    tree_div_by_zero = ExpressionTree(root_div_by_zero)
    try:
        tree_div_by_zero.evaluate()
        assert False, "ZeroDivisionError was not raised"
    except ZeroDivisionError:
        pass