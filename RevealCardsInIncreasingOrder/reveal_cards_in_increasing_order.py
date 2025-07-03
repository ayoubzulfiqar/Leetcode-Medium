import collections

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        n = len(deck)
        sorted_deck = sorted(deck)
        
        indices = collections.deque(range(n))
        
        result = [0] * n 
        
        for card in sorted_deck:
            reveal_idx = indices.popleft()
            result[reveal_idx] = card
            
            if indices:
                indices.append(indices.popleft())
                
        return result