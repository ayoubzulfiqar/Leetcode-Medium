class Solution:
    def stoneGameVI(self, aliceValues: list[int], bobValues: list[int]) -> int:
        n = len(aliceValues)
        
        stones_data = []
        for i in range(n):
            stones_data.append((aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]))
            
        stones_data.sort(key=lambda x: x[0], reverse=True)
        
        alice_total_score = 0
        bob_total_score = 0
        
        for i in range(n):
            current_stone = stones_data[i]
            if i % 2 == 0:
                alice_total_score += current_stone[1]
            else:
                bob_total_score += current_stone[2]
                
        if alice_total_score > bob_total_score:
            return 1
        elif alice_total_score < bob_total_score:
            return -1
        else:
            return 0