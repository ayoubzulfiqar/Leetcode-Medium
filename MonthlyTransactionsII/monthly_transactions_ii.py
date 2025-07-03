import datetime
from collections import defaultdict

class Solution:
    def analyze_transactions(self, transactions):
        """
        Analyzes a list of transactions to generate monthly reports.

        Args:
            transactions (list): A list of transaction dictionaries.
                                 Each dictionary is expected to have:
                                 - 'id': str (unique transaction ID)
                                 - 'date': str (transaction date in 'YYYY-MM-DD' format)
                                 - 'amount': float (transaction amount)
                                 - 'state': str (e.g., 'approved', 'declined', 'chargeback')

        Returns:
            dict: A dictionary where keys are months ('YYYY-MM') and values are
                  dictionaries containing aggregated statistics for that month.
                  Example structure for a month:
                  {
                      'total_transactions': int,
                      'total_amount': float,
                      'approved_count': int,
                      'approved_amount': float,
                      'declined_count': int,
                      'declined_amount': float,
                      'chargeback_count': int,
                      'chargeback_amount': float
                  }
        """
        monthly_reports = defaultdict(lambda: {
            'total_transactions': 0,
            'total_amount': 0.0,
            'approved_count': 0,
            'approved_amount': 0.0,
            'declined_count': 0,
            'declined_amount': 0.0,
            'chargeback_count': 0,
            'chargeback_amount': 0.0,
        })

        for transaction in transactions:
            try:
                transaction_date_str = transaction['date']
                amount = float(transaction['amount'])
                state = transaction['state'].lower()

                date_obj = datetime.datetime.strptime(transaction_date_str, '%Y-%m-%d')
                month_key = date_obj.strftime('%Y-%m')

                monthly_reports[month_key]['total_transactions'] += 1
                monthly_reports[month_key]['total_amount'] += amount

                if state == 'approved':
                    monthly_reports[month_key]['approved_count'] += 1
                    monthly_reports[month_key]['approved_amount'] += amount
                elif state == 'declined':
                    monthly_reports[month_key]['declined_count'] += 1
                    monthly_reports[month_key]['declined_amount'] += amount
                elif state == 'chargeback':
                    monthly_reports[month_key]['chargeback_count'] += 1
                    monthly_reports[month_key]['chargeback_amount'] += amount
                
            except (KeyError, ValueError):
                continue

        return dict(monthly_reports)