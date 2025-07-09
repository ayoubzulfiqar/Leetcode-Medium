import pandas as pd

def drop_type1_orders(orders_df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops Type 1 orders for customers who also have Type 0 orders.

    Args:
        orders_df (pd.DataFrame): A DataFrame with at least 'customer_id' and 'order_type' columns.
                                  'order_type' is expected to be 0 or 1.

    Returns:
        pd.DataFrame: A new DataFrame with Type 1 orders dropped for relevant customers.
    """
    # Identify unique customer IDs that have at least one Type 0 order
    customers_with_type_0 = orders_df[orders_df['order_type'] == 0]['customer_id'].unique()

    # Create a boolean mask for rows that should be DROPPED
    # A row is dropped if:
    # 1. Its 'customer_id' is in the set of customers who have Type 0 orders AND
    # 2. Its 'order_type' is 1
    mask_to_drop = (
        orders_df['customer_id'].isin(customers_with_type_0) &
        (orders_df['order_type'] == 1)
    )

    # Return the DataFrame containing only the rows that should NOT be dropped
    filtered_df = orders_df[~mask_to_drop]

    return filtered_df