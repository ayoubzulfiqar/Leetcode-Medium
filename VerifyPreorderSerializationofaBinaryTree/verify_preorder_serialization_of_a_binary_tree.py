class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        
        diff = 1 
        
        for i in range(len(nodes)):
            if diff == 0:
                return False
            
            node = nodes[i]
            if node == '#':
                diff -= 1
            else:
                diff += 1
                
        return diff == 0