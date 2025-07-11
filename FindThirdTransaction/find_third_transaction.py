import sys
from collections import defaultdict, namedtuple

Transaction = namedtuple('Transaction', ['tid', 'uid', 'timestamp', 'amount'])

def find_third_transaction():
    user_transactions = defaultdict(list)
    
    try:
        N = int(sys.stdin.readline().strip())
    except ValueError:
        return

    for _ in range(N):
        line = sys.stdin.readline().strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) != 4:
            continue

        try:
            tid = int(parts[0])
            uid = int(parts[1])
            timestamp = int(parts[2])
            amount = float(parts[3])
            
            transaction = Transaction(tid, uid, timestamp, amount)
            user_transactions[uid].append(transaction)
        except ValueError:
            continue

    results = []

    for uid in sorted(user_transactions.keys()):
        transactions_for_user = user_transactions[uid]
        transactions_for_user.sort(key=lambda t: t.timestamp)
        
        if len(transactions_for_user) >= 3:
            third_transaction = transactions_for_user[2]
            results.append(third_transaction.tid)

    for tid in results:
        print(tid)

if __name__ == '__main__':
    find_third_transaction()