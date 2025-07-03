import math

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            current_shelf_width = 0
            current_shelf_max_height = 0
            
            for j in range(i - 1, -1, -1):
                book_thickness = books[j][0]
                book_height = books[j][1]
                
                current_shelf_width += book_thickness
                
                if current_shelf_width > shelfWidth:
                    break
                
                current_shelf_max_height = max(current_shelf_max_height, book_height)
                
                dp[i] = min(dp[i], dp[j] + current_shelf_max_height)
                
        return dp[n]