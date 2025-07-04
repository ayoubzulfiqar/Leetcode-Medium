class Solution:
    def putBoxesIntoTheWarehouseII(self, boxes: list[int], warehouse: list[int]) -> int:
        boxes.sort()
        
        left = 0
        right = len(warehouse) - 1
        
        count = 0
        
        for box_width in boxes:
            if left > right:
                break
            
            can_fit_left = (box_width <= warehouse[left])
            can_fit_right = (box_width <= warehouse[right])
            
            if can_fit_left and can_fit_right:
                if warehouse[left] <= warehouse[right]:
                    left += 1
                else: 
                    right -= 1
                count += 1
            elif can_fit_left:
                left += 1
                count += 1
            elif can_fit_right:
                right -= 1
                count += 1
            else:
                break
                
        return count