def count_salary_categories(accounts: list[dict]) -> list[dict]:
    """
    Calculates the number of bank accounts for each salary category.

    Args:
        accounts: A list of dictionaries, where each dictionary represents an account
                  with 'account_id' (int) and 'income' (int).

    Returns:
        A list of dictionaries, each with 'category' (str) and 'accounts_count' (int),
        containing counts for "Low Salary", "Average Salary", and "High Salary".
        All three categories are always included, even if the count is 0.
    """
    low_salary_count = 0
    average_salary_count = 0
    high_salary_count = 0

    for account in accounts:
        income = account['income']
        if income < 20000:
            low_salary_count += 1
        elif 20000 <= income <= 50000:
            average_salary_count += 1
        else:  # income > 50000
            high_salary_count += 1

    result = [
        {"category": "Low Salary", "accounts_count": low_salary_count},
        {"category": "Average Salary", "accounts_count": average_salary_count},
        {"category": "High Salary", "accounts_count": high_salary_count}
    ]
    return result