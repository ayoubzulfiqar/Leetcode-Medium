class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_node = 0
        n = len(gas)

        for i in range(n):
            diff = gas[i] - cost[i]
            total_tank += diff
            current_tank += diff

            if current_tank < 0:
                current_tank = 0
                start_node = i + 1
        
        if total_tank < 0:
            return -1
        else:
            return start_node