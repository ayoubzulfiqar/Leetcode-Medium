class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        loss_counts = {}
        all_players = set()

        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)
            loss_counts[loser] = loss_counts.get(loser, 0) + 1
        
        no_losses = []
        one_loss = []

        for player in sorted(all_players):
            losses = loss_counts.get(player, 0)
            if losses == 0:
                no_losses.append(player)
            elif losses == 1:
                one_loss.append(player)
        
        return [no_losses, one_loss]