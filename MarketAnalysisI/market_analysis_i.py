import pandas as pd

def market_analysis_i(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = pd.to_datetime(orders['order_date'])

    orders_2019 = orders[orders['order_date'].dt.year == 2019]

    orders_in_2019_count = orders_2019['buyer_id'].value_counts().reset_index()
    orders_in_2019_count.columns = ['buyer_id', 'orders_in_2019']

    result = users.merge(
        orders_in_2019_count,
        left_on='user_id',
        right_on='buyer_id',
        how='left'
    )

    result['orders_in_2019'] = result['orders_in_2019'].fillna(0).astype(int)

    final_output = result[['user_id', 'join_date', 'orders_in_2019']]
    final_output = final_output.rename(columns={'user_id': 'buyer_id'})

    return final_output