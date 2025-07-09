from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        current_node = head

        while top <= bottom and left <= right:
            # Traverse Right
            for c in range(left, right + 1):
                if current_node:
                    matrix[top][c] = current_node.val
                    current_node = current_node.next
                else:
                    return matrix # Linked list exhausted, return current matrix
            top += 1

            # Traverse Down
            for r in range(top, bottom + 1):
                if current_node:
                    matrix[r][right] = current_node.val
                    current_node = current_node.next
                else:
                    return matrix
            right -= 1

            # Traverse Left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    if current_node:
                        matrix[bottom][c] = current_node.val
                        current_node = current_node.next
                    else:
                        return matrix
                bottom -= 1

            # Traverse Up
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    if current_node:
                        matrix[r][left] = current_node.val
                        current_node = current_node.next
                    else:
                        return matrix
                left += 1
        
        return matrix