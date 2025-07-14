def calculate_product_final_price(base_price, tax_rate, discount_rate, shipping_cost):
    price_after_discount = base_price * (1 - discount_rate)
    price_after_tax = price_after_discount * (1 + tax_rate)
    final_price = price_after_tax + shipping_cost
    return final_price

if __name__ == "__main__":
    product_base_price = 100.00
    product_tax_rate = 0.08
    product_discount_rate = 0.10
    product_shipping_cost = 5.00

    calculated_final_price = calculate_product_final_price(
        product_base_price,
        product_tax_rate,
        product_discount_rate,
        product_shipping_cost
    )

    print(f"{calculated_final_price:.2f}")