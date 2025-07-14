import pandas as pd

def solve():
    transactions = pd.DataFrame({
        'transaction_id': [1, 2, 3, 4, 5, 6],
        'amount': [150, 200, 75, 300, 50, 120],
        'transaction_date': ['2024-07-01', '2024-07-01', '2024-07-01', '2024-07-02', '2024-07-02', '2024-07-03']
    })

    transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'])

    result = transactions.groupby('transaction_date').agg(
        odd_sum=('amount', lambda x: x[x % 2 != 0].sum()),
        even_sum=('amount', lambda x: x[x % 2 == 0].sum())
    ).reset_index()

    result = result.sort_values(by='transaction_date', ascending=True)

    result['transaction_date'] = result['transaction_date'].dt.strftime('%Y-%m-%d')

    return result