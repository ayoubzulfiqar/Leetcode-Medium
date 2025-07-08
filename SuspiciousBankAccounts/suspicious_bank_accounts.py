import datetime
from collections import defaultdict

def find_suspicious_accounts(transactions, config):
    suspicious_accounts = set()

    high_value_threshold = config.get('HIGH_VALUE_THRESHOLD', 10000)
    blacklisted_accounts = config.get('BLACKLISTED_ACCOUNTS', set())
    max_transactions_per_day = config.get('MAX_TRANSACTIONS_PER_DAY', 5)
    max_daily_volume = config.get('MAX_DAILY_VOLUME', 50000)

    transactions_count_by_account_day = defaultdict(lambda: defaultdict(int))
    volume_by_account_day = defaultdict(lambda: defaultdict(float))

    for transaction in transactions:
        sender = transaction['sender']
        receiver = transaction['receiver']
        amount = transaction['amount']
        timestamp_str = transaction['timestamp']

        transaction_date = datetime.datetime.fromisoformat(timestamp_str).date()

        if amount > high_value_threshold:
            suspicious_accounts.add(sender)
            suspicious_accounts.add(receiver)

        if sender in blacklisted_accounts:
            suspicious_accounts.add(sender)
            suspicious_accounts.add(receiver)
        if receiver in blacklisted_accounts:
            suspicious_accounts.add(receiver)
            suspicious_accounts.add(sender)

        transactions_count_by_account_day[sender][transaction_date] += 1
        volume_by_account_day[sender][transaction_date] += amount
        transactions_count_by_account_day[receiver][transaction_date] += 1
        volume_by_account_day[receiver][transaction_date] += amount

    for account_id, daily_counts in transactions_count_by_account_day.items():
        for date, count in daily_counts.items():
            if count > max_transactions_per_day:
                suspicious_accounts.add(account_id)

    for account_id, daily_volumes in volume_by_account_day.items():
        for date, total_volume in daily_volumes.items():
            if total_volume > max_daily_volume:
                suspicious_accounts.add(account_id)

    return suspicious_accounts

if __name__ == '__main__':
    transactions_data = [
        {'sender': 'Acc001', 'receiver': 'Acc002', 'amount': 12000, 'timestamp': '2023-01-15T10:00:00'},
        {'sender': 'Acc003', 'receiver': 'Acc004', 'amount': 500, 'timestamp': '2023-01-15T11:00:00'},
        {'sender': 'Acc005', 'receiver': 'Acc006', 'amount': 2000, 'timestamp': '2023-01-15T12:00:00'},
        {'sender': 'Acc007', 'receiver': 'Acc008', 'amount': 300, 'timestamp': '2023-01-15T13:00:00'},
        {'sender': 'Acc009', 'receiver': 'Acc010', 'amount': 100, 'timestamp': '2023-01-15T14:00:00'},
        {'sender': 'Acc011', 'receiver': 'Acc012', 'amount': 50, 'timestamp': '2023-01-15T15:00:00'},
        {'sender': 'Acc013', 'receiver': 'Acc014', 'amount': 200, 'timestamp': '2023-01-15T16:00:00'},
        {'sender': 'Acc015', 'receiver': 'Acc016', 'amount': 1000, 'timestamp': '2023-01-15T17:00:00'},
        {'sender': 'Acc017', 'receiver': 'Acc018', 'amount': 5000, 'timestamp': '2023-01-15T18:00:00'},
        {'sender': 'Acc019', 'receiver': 'Acc020', 'amount': 200, 'timestamp': '2023-01-15T19:00:00'},

        {'sender': 'Acc021', 'receiver': 'BlacklistedAcc', 'amount': 100, 'timestamp': '2023-01-16T09:00:00'},
        {'sender': 'BlacklistedAcc', 'receiver': 'Acc022', 'amount': 5000, 'timestamp': '2023-01-16T10:00:00'},

        {'sender': 'FrequentAcc', 'receiver': 'AccB', 'amount': 100, 'timestamp': '2023-01-17T09:00:00'},
        {'sender': 'AccB', 'receiver': 'FrequentAcc', 'amount': 100, 'timestamp': '2023-01-17T09:10:00'},
        {'sender': 'FrequentAcc', 'receiver': 'AccC', 'amount': 100, 'timestamp': '2023-01-17T09:20:00'},
        {'sender': 'AccC', 'receiver': 'FrequentAcc', 'amount': 100, 'timestamp': '2023-01-17T09:30:00'},
        {'sender': 'FrequentAcc', 'receiver': 'AccD', 'amount': 100, 'timestamp': '2023-01-17T09:40:00'},
        {'sender': 'AccD', 'receiver': 'FrequentAcc', 'amount': 100, 'timestamp': '2023-01-17T09:50:00'},

        {'sender': 'VolumeAcc', 'receiver': 'AccX', 'amount': 20000, 'timestamp': '2023-01-18T10:00:00'},
        {'sender': 'AccX', 'receiver': 'VolumeAcc', 'amount': 15000, 'timestamp': '2023-01-18T11:00:00'},
        {'sender': 'VolumeAcc', 'receiver': 'AccY', 'amount': 10000, 'timestamp': '2023-01-18T12:00:00'},
        {'sender': 'AccY', 'receiver': 'VolumeAcc', 'amount': 8000, 'timestamp': '2023-01-18T13:00:00'},
    ]

    detection_config = {
        'HIGH_VALUE_THRESHOLD': 10000,
        'BLACKLISTED_ACCOUNTS': {'BlacklistedAcc', 'AnotherBadAcc'},
        'MAX_TRANSACTIONS_PER_DAY': 5,
        'MAX_DAILY_VOLUME': 50000
    }

    suspicious = find_suspicious_accounts(transactions_data, detection_config)
    print(sorted(list(suspicious)))