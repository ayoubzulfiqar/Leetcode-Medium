import pandas as pd

def find_product_recommendation_pairs(product_purchases: list[dict], product_info: list[dict]) -> list[dict]:
    df_purchases = pd.DataFrame(product_purchases)
    df_info = pd.DataFrame(product_info)

    df_merged_purchases = pd.merge(
        df_purchases,
        df_purchases,
        on='user_id',
        suffixes=('_1', '_2')
    )

    df_product_pairs = df_merged_purchases[
        df_merged_purchases['product_id_1'] < df_merged_purchases['product_id_2']
    ].copy()

    df_customer_counts = df_product_pairs.groupby(['product_id_1', 'product_id_2'])['user_id'].nunique().reset_index()
    df_customer_counts.rename(columns={'user_id': 'customer_count'}, inplace=True)

    df_filtered_pairs = df_customer_counts[df_customer_counts['customer_count'] >= 3]

    df_result = pd.merge(
        df_filtered_pairs,
        df_info[['product_id', 'category']],
        left_on='product_id_1',
        right_on='product_id',
        how='left'
    )
    df_result.rename(columns={'category': 'product1_category'}, inplace=True)
    df_result.drop(columns=['product_id'], inplace=True)

    df_result = pd.merge(
        df_result,
        df_info[['product_id', 'category']],
        left_on='product_id_2',
        right_on='product_id',
        how='left'
    )
    df_result.rename(columns={'category': 'product2_category'}, inplace=True)
    df_result.drop(columns=['product_id'], inplace=True)

    df_final = df_result[[
        'product_id_1',
        'product_id_2',
        'product1_category',
        'product2_category',
        'customer_count'
    ]]
    df_final.rename(columns={
        'product_id_1': 'product1_id',
        'product_id_2': 'product2_id'
    }, inplace=True)

    df_final_sorted = df_final.sort_values(
        by=['customer_count', 'product1_id', 'product2_id'],
        ascending=[False, True, True]
    )

    return df_final_sorted.to_dict(orient='records')