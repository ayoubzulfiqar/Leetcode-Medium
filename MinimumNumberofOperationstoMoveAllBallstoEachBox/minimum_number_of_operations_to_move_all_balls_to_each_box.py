class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        answer = [0] * n

        for i in range(n):
            current_operations = 0
            for j in range(n):
                if boxes[j] == '1':
                    current_operations += abs(i - j)
            answer[i] = current_operations
        
        return answer