class Solution:
    def maxBoxesInWarehouse(self, boxes: list[int], warehouse: list[int]) -> int:
        n = len(boxes)
        m = len(warehouse)

        if n == 0 or m == 0:
            return 0

        effective_warehouse = [0] * m
        min_height_so_far = float('inf')
        for i in range(m):
            min_height_so_far = min(min_height_so_far, warehouse[i])
            effective_warehouse[i] = min_height_so_far
        
        boxes.sort()

        box_ptr = 0
        count = 0

        for room_height in effective_warehouse:
            if box_ptr < n and boxes[box_ptr] <= room_height:
                count += 1
                box_ptr += 1
            else:
                break
        
        return count