import pandas as pd

def product_sales_analysis_iv(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    sales['total_sale_price'] = sales['quantity'] * sales['price']
    yearly_product_sales = sales.groupby(['product_id', 'year']).agg(
        total_sales=('total_sale_price', 'sum')
    ).reset_index()
    result = yearly_product_sales.merge(product, on='product_id', how='left')
    result = result[['product_id', 'product_name', 'year', 'total_sales']]
    result = result.sort_values(by=['product_id', 'year']).reset_index(drop=True)
    return result