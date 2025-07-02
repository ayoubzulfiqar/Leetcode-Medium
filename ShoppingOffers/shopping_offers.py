class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        n = len(price)
        memo = {}

        filtered_special = []
        for offer in special:
            offer_price = offer[n]
            individual_cost_of_offer_items = 0
            for i in range(n):
                individual_cost_of_offer_items += offer[i] * price[i]
            
            if offer_price < individual_cost_of_offer_items:
                filtered_special.append(offer)

        def solve(current_needs_tuple: tuple) -> int:
            if current_needs_tuple in memo:
                return memo[current_needs_tuple]

            cost = 0
            for i in range(n):
                cost += current_needs_tuple[i] * price[i]
            
            for offer in filtered_special:
                next_needs_list = list(current_needs_tuple)
                can_apply = True
                
                for i in range(n):
                    if next_needs_list[i] < offer[i]:
                        can_apply = False
                        break
                    next_needs_list[i] -= offer[i]
                
                if can_apply:
                    offer_price = offer[n]
                    cost = min(cost, offer_price + solve(tuple(next_needs_list)))
            
            memo[current_needs_tuple] = cost
            return cost

        return solve(tuple(needs))