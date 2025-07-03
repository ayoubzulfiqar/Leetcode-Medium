def get_first_year_sales(sales_table, product_table):
    first_sale_year_map = {}
    for sale in sales_table:
        product_id = sale['product_id']
        year = sale['year']
        if product_id not in first_sale_year_map or year < first_sale_year_map[product_id]:
            first_sale_year_map[product_id] = year

    result = []
    for sale in sales_table:
        product_id = sale['product_id']
        year = sale['year']
        
        if product_id in first_sale_year_map and year == first_sale_year_map[product_id]:
            result.append({
                'product_id': product_id,
                'first_year': year,
                'quantity': sale['quantity'],
                'price': sale['price']
            })
            
    return result