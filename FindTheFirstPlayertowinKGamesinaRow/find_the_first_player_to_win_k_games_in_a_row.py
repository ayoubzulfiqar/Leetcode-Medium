import collections

class Solution:
    def getWinner(self, skills: list[int], k: int) -> int:
        n = len(skills)

        # Optimization: If k is greater than or equal to n-1, the player with the
        # highest skill will eventually reach the front and win all remaining games.
        # Once the player with the maximum skill is at the front, they will never lose.
        # Thus, they will be the first to achieve k consecutive wins if k is large enough
        # to defeat all other n-1 players.
        if k >= n - 1:
            max_skill = -1
            max_skill_idx = -1
            for i, skill in enumerate(skills):
                if skill > max_skill:
                    max_skill = skill
                    max_skill_idx = i
            return max_skill_idx

        # Initialize the queue with player initial indices (0 to n-1)
        # We use player indices to refer back to their skill levels in the skills array
        queue = collections.deque(range(n))

        # current_winner_idx stores the initial index of the player currently on a winning streak
        # consecutive_wins stores the number of games won consecutively by current_winner_idx
        current_winner_idx = -1
        consecutive_wins = 0

        while True:
            # Get the first two players from the queue
            player1_idx = queue.popleft()
            player2_idx = queue.popleft()

            skill1 = skills[player1_idx]
            skill2 = skills[player2_idx]

            # Determine the winner and loser of the current game
            if skill1 > skill2:
                winner_idx = player1_idx
                loser_idx = player2_idx
            else: # skill2 > skill1 because all skills are unique
                winner_idx = player2_idx
                loser_idx = player1_idx

            # Update consecutive win count
            if current_winner_idx == -1: # This is the very first game played
                current_winner_idx = winner_idx
                consecutive_wins = 1
            elif winner_idx == current_winner_idx:
                # The current winner continues their streak
                consecutive_wins += 1
            else:
                # A new player has won, reset the streak
                current_winner_idx = winner_idx
                consecutive_wins = 1

            # Check if the winning condition is met
            if consecutive_wins == k:
                return current_winner_idx

            # Re-queue the players: winner to the front, loser to the back
            queue.appendleft(winner_idx)
            queue.append(loser_idx)