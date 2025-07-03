class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        parsed_transactions = []
        for i, tx_str in enumerate(transactions):
            parts = tx_str.split(',')
            name = parts[0]
            time = int(parts[1])
            amount = int(parts[2])
            city = parts[3]
            parsed_transactions.append([name, time, amount, city, i])

        invalid_indices = set()

        for i in range(len(parsed_transactions)):
            name_i, time_i, amount_i, city_i, original_idx_i = parsed_transactions[i]

            # Rule 1: Amount exceeds $1000
            if amount_i > 1000:
                invalid_indices.add(original_idx_i)

            # Rule 2: Check against other transactions
            for j in range(len(parsed_transactions)):
                if i == j:
                    continue # Don't compare a transaction with itself

                name_j, time_j, amount_j, city_j, original_idx_j = parsed_transactions[j]

                # Same name, different city, and within 60 minutes
                if name_i == name_j and city_i != city_j and abs(time_i - time_j) <= 60:
                    invalid_indices.add(original_idx_i)
                    invalid_indices.add(original_idx_j)

        result = []
        for idx in invalid_indices:
            result.append(transactions[idx])

        return result