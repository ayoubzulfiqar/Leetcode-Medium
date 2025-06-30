class Solution:
    def verifyPreorder(self, preorder: list[int]) -> bool:
        stack = []
        lower_bound = float('-inf')

        for node_val in preorder:
            if node_val < lower_bound:
                return False

            while stack and node_val > stack[-1]:
                lower_bound = stack.pop()
            
            stack.append(node_val)
        
        return True