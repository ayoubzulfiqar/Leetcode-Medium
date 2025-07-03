import pandas as pd

def immediate_food_delivery_ii(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['order_date'] = pd.to_datetime(delivery['order_date'])
    delivery['customer_pref_delivery_date'] = pd.to_datetime(delivery['customer_pref_delivery_date'])

    delivery_sorted = delivery.sort_values(by=['customer_id', 'order_date', 'delivery_id'])

    first_orders = delivery_sorted.drop_duplicates(subset=['customer_id'], keep='first')

    immediate_first_orders = first_orders[first_orders['order_date'] == first_orders['customer_pref_delivery_date']]

    num_immediate_first_orders = len(immediate_first_orders)
    total_customers = len(first_orders)

    if total_customers == 0:
        percentage = 0.00
    else:
        percentage = (num_immediate_first_orders / total_customers) * 100

    percentage = round(percentage, 2)

    result_df = pd.DataFrame({'immediate_percentage': [percentage]})

    return result_df