import heapq

class Solution:
    def minimumCost(self, n: int, discounts: list[int], fares: list[list[int]], k: int) -> float:
        min_cost = [[float('inf')] * (k + 1) for _ in range(n)]

        pq = [(0.0, 0, 0)]
        min_cost[0][0] = 0.0

        while pq:
            current_cost, u, used_discounts = heapq.heappop(pq)

            if current_cost > min_cost[u][used_discounts]:
                continue

            for v in range(n):
                if u == v:
                    continue

                fare_uv = fares[u][v]

                # Option 1: Travel from u to v without using a discount
                new_cost_no_discount = current_cost + fare_uv
                new_used_discounts_no_discount = used_discounts

                if new_cost_no_discount < min_cost[v][new_used_discounts_no_discount]:
                    min_cost[v][new_used_discounts_no_discount] = new_cost_no_discount
                    heapq.heappush(pq, (new_cost_no_discount, v, new_used_discounts_no_discount))

                # Option 2: Travel from u to v using a discount
                if used_discounts < k:
                    discount_percentage = discounts[u]
                    discounted_fare_uv = fare_uv * (100 - discount_percentage) / 100.0
                    
                    new_cost_with_discount = current_cost + discounted_fare_uv
                    new_used_discounts_with_discount = used_discounts + 1

                    if new_cost_with_discount < min_cost[v][new_used_discounts_with_discount]:
                        min_cost[v][new_used_discounts_with_discount] = new_cost_with_discount
                        heapq.heappush(pq, (new_cost_with_discount, v, new_used_discounts_with_discount))

        min_cost_to_target = float('inf')
        for i in range(k + 1):
            min_cost_to_target = min(min_cost_to_target, min_cost[n-1][i])

        return min_cost_to_target