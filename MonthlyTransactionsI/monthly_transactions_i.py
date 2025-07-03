from collections import defaultdict

def monthly_transactions(transactions):
    aggregated_data = defaultdict(lambda: {
        'trans_count': 0,
        'approved_count': 0,
        'trans_total_amount': 0,
        'approved_total_amount': 0
    })

    for transaction in transactions:
        trans_date = transaction['trans_date']
        country = transaction['country']
        state = transaction['state']
        amount = transaction['amount']

        month_str = trans_date[:7]

        key = (month_str, country)

        aggregated_data[key]['trans_count'] += 1
        aggregated_data[key]['trans_total_amount'] += amount

        if state == 'approved':
            aggregated_data[key]['approved_count'] += 1
            aggregated_data[key]['approved_total_amount'] += amount

    result = []
    for (month, country), data in aggregated_data.items():
        result.append({
            'month': month,
            'country': country,
            'trans_count': data['trans_count'],
            'approved_count': data['approved_count'],
            'trans_total_amount': data['trans_total_amount'],
            'approved_total_amount': data['approved_total_amount']
        })

    return result