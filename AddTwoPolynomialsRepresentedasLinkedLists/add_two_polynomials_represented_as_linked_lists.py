class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class Solution:
    def addPolynomials(self, poly1: Node, poly2: Node) -> Node:
        dummy_head = Node(0, 0)
        current = dummy_head

        while poly1 and poly2:
            if poly1.exponent > poly2.exponent:
                current.next = Node(poly1.coefficient, poly1.exponent)
                current = current.next
                poly1 = poly1.next
            elif poly2.exponent > poly1.exponent:
                current.next = Node(poly2.coefficient, poly2.exponent)
                current = current.next
                poly2 = poly2.next
            else: # poly1.exponent == poly2.exponent
                sum_coeff = poly1.coefficient + poly2.coefficient
                if sum_coeff != 0:
                    current.next = Node(sum_coeff, poly1.exponent)
                    current = current.next
                poly1 = poly1.next
                poly2 = poly2.next
        
        # Append remaining terms from poly1
        while poly1:
            current.next = Node(poly1.coefficient, poly1.exponent)
            current = current.next
            poly1 = poly1.next

        # Append remaining terms from poly2
        while poly2:
            current.next = Node(poly2.coefficient, poly2.exponent)
            current = current.next
            poly2 = poly2.next

        return dummy_head.next