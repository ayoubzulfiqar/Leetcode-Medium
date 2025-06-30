class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        if not costs:
            return 0

        num_houses = len(costs)

        prev_cost_red = costs[0][0]
        prev_cost_blue = costs[0][1]
        prev_cost_green = costs[0][2]

        for i in range(1, num_houses):
            curr_cost_red = costs[i][0] + min(prev_cost_blue, prev_cost_green)
            curr_cost_blue = costs[i][1] + min(prev_cost_red, prev_cost_green)
            curr_cost_green = costs[i][2] + min(prev_cost_red, prev_cost_blue)

            prev_cost_red = curr_cost_red
            prev_cost_blue = curr_cost_blue
            prev_cost_green = curr_cost_green
        
        return min(prev_cost_red, prev_cost_blue, prev_cost_green)