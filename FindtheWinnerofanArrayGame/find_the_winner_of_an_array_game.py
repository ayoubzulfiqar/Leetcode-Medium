class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        current_winner = arr[0]
        win_count = 0

        for i in range(1, len(arr)):
            challenger = arr[i]
            if current_winner > challenger:
                win_count += 1
            else:
                current_winner = challenger
                win_count = 1
            
            if win_count == k:
                return current_winner
        
        return current_winner