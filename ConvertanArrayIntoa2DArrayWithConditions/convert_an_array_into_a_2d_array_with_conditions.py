class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        result = []

        for num in nums:
            placed = False
            # Try to place the current number in an existing row
            for row in result:
                if num not in row:
                    row.append(num)
                    placed = True
                    break  # Number placed, move to the next number in nums
            
            # If the number could not be placed in any existing row, create a new row for it
            if not placed:
                result.append([num])
        
        return result