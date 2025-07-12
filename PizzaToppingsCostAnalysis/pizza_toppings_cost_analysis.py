TOPPINGS_PRICES = {
    "pepperoni": 1.50,
    "mushrooms": 0.75,
    "onions": 0.50,
    "peppers": 0.75,
    "extra cheese": 1.00,
    "olives": 0.60,
    "ham": 1.20,
    "pineapple": 0.90,
    "bacon": 1.75
}

def calculate_toppings_cost(selected_toppings_list):
    total_cost = 0.0
    details = []
    invalid_toppings = []

    for topping in selected_toppings_list:
        topping_lower = topping.strip().lower()
        if topping_lower in TOPPINGS_PRICES:
            price = TOPPINGS_PRICES[topping_lower]
            total_cost += price
            details.append(f"{topping.strip().capitalize()}: ${price:.2f}")
        else:
            invalid_toppings.append(topping.strip())
    
    return total_cost, details, invalid_toppings

if __name__ == "__main__":
    print("Welcome to Pizza Toppings Cost Analysis!")
    print("\nAvailable Toppings and Prices:")
    for topping, price in TOPPINGS_PRICES.items():
        print(f"- {topping.capitalize()}: ${price:.2f}")

    print("\nEnter toppings you want, separated by commas (e.g., pepperoni, mushrooms, extra cheese)")
    print("Type 'exit' to quit at any time.")

    while True:
        user_input = input("\nYour selected toppings: ")
        if user_input.lower() == 'exit':
            break

        processed_toppings = [t.strip() for t in user_input.split(',') if t.strip()]

        if not processed_toppings:
            print("No toppings entered or recognized. Please try again.")
            continue

        total_cost, details, invalid_toppings = calculate_toppings_cost(processed_toppings)

        print("\n--- Order Summary ---")
        if details:
            print("Selected Toppings:")
            for detail in details:
                print(f"  {detail}")
            print(f"Total Toppings Cost: ${total_cost:.2f}")
        else:
            print("No valid toppings selected for this order.")

        if invalid_toppings:
            print("\nWarning: The following toppings were not recognized and were not added to the cost:")
            for invalid_topping in invalid_toppings:
                print(f"  - '{invalid_topping}'")

    print("\nThank you for using the Pizza Toppings Cost Analysis!")