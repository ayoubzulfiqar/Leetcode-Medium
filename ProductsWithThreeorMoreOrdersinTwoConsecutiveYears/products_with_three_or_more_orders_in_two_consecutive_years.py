def find_products_with_consecutive_orders(orders):
    product_year_counts = {}
    for product_id, year in orders:
        product_year_counts[(product_id, year)] = product_year_counts.get((product_id, year), 0) + 1

    eligible_product_years_set = set()
    for (product_id, year), count in product_year_counts.items():
        if count >= 3:
            eligible_product_years_set.add((product_id, year))

    product_to_eligible_years = {}
    for product_id, year in eligible_product_years_set:
        if product_id not in product_to_eligible_years:
            product_to_eligible_years[product_id] = []
        product_to_eligible_years[product_id].append(year)

    result_product_ids = set()
    for product_id, years in product_to_eligible_years.items():
        years.sort()
        for i in range(len(years) - 1):
            if years[i+1] == years[i] + 1:
                result_product_ids.add(product_id)
                break

    return sorted(list(result_product_ids))