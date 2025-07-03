class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        
        right_forces = [0] * n
        current_force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                current_force = n
            elif dominoes[i] == 'L':
                current_force = 0
            else:
                if current_force > 0:
                    current_force -= 1
            right_forces[i] = current_force
        
        left_forces = [0] * n
        current_force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                current_force = n
            elif dominoes[i] == 'R':
                current_force = 0
            else:
                if current_force > 0:
                    current_force -= 1
            left_forces[i] = current_force
            
        result = [''] * n
        for i in range(n):
            net_force = right_forces[i] - left_forces[i]
            if net_force > 0:
                result[i] = 'R'
            elif net_force < 0:
                result[i] = 'L'
            else:
                result[i] = '.'
                
        return "".join(result)