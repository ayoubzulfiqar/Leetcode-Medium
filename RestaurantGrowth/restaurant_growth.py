import pandas as pd
from datetime import date

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer['visited_on'] = pd.to_datetime(customer['visited_on'])

    daily_total = customer.groupby('visited_on')['amount'].sum().reset_index()

    min_date = daily_total['visited_on'].min()
    max_date = daily_total['visited_on'].max()
    full_date_range = pd.date_range(start=min_date, end=max_date, freq='D')

    full_df = pd.DataFrame(full_date_range, columns=['visited_on'])

    full_df = pd.merge(full_df, daily_total, on='visited_on', how='left').fillna(0)

    full_df = full_df.sort_values(by='visited_on')

    full_df['amount_7_day_sum'] = full_df['amount'].rolling(window=7, min_periods=7).sum()

    full_df['average_amount'] = (full_df['amount_7_day_sum'] / 7).round(2)

    result_df = full_df[full_df['amount_7_day_sum'].notna()].copy()

    result_df.rename(columns={'amount_7_day_sum': 'amount'}, inplace=True)

    result_df = result_df[['visited_on', 'amount', 'average_amount']]

    result_df['visited_on'] = result_df['visited_on'].dt.date

    return result_df