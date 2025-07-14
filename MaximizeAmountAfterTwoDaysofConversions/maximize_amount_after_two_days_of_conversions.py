class Solution:
    def maximizeAmount(self, initialCurrency: str, pairs1: list[list[str]], rates1: list[float], pairs2: list[list[str]], rates2: list[float]) -> float:
        
        all_currencies_set = set()
        all_currencies_set.add(initialCurrency)
        for p in pairs1:
            all_currencies_set.add(p[0])
            all_currencies_set.add(p[1])
        for p in pairs2:
            all_currencies_set.add(p[0])
            all_currencies_set.add(p[1])
        
        currency_list = sorted(list(all_currencies_set))
        currency_to_idx = {currency: i for i, currency in enumerate(currency_list)}
        num_currencies = len(currency_list)
        
        initial_currency_idx = currency_to_idx[initialCurrency]

        def floyd_warshall(pairs, rates):
            max_rates = [[0.0] * num_currencies for _ in range(num_currencies)]
            
            for i in range(num_currencies):
                max_rates[i][i] = 1.0
            
            for i, (start_curr, target_curr) in enumerate(pairs):
                start_idx = currency_to_idx[start_curr]
                target_idx = currency_to_idx[target_curr]
                rate = rates[i]
                
                max_rates[start_idx][target_idx] = max(max_rates[start_idx][target_idx], rate)
                max_rates[target_idx][start_idx] = max(max_rates[target_idx][start_idx], 1.0 / rate)
            
            for k in range(num_currencies):
                for i in range(num_currencies):
                    for j in range(num_currencies):
                        if max_rates[i][k] > 0 and max_rates[k][j] > 0:
                            max_rates[i][j] = max(max_rates[i][j], max_rates[i][k] * max_rates[k][j])
            
            return max_rates

        max_rates_day1 = floyd_warshall(pairs1, rates1)
        
        day1_max_amounts = [0.0] * num_currencies
        for i in range(num_currencies):
            day1_max_amounts[i] = max_rates_day1[initial_currency_idx][i]
        
        max_rates_day2 = floyd_warshall(pairs2, rates2)
        
        max_final_amount = 0.0
        
        for i in range(num_currencies):
            amount_of_currency_i_on_day1 = day1_max_amounts[i]
            
            if amount_of_currency_i_on_day1 > 0:
                rate_to_initial_currency_on_day2 = max_rates_day2[i][initial_currency_idx]
                
                max_final_amount = max(max_final_amount, amount_of_currency_i_on_day1 * rate_to_initial_currency_on_day2)
        
        return max_final_amount