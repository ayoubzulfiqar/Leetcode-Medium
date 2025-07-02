import collections

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        counts = collections.Counter(hand)
        sorted_unique_cards = sorted(counts.keys())

        for start_card in sorted_unique_cards:
            if counts[start_card] == 0:
                continue

            current_count = counts[start_card]

            for i in range(groupSize):
                card_to_check = start_card + i
                if counts[card_to_check] < current_count:
                    return False
                counts[card_to_check] -= current_count
        
        return True