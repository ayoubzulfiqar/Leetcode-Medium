class Leaderboard:

    def __init__(self):
        self.player_scores = {}

    def add_score(self, playerId: int, score: int) -> None:
        # If the player exists, their score is updated to the new score.
        # If the player does not exist, they are added with the given score.
        self.player_scores[playerId] = score

    def top(self, K: int) -> int:
        # Get all scores from the leaderboard.
        scores = list(self.player_scores.values())
        
        # Sort the scores in descending order to find the top scores.
        scores.sort(reverse=True)
        
        # Calculate the sum of the top K scores.
        total_sum = 0
        # Iterate up to K scores or the total number of available scores, whichever is smaller.
        for i in range(min(K, len(scores))):
            total_sum += scores[i]
            
        return total_sum

    def reset(self, playerId: int) -> None:
        # Remove the player from the leaderboard.
        # If the player does not exist, nothing happens.
        if playerId in self.player_scores:
            del self.player_scores[playerId]